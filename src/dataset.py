import json
from pathlib import Path
from typing import cast

from PIL import Image
from torch import Tensor
from torch.utils.data import Dataset as TorchDataset
from torchvision.transforms.v2.functional import pil_to_tensor, to_grayscale, to_pil_image

from src.history import History
from src.model import Model

# return image piexels, labels, history.xml
class Dataset(TorchDataset[tuple[Tensor, Tensor, str]]):
    def __init__(
        self,
        data: list[History],
        model: Model,
        *,
        training: bool = True,
    ) -> None:
        self.data = data
        self.model = model
        self.training = training

    def __getitem__(self, index: int) -> tuple[Tensor, Tensor, str]:
        history = self.data[index]

        image = Image.open(history.image_path)

        pixel_values = self._image_to_tensor(image, random_padding=self.training)
        # labels are converted from json to xml here
        labels = self._target_string_to_tensor(history.special_xml)

        return pixel_values, labels, history.special_xml

    def __len__(self) -> int:
        return len(self.data)

    @classmethod
    def load(
        cls,
        path: Path,
        model: Model,
        *,
        training: bool = True,
    ) -> "Dataset":
        with (path / "label.json").open() as f:
            labels_json = cast(list[dict], json.load(f))

        return cls(
            [
                History(
                image_path=label_json["image_path"],
                company_number=label_json["company_number"],
                company_name1=label_json["company_name1"],
                company_name2=label_json["company_name2"],
                company_address1=label_json["company_address1"],
                company_address2=label_json["company_address2"],
                director_name=label_json["director_name"],
                supervisor_name=label_json["supervisor_name"],
                ceo_address_line=label_json["ceo_address_line"],
                ceo_name_line=label_json["ceo_name_line"],
                ceo_address=label_json["ceo_address"],
                ceo_name=label_json["ceo_name"],

                company_name_change_date1=label_json["company_name_change_date1"],
                company_name_register_date1=label_json["company_name_register_date1"],
                company_name_change_date2=label_json["company_name_change_date2"],
                company_name_register_date2=label_json["company_name_register_date2"],
                company_address_change_date1=label_json["company_address_change_date1"],
                company_address_register_date1=label_json["company_address_register_date1"],
                company_address_change_date2=label_json["company_address_change_date2"],
                company_address_register_date2=label_json["company_address_register_date2"],
                company_launch_date=label_json["company_launch_date"],
                purpose1=label_json["purpose1"],
                purpose_change_date1=label_json["purpose_change_date1"],
                purpose_register_date1=label_json["purpose_register_date1"],
                purpose2=label_json["purpose2"],
                purpose_change_date2=label_json["purpose_change_date2"],
                purpose_register_date2=label_json["purpose_register_date2"],
                director_change_date=label_json["director_change_date"],
                director_register_date=label_json["director_register_date"],
                supervisor_change_date=label_json["supervisor_change_date"],
                supervisor_register_date=label_json["supervisor_register_date"],
                ceo_line_change_date=label_json["ceo_line_change_date"],
                ceo_line_register_date=label_json["ceo_line_register_date"],
                ceo_change_date=label_json["ceo_change_date"],
                ceo_register_date=label_json["ceo_register_date"]
            )

                for label_json in labels_json
            ],
            model,
            training=training,
        )

    def _gray_scaling_image(self, image: Image.Image) -> Image.Image:
        return to_pil_image(to_grayscale(pil_to_tensor(image)))

    def _image_to_tensor(self, image: Image.Image, *, random_padding: bool) -> Tensor:
        preprocess_image = self._gray_scaling_image(image)
        pixel_values = cast(
            Tensor,
            self.model.processor(
                preprocess_image.convert("RGB"),
                random_padding=random_padding,
                return_tensors="pt",
            ).pixel_values,
        )

        return pixel_values.squeeze()

    def _target_string_to_tensor(self, target: str) -> Tensor:
        ignore_id = -100
        input_ids = cast(
            Tensor,
            self.model.tokenizer(
                target,
                add_special_tokens=False,
                max_length=self.model.model.config.decoder.max_length,
                padding="max_length",
                truncation=True,
                return_tensors="pt",
                return_special_tokens_mask=True,
            ).input_ids,
        ).squeeze(0)

        labels = input_ids.clone()
        labels[labels == self.model.tokenizer.pad_token_id] = ignore_id

        return labels
