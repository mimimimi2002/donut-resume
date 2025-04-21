from typing import cast

from torch import FloatTensor, LongTensor, Tensor
from transformers import (
    LogitsProcessor,
    XLMRobertaTokenizer,
)

from src.history import History
import torch


# adjust processor
class InferenceLogitsProcessor(LogitsProcessor):
    def __init__(self, tokenizer: XLMRobertaTokenizer) -> None:
        self.tokenizer = tokenizer
        self.special_tokens = History.get_xml_tags()
        self.special_token_ids = cast(
            list[int],
            tokenizer.convert_tokens_to_ids(self.special_tokens),
        )


    # get the last token id for last special token in input id, if it is generated characters,
    # it will traverse back until it finds special token
    def _last_tag(self, ids: Tensor) -> str:
        last_special_token_id = next(
            (token_id for token_id in reversed(ids.tolist()) if token_id in self.special_token_ids),
        )
        return self.tokenizer.convert_ids_to_tokens(last_special_token_id)

    # *change point to have candidate tags that can be predicted from the last tags
    # @staticmethod
    # def _candidate_tags(last_tag: str) -> list[str]:
    #     return {
    #         "<s>": ["<s_cert_title>"],
    #         "<s_cert_title>": ["</s_cert_title>"],
    #         "</s_cert_title>": ["<s_cert_title_detail>"],
    #         "<s_cert_title_detail>": ["</s_cert_title_detail>", "<s_cert_title_detail_block>"],
    #         "<s_cert_title_detail_block>": ["</s_cert_title_detail_block>", "<s_cert_detail_underline>", "<s_cert_title_detail_left_block>"],
    #         "<s_cert_detail_underline>" : ["</s_cert_detail_underline>"],
    #         "<s_cert_title_detail_left_block>" : ["<s_cert_detail_underline>", "<s_cert_detail_no_line>"],
    #         "<s_cert_detail_no_line>" : ["</s_cert_detail_no_line>"],
    #         "</s_cert_title_detail>" : ["<s_cert_title>", "</s>"],
    #         "</s_cert_title_detail_block>" : ["<s_cert_title_detail_block>", "</s_cert_title_detail>"],
    #         "</s_cert_detail_underline>" : ["</s_cert_title_detail_block>", "<s_cert_detail_no_line>"],
    #         "</s_cert_detail_no_line>" : ["</s_cert_title_detail_left_block>", "</s_cert_title_detail_block>"],
    #         "</s_cert_title_detail_left_block>" : ["<s_cert_title_detail_right_block>"],
    #         "<s_cert_title_detail_right_block>" : ["<s_cert_title_detail_right_up_block>"],
    #         "</s_cert_title_detail_right_block>" : ["</s_cert_title_detail_block>"],
    #         "<s_cert_title_detail_right_up_block>" : ["<s_cert_title_detail_right_down_block>"],
    #         "<s_cert_title_detail_right_down_block>" : ["/<s_cert_title_detail_right_down_block>"],
    #         "</<s_cert_title_detail_right_down_block>" : ["</s_cert_title_detail_right_block>"],
    #         "</s_cert_title_detail_right_up_block>" : ["</s_cert_title_detail_block>"],

    #     }[last_tag]

    @staticmethod
    def _candidate_tags(last_tag: str) -> list[str]:
        return {
            "<s>": ["<s_record>"],
            "<s_record>": ["<s_company_number>"],
            "<s_company_number>": ["</s_company_number>"],
            "</s_company_number>": ["<s_company_name_first>"],
            "<s_company_name_first>": ["</s_company_name_first>"],
            "</s_company_name_first>": ["<s_company_name_change_date_first>"],
            "<s_company_name_change_date_first>": ["</s_company_name_change_date_first>"],
            "</s_company_name_change_date_first>": ["<s_company_name_register_date_first>"],
            "<s_company_name_register_date_first>": ["</s_company_name_register_date_first>"],
            "</s_company_name_register_date_first>": ["<s_company_name_second>"],
            "<s_company_name_second>": ["</s_company_name_second>"],
            "</s_company_name_second>": ["<s_company_name_change_date_second>"],
            "<s_company_name_change_date_second>": ["</s_company_name_change_date_second>"],
            "</s_company_name_change_date_second>": ["<s_company_name_register_date_second>"],
            "<s_company_name_register_date_second>": ["</s_company_name_register_date_second>"],
            "</s_company_name_register_date_second>": ["<s_company_address_first>"],
            "<s_company_address_first>": ["</s_company_address_first>"],
            "</s_company_address_first>": ["<s_company_address_change_date_first>"],
            "<s_company_address_change_date_first>": ["</s_company_address_change_date_first>"],
            "</s_company_address_change_date_first>": ["<s_company_address_register_date_first>"],
            "<s_company_address_register_date_first>": ["</s_company_address_register_date_first>"],
            "</s_company_address_register_date_first>": ["<s_company_address_second>"],
            "<s_company_address_second>": ["</s_company_address_second>"],
            "</s_company_address_second>": ["<s_company_address_change_date_second>"],
            "<s_company_address_change_date_second>": ["</s_company_address_change_date_second>"],
            "</s_company_address_change_date_second>": ["<s_company_address_register_date_second>"],
            "<s_company_address_register_date_second>": ["</s_company_address_register_date_second>"],
            "</s_company_address_register_date_second>": ["<s_company_launch_date>"],
            "<s_company_launch_date>": ["</s_company_launch_date>"],
            "</s_company_launch_date>": ["<s_purpose_first>"],
            "<s_purpose_first>": ["</s_purpose_first>"],
            "</s_purpose_first>": ["<s_purpose_change_date_first>"],
            "<s_purpose_change_date_first>": ["</s_purpose_change_date_first>"],
            "</s_purpose_change_date_first>": ["<s_purpose_register_date_first>"],
            "<s_purpose_register_date_first>": ["</s_purpose_register_date_first>"],
            "</s_purpose_register_date_first>": ["<s_purpose_second>"],
            "<s_purpose_second>": ["</s_purpose_second>"],
            "</s_purpose_second>": ["<s_purpose_register_date_second>"],
            "<s_purpose_register_date_second>": ["</s_purpose_register_date_second>"],
            "</s_purpose_register_date_second>": ["<s_director_name>"],
            "<s_director_name>": ["</s_director_name>"],
            "</s_director_name>": ["<s_director_change_date>"],
            "<s_director_change_date>": ["</s_director_change_date>"],
            "</s_director_change_date>": ["<s_director_register_date>"],
            "<s_director_register_date>": ["</s_director_register_date>"],
            "</s_director_register_date>": ["<s_supervisor_name>"],
            "<s_supervisor_name>": ["</s_supervisor_name>"],
            "</s_supervisor_name>": ["<s_supervisor_change_date>"],
            "<s_supervisor_change_date>": ["</s_supervisor_change_date>"],
            "</s_supervisor_change_date>": ["<s_supervisor_register_date>"],
            "<s_supervisor_register_date>": ["</s_supervisor_register_date>"],
            "</s_supervisor_register_date>": ["<s_ceo_address_line>"],
            "<s_ceo_address_line>": ["</s_ceo_address_line>"],
            "</s_ceo_address_line>": ["<s_ceo_name_line>"],
            "<s_ceo_name_line>": ["</s_ceo_name_line>"],
            "</s_ceo_name_line>": ["<s_ceo_line_change_date>"],
            "<s_ceo_line_change_date>": ["</s_ceo_line_change_date>"],
            "</s_ceo_line_change_date>": ["<s_ceo_line_register_date>"],
            "<s_ceo_line_register_date>": ["</s_ceo_line_register_date>"],
            "</s_ceo_line_register_date>": ["<s_ceo_address>"],
            "<s_ceo_address>": ["</s_ceo_address>"],
            "</s_ceo_address>": ["<s_ceo_name>"],
            "<s_ceo_name>": ["</s_ceo_name>"],
            "</s_ceo_name>": ["<s_ceo_change_date>"],
            "<s_ceo_change_date>": ["</s_ceo_change_date>"],
            "</s_ceo_change_date>": ["<s_ceo_register_date>"],
            "<s_ceo_register_date>": ["</s_ceo_register_date>"],
            "</s_ceo_register_date>": ["</s_record>"],
            "</s_record>": ["</s>"]
        }[last_tag]





    # input_ids are input for decoder and based on the last input, they will predict the next token ids
    # they did not specify the next token but, if it is not in candidate_tags they will have negative scores
    # it doesn't mean it will guarantee the corresponding tag, but the unexpected tags have lower chance to come to next
    # it can come characters because we did not specify the character's score
    def __call__(self, input_ids, scores):
        for i_row in range(len(input_ids)):
            ids = input_ids[i_row]

            last_tag_label = self._last_tag(ids)

            candidates = self._candidate_tags(last_tag_label)
            forbidden = [
                token_id
                for token_id in self.special_token_ids
                if self.tokenizer.convert_ids_to_tokens(token_id) not in candidates
            ]

            scores[i_row, forbidden] = -float("inf")

        return scores
