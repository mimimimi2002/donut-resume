import warnings
from pathlib import Path
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning
from PIL import Image, ImageDraw, ImageFont
from src.history import History
import random
import pandas as pd
from dataclasses import asdict
import json
from src.purpose import purposes_dict

DATASET_PATH = Path("dataset/train3")
LABEL_PATH = DATASET_PATH / "label.json"
OUTPUT_PATH = DATASET_PATH / "output.json"
IMAGE_DIR = DATASET_PATH / "image"
IMAGE_SIZE = (700, 500)
DATASET_LENGTH = 1000

person_info_path = "name.csv"
company_info_path = "00_zenkoku_all_20250331.csv"

person_df = pd.read_csv(person_info_path)
company_df = pd.read_csv(company_info_path, header=None, low_memory=False)
company_num = len(company_df)
now_year = 2025

# === 配置 ===
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
xml_path = Path("cert_data.xml")
xml_demo_path = Path("cert_data_demo.xml")
font_path = "msmincho.ttc"
output_path = "cert_table.png"
font_size = 28
padding = 5
line_spacing = 5

def random_company_number():
  i = random.randint(0, company_num -1)
  number = str(company_df.iloc[i, 1])
  return number[:4] + "-" + number[4:6] + "-" + number[6:12]

def random_company_info():
    i = random.randint(0, company_num -1)
    company_name = str(company_df.iloc[i, 6])
    company_address = str(company_df.iloc[i, 9]) + str(company_df.iloc[i, 10]) + str(company_df.iloc[i, 11])
    return company_name, company_address

def random_person_name():
    person_name = random.choice(person_df.loc[:, '氏名'].dropna().tolist())
    return person_name

def random_person_address():
    person_address = random.choice(person_df.loc[:, '住所'].dropna().tolist())
    return person_address

def random_date():
    import random

    # Define the range for the "和暦" (Japanese era years)
    era_years = [
        ("令和", 2019, now_year),  # Reiwa era, started in 2019
        ("平成", 1989, 2019),  # Heisei era, lasted until 2019
        ("昭和", 1926, 1989),  # Showa era, lasted until 1989
    ]

    # Randomly select an era and generate a random year in that era
    era, start_year, end_year = random.choice(era_years)
    year_in_era = random.randint(1, end_year - start_year + 1)
    era_year = start_year + year_in_era - 1

    # Randomly generate a month and day
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    # Format the result in 和暦 XX年 XX月 XX日
    random_date = f"{era} {year_in_era}年 {month}月 {day}日"
    return random_date


def get_random_purpose():
  num = 6
  purposes = ""
  for i in range(num):
    id = random.randint(0, len(purposes_dict) - 1)
    random_purpose = purposes_dict[id]
    purposes += str(i+1) + ". " + random_purpose

  return purposes


def generate_dummy_resume(image_num: int):
    # generate random xml
    company_number=random_company_number()
    company_name1, company_address1 = random_company_info()
    company_name2, company_address2 = random_company_info()
    director_name = random_person_name()
    supervisor_name=random_person_name()
    ceo_address_line=random_person_address()
    ceo_name_line=random_person_name()
    ceo_address=random_person_address()
    ceo_name=random_person_name()
    company_name_change_date1 = random_date()
    company_name_register_date1 = random_date()
    company_name_change_date2 = random_date()
    company_name_register_date2 = random_date()
    company_address_change_date1 = random_date()
    company_address_register_date1 = random_date()
    company_address_change_date2 = random_date()
    company_address_register_date2 = random_date()
    company_launch_date = random_date()
    purpose1 = get_random_purpose()
    purpose_change_date1 = random_date()
    purpose_register_date1 = random_date()
    purpose2 = get_random_purpose()
    purpose_change_date2 = random_date()
    purpose_register_date2 = random_date()
    director_change_date = random_date()
    director_register_date = random_date()
    supervisor_change_date = random_date()
    supervisor_register_date = random_date()
    ceo_line_change_date = random_date()
    ceo_line_register_date = random_date()
    ceo_change_date = random_date()
    ceo_register_date = random_date()


    new_history =  History (
        image_path=f"{IMAGE_DIR}/{image_num}.png",
        company_number=company_number,
        company_name1=company_name1,
        company_name2=company_name2,
        company_address1 = company_address1,
        company_address2 = company_address2,
        director_name = director_name,
        supervisor_name=supervisor_name,
        ceo_address_line=ceo_address_line,
        ceo_name_line=ceo_name_line,
        ceo_address=ceo_address,
        ceo_name=ceo_name,
        company_name_change_date1=company_name_change_date1,
        company_name_register_date1=company_name_register_date1,
        company_name_change_date2=company_name_change_date2,
        company_name_register_date2=company_name_register_date2,
        company_address_change_date1=company_address_change_date1,
        company_address_register_date1=company_address_register_date1,
        company_address_change_date2=company_address_change_date2,
        company_address_register_date2=company_address_register_date2,
        company_launch_date=company_launch_date,
        purpose1=purpose1,
        purpose_change_date1=purpose_change_date1,
        purpose_register_date1=purpose_register_date1,
        purpose2=purpose2,
        purpose_change_date2=purpose_change_date2,
        purpose_register_date2=purpose_register_date2,
        director_change_date=director_change_date,
        director_register_date=director_register_date,
        supervisor_change_date=supervisor_change_date,
        supervisor_register_date=supervisor_register_date,
        ceo_line_change_date=ceo_line_change_date,
        ceo_line_register_date=ceo_line_register_date,
        ceo_change_date=ceo_change_date,
        ceo_register_date=ceo_register_date,
    )


    with open(xml_demo_path, "w", encoding="utf-8") as f:
        f.write(new_history.xml)



    # === 加载 XML 和字体 ===
    with xml_demo_path.open("r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "lxml-xml")
    font = ImageFont.truetype(str(font_path), font_size)

    # === 解析 XML 结构 ===
    rows = []
    titles = soup.find_all("s_cert_title")
    details = soup.find_all("s_cert_title_detail")

    def create_special_str_mixed_line(left):
        left_line = left.find("s_cert_detail_underline")
        left_no_line = left.find("s_cert_detail_no_line")
        if left_line:
            left_text_line = left_line.get_text(" ", strip=True)
        else: left_text_line = ""
        if left_no_line:
            left_text_no_line = left_no_line.get_text(" ", strip=True)
        else: left_text_no_line = ""

        for child in left.children:
            child_str = str(child).strip()

            if not child_str:
                continue  # skip empty / whitespace-only children

            if "s_cert_detail_no_line" in child_str:
                if left_text_no_line:
                    return left_text_no_line + "\n" + "<" + left_text_line + ">"
                else:
                    return "<" + left_text_line + ">"
            elif "s_cert_detail_underline" in child_str:
                # First meaningful child is not s_cert_detail_no_line
                if left_text_line:
                    return "<" + left_text_line + ">" + "\n" + left_text_no_line
                else: return left_text_no_line

    for title, detail in zip(titles, details):
        title_text = title.get_text(strip=True)
        blocks =  detail.find_all("s_cert_title_detail_block")

        if blocks:
            for i, block in enumerate(blocks):
                left_blocks = block.find_all("s_cert_title_detail_left_block")
                right_blocks = block.find_all("s_cert_title_detail_right_block")
                if left_blocks and right_blocks:
                    for j, (left, right) in enumerate(zip(left_blocks, right_blocks)):
                        #left_text = left.get_text(" ", strip=True)

                        left_text = create_special_str_mixed_line(left)
                        right_up = right.find("s_cert_title_detail_right_up_block")
                        right_down = right.find("s_cert_title_detail_right_down_block")

                        if right_up or right_down:
                            if right_up:
                                rows.append([title_text if (i == 0 and j == 0) else "", left_text, right_up.get_text(strip=True), False])
                                title_text, left_text = "", ""
                            if right_down:
                                rows.append([title_text if (i == 0 and j == 0) else "", left_text, right_down.get_text(strip=True), False])
                        else:
                            rows.append([title_text if (i == 0 and j == 0) else "", left_text, right.get_text(" ", strip=True), False])
                else:
                    underline = detail.find("s_cert_detail_underline")
                    no_line = detail.find("s_cert_detail_no_line")

                    # whole sentence is underlined
                    if underline and not no_line:
                        detail_text = underline.get_text(" ", strip=True)
                        rows.append([title_text if i == 0 else "", detail_text, None, True]) # None 表示合并 2-3 列 , is_underline is true means it should be underlined

                    # some sentence is underlined and the other is not lined
                    elif underline and no_line:
                        detail_text = create_special_str_mixed_line(block)
                        rows.append([title_text if i == 0 else "", detail_text, None, False])

                    # not underlined
                    else:
                        detail_text = block.get_text(" ", strip=True)
                        rows.append([title_text if i == 0 else "", detail_text, None, False]) # None 表示合并 2-3 列 , is_underline is true means it should be underlined

        else:
            underline = detail.find("s_cert_detail_underline")
            no_line = detail.find("s_cert_detail_no_line")

            # whole sentence is underlined
            if underline and not no_line:
                detail_text = underline.get_text(" ", strip=True)
                rows.append([title_text, detail_text, None, True]) # None 表示合并 2-3 列 , is_underline is true means it should be underlined

            # some sentence is underlined and the other is not lined
            elif underline and no_line:
                detail_text = create_special_str_mixed_line(detail)
                rows.append([title_text, detail_text, None, False])

            # not underlined
            else:
                detail_text = detail.get_text(" ", strip=True)
                rows.append([title_text, detail_text, None, False]) # None 表示合并 2-3 列 , is_underline is true means it should be underlined

    # === 第一列换行：超过9个字符强制换行
    def wrap_japanese(text, max_chars=8):
        if text and len(text) > max_chars:
            return text[:max_chars] + "\n" + text[max_chars:]
        return text

    for i in range(len(rows)):
        rows[i][0] = wrap_japanese(rows[i][0])

    # judge if it is a number, maybe need adjust the number
    def is_number(ch):
        if '1' <= ch <= '9':
            return True
        else: return False

    # === 自动换行函数
    def wrap_text(text, width):
        if not text:
            return ""
        lines = []
        current = ""
        for i, ch in enumerate(text):
            if is_number(ch): # make new line in purpose section for each number
                next_ch = text[i+1] if i+1 < len(text) else ''
                if next_ch == "." and current:
                    if text[0] == "<":
                        lines.append(current + ">")
                    else:
                        lines.append(current)
                    current = ""
            if ch != '\n': #when ch contains \n by wrap_japanese
                bbox = font.getbbox(current + ch)
                text_width = bbox[2] - bbox[0]
                if text_width <= width - 2 * padding:
                    current += ch
                else:
                    if current:
                        if text[0] == "<":
                            lines.append(current + ">")
                        else:
                            lines.append(current)
                    current = ch
            else:
                lines.append(current)
                current = ""
        if current:
            lines.append(current)
        return "\n".join(lines)

    # === 纵向合并函数
    def merge_vertical(data, col):
        merged = []
        i = 0
        while i < len(data):
            val = data[i][col]
            span = 1
            while i + span < len(data) and data[i + span][col] == "":
                span += 1
            merged.append((i, span, val))
            i += span
        return merged

    merged_col0 = merge_vertical(rows, 0)
    merged_col1 = merge_vertical(rows, 1)

    # === 图像尺寸设置
    image_width = 1600
    col_widths = [int(image_width * r) for r in [0.15, 0.525, 0.325]] # adjust the left vertical line
    min_line_height = font_size + padding * 2
    row_heights = [min_line_height for _ in rows]

    # === 自动计算每列需要的高度
    def calculate_required_height(text, width):
        lines = wrap_text(text, width).count("\n") + 1
        return lines * font_size + (lines - 1) * line_spacing + 2 * padding

    # 自动扩展：第一列合并区域高度
    def adjust_height_for_merged(merged_col, col_idx):
        for start, span, val in merged_col:
            h_total = sum(row_heights[start:start+span])
            cell_width = col_widths[col_idx]
            if rows[start][2] is None and col_idx == 1:
                cell_width = col_widths[1] + col_widths[2]
            required_h = calculate_required_height(val, cell_width)
            if required_h > h_total:
                per_row = required_h / span
                for i in range(start, start + span):
                    row_heights[i] = max(row_heights[i], per_row)

    adjust_height_for_merged(merged_col0, 0)
    adjust_height_for_merged(merged_col1, 1)

    # 自动扩展：第三列（不合并）
    for i, row in enumerate(rows):
        if row[2] is not None:
            h = calculate_required_height(row[2], col_widths[2])
            row_heights[i] = max(row_heights[i], h)

    # === 开始绘图 ===
    image_height = int(sum(row_heights))
    img = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(img)

    # 单元格绘制函数
    def draw_cell(x0, y0, w, h, text, is_line = False):
        draw.rectangle([x0, y0, x0 + w, y0 + h], outline="black")
        if text:
            lines = wrap_text(text, w).split("\n")
            y_text = y0 + padding
            for line in lines:
                if line[0] == "<" or line[-1] == ">":
                    # if empty
                    if line[0] == "<" and line[1] == ">": continue

                    # if one line contains <-->
                    if line[0] == "<" and line[-1] == ">":
                        line = line[1:-1]

                    # if one line contins <---
                    elif line[0] == "<":
                        line = line[1:]

                    elif line[-1] == ">":
                        line = line[:-1]
                    bbox = font.getbbox(line)
                    text_width = bbox[2] - bbox[0]
                    draw.line((x0, y_text + font_size, x0 + text_width, y_text + font_size), fill='black', width=2)

                draw.text((x0 + padding, y_text), line, font=font, fill="black")
                y_text += font_size + line_spacing
                if is_line:
                    bbox = font.getbbox(line)
                    text_width = bbox[2] - bbox[0]
                    draw.line((x0, y_text - line_spacing, x0 + text_width, y_text - line_spacing), fill='black', width=2)
    # === 绘制每一行 ===
    y = 0
    for i, height in enumerate(row_heights):
        # 第一列
        for start, span, text in merged_col0:
            if start == i:
                h = sum(row_heights[start:start+span])
                draw_cell(0, y, col_widths[0], h, text)

        # 第二列
        for start, span, text in merged_col1:
            if start == i:
                h = sum(row_heights[start:start+span])
                if rows[start][2] is None:
                    draw_cell(col_widths[0], y, col_widths[1] + col_widths[2], h, text, rows[start][3])
                else:
                    draw_cell(col_widths[0], y, col_widths[1], h, text, rows[start][3])

        # 第三列（不合并）
        if rows[i][2] is not None:
            draw_cell(col_widths[0] + col_widths[1], y, col_widths[2], height, rows[i][2], rows[start][3])

        y += height

    # 画像を保存
    img.save(f"{IMAGE_DIR}/{image_num}.png")

    return new_history


#generate_dummy_resume(0)

if __name__ == "__main__":
    resumes = []

    i = 0
    while i < DATASET_LENGTH:
        resume = generate_dummy_resume(i)

        if resume is None:
            continue

        print("Generated: %s", resume)
        resumes.append(asdict(resume))

        i += 1

    print("Generated %s cards", len(resumes))

    print(LABEL_PATH)
    with LABEL_PATH.open("w") as f:
        f.write(json.dumps(resumes, ensure_ascii=False, indent=4))


