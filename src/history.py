from dataclasses import dataclass

import random
import pandas as pd
from src.purpose import purposes_dict
from typing import Optional
from typing import List

now_year = 2025

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

@dataclass
class History:
    image_path: str
    company_number: str
    company_name1: str
    company_name2: str
    company_address1: str
    company_address2: str
    director_name: str
    supervisor_name: str
    ceo_address_line: str
    ceo_name_line: str
    ceo_address: str
    ceo_name: str
    company_name_change_date1: str
    company_name_register_date1: str
    company_name_change_date2: str
    company_name_register_date2: str
    company_address_change_date1: str
    company_address_register_date1: str
    company_address_change_date2: str
    company_address_register_date2: str
    company_launch_date: str
    purpose1: str
    purpose_change_date1: str
    purpose_register_date1: str
    purpose2: str
    purpose_change_date2:str
    purpose_register_date2: str
    director_change_date: str
    director_register_date: str
    supervisor_change_date: str
    supervisor_register_date: str
    ceo_line_change_date: str
    ceo_line_register_date: str
    ceo_change_date: str
    ceo_register_date: str
    
    def get_company_name_xml(self):

      # Example logic to choose a block
      # You can replace this condition with your actual logic
      block_type = random.randint(1, 3)

      if block_type == 1:
          self.company_name2 = None
          self.company_name_change_date1 = None
          self.company_name_register_date1 = None
          self.company_name_change_date2 = None
          self.company_name_register_date2 = None
          block = f"<s_cert_title_detail>{self.company_name1}</s_cert_title_detail>"
      elif block_type == 2:
          self.company_name_change_date2 = None
          self.company_name_register_date2 = None
          block = f"""
          <s_cert_title_detail>
            <s_cert_title_detail_block>
                <s_cert_detail_underline>{self.company_name1}</s_cert_detail_underline>
            </s_cert_title_detail_block>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline></s_cert_detail_underline>
                <s_cert_detail_no_line>{self.company_name2}</s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.company_name_change_date1}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.company_name_register_date1}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
          </s_cert_title_detail>
          """
      else:
          block = f"""
          <s_cert_title_detail>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline>{self.company_name1}</s_cert_detail_underline>
                <s_cert_detail_no_line></s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.company_name_change_date1}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.company_name_register_date1}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline></s_cert_detail_underline>
                <s_cert_detail_no_line>{self.company_name2}</s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.company_name_change_date2}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.company_name_register_date2}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
          </s_cert_title_detail>
          """

      return block
    
    def get_company_address_xml(self):
      block_type = random.randint(1, 2)
      if block_type == 1:
        self.company_address2 = None
        self.company_address_change_date1 = None
        self.company_address_register_date1 = None
        self.company_address_change_date2 = None
        self.company_address_register_date2 = None
        block = f"<s_cert_title_detail>{self.company_address1}</s_cert_title_detail>"

      elif block_type == 2:
        block = f"""
          <s_cert_title_detail>
          <s_cert_title_detail_block>
            <s_cert_title_detail_left_block>
              <s_cert_detail_underline>{self.company_address1}</s_cert_detail_underline>
              <s_cert_detail_no_line></s_cert_detail_no_line>
            </s_cert_title_detail_left_block>
            <s_cert_title_detail_right_block>
              <s_cert_title_detail_right_up_block>{self.company_address_change_date1}変更</s_cert_title_detail_right_up_block>
              <s_cert_title_detail_right_down_block>{self.company_address_register_date1}登記</s_cert_title_detail_right_down_block>
            </s_cert_title_detail_right_block>
          </s_cert_title_detail_block>
          <s_cert_title_detail_block>
            <s_cert_title_detail_left_block>
              <s_cert_detail_underline></s_cert_detail_underline>
              <s_cert_detail_no_line>{self.company_address2}</s_cert_detail_no_line>
            </s_cert_title_detail_left_block>
            <s_cert_title_detail_right_block>
              <s_cert_title_detail_right_up_block>{self.company_address_change_date2}変更</s_cert_title_detail_right_up_block>
              <s_cert_title_detail_right_down_block>{self.company_address_register_date2}登記</s_cert_title_detail_right_down_block>
            </s_cert_title_detail_right_block>
          </s_cert_title_detail_block>
          </s_cert_title_detail>
          """

      return block

    def get_random_purpose():
      num = random.randint(4, 8)
      purposes = ""
      for i in range(num):
        id = random.randint(0, len(purposes_dict) - 1)
        random_purpose = purposes_dict[id]
        purposes += str(i+1) + ". " + random_purpose

      return purposes

    def get_random_purpose_xml(self):
      block = ""

      block_type = random.randint(1, 2)
      if block_type == 1:
        self.purpose2 = None
        self.purpose_change_date2 = None
        self.purpose_register_date2 = None
        block = f"<s_cert_title_detail>{self.purpose1}\n{self.purpose_change_date1} 変更 {self.purpose_register_date1} 登記</s_cert_title_detail>"

      elif block_type == 2:
        block = f"""
        <s_cert_title_detail>
        <s_cert_title_detail_block>
        <s_cert_detail_underline>{self.purpose1}</s_cert_detail_underline>
        <s_cert_detail_no_line>{self.purpose_change_date1} 変更 {self.purpose_register_date1} 登記</s_cert_detail_no_line>
        </s_cert_title_detail_block>
        <s_cert_title_detail_block>
        <s_cert_detail_underline></s_cert_detail_underline>
        <s_cert_detail_no_line>{self.purpose2}\n{self.purpose_change_date2} 変更 {self.purpose_register_date2} 登記</s_cert_detail_no_line>
        </s_cert_title_detail_block>
        </s_cert_title_detail>
        """

      return block

    def get_executive_xml(self):

      block =  f"""
        <s_cert_title_detail>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline>{self.director_name}</s_cert_detail_underline>
                <s_cert_detail_no_line></s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.director_change_date}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.director_register_date}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline></s_cert_detail_underline>
                <s_cert_detail_no_line>{self.supervisor_name}</s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.supervisor_change_date}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.supervisor_register_date}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline>{self.ceo_address_line}\n{self.ceo_name_line}</s_cert_detail_underline>
                <s_cert_detail_no_line></s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.ceo_line_change_date}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.ceo_line_register_date}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
            <s_cert_title_detail_block>
              <s_cert_title_detail_left_block>
                <s_cert_detail_underline></s_cert_detail_underline>
                <s_cert_detail_no_line>{self.ceo_address}\n{self.ceo_name}</s_cert_detail_no_line>
              </s_cert_title_detail_left_block>
              <s_cert_title_detail_right_block>
                <s_cert_title_detail_right_up_block>{self.ceo_change_date}変更</s_cert_title_detail_right_up_block>
                <s_cert_title_detail_right_down_block>{self.ceo_register_date}登記</s_cert_title_detail_right_down_block>
              </s_cert_title_detail_right_block>
            </s_cert_title_detail_block>
          </s_cert_title_detail>
      """
      return block





    @property
    def xml(self) -> str:
        return (
            "<s>"
            "<s_cert_title>会社法人等の番号</s_cert_title>"
            f"<s_cert_title_detail>{self.company_number}</s_cert_title_detail>"
            "<s_cert_title>商号</s_cert_title>"
            f"{self.get_company_name_xml()}"
            "<s_cert_title>本店</s_cert_title>"
            f"{self.get_company_address_xml()}"
            "<s_cert_title>公告する方法</s_cert_title>"
            f"<s_cert_title_detail>官報に掲載する方法により行う。</s_cert_title_detail>"
            "<s_cert_title>会社成立の年月日</s_cert_title>"
            f"<s_cert_title_detail>{self.company_launch_date}</s_cert_title_detail>"
            "<s_cert_title>目的</s_cert_title>"
            f"{self.get_random_purpose_xml()}"
            "<s_cert_title>役員に関する事項</s_cert_title>"
            f"{self.get_executive_xml()}"
            "</s>"
        )

    # @classmethod
    # def get_xml_tags(cls) -> list[str]:
    #     return [
    #         "<s>",
    #         "<s_cert_title>",
    #         "</s_cert_title>",
    #         "<s_cert_title_detail>",
    #         "</s_cert_title_detail>",
    #         "<s_cert_title_detail_block>",
    #         "</s_cert_title_detail_block>",
    #         "<s_cert_detail_underline>",
    #         "</s_cert_detail_underline>",
    #         "<s_cert_detail_no_line>",
    #         "</s_cert_detail_no_line>",
    #         "<s_cert_title_detail_left_block>",
    #         "</s_cert_title_detail_left_block>",
    #         "<s_cert_title_detail_right_block>",
    #         "</s_cert_title_detail_right_block>",
    #         "<s_cert_title_detail_right_up_block>",
    #         "</s_cert_title_detail_right_up_block>",
    #         "<s_cert_title_detail_right_down_block>",
    #         "</s_cert_title_detail_right_down_block>"
    #         "</s>",
    #     ]
    @property
    def special_xml(self) -> str:
      return (
        f"""
        <s>
          <s_record>

            <s_company_number>{self.company_number}</s_company_number>
            

            <s_company_name_first>{self.company_name1}</s_company_name_first>
            <s_company_name_change_date_first>{self.company_name_change_date1}</s_company_name_change_date_first>
            <s_company_name_register_date_first>{self.company_name_register_date1}</s_company_name_register_date_first>

            <s_company_name_second>{self.company_name2}</s_company_name_second>
            <s_company_name_change_date_second>{self.company_name_change_date2}</s_company_name_change_date_second>
            <s_company_name_register_date_second>{self.company_name_register_date2}</s_company_name_register_date_second>

            <s_company_address_first>{self.company_address1}</s_company_address_first>
            <s_company_address_change_date_first>{self.company_address_change_date1}</s_company_address_change_date_first>
            <s_company_address_register_date_first>{self.company_address_register_date1}</s_company_address_register_date_first>

            <s_company_address_second>{self.company_address2}</s_company_address_second>
            <s_company_address_change_date_second>{self.company_address_change_date2}</s_company_address_change_date_second>
            <s_company_address_register_date_second>{self.company_address_register_date2}</s_company_address_register_date_second>

            <s_company_launch_date>{self.company_launch_date}</s_company_launch_date>

            <s_purpose_first>{self.purpose1}</s_purpose_first>
            <s_purpose_change_date_first>{self.purpose_change_date1}</s_purpose_change_date_first>
            <s_purpose_register_date_first>{self.purpose_register_date1}</s_purpose_register_date_first>

            <s_purpose_second>{self.purpose2}</s_purpose_second>
            <s_purpose_register_date_second>{self.purpose_register_date2}</s_purpose_register_date_second>

            <s_director_name>{self.director_name}</s_director_name>
            <s_director_change_date>{self.director_change_date}</s_director_change_date>
            <s_director_register_date>{self.director_register_date}</s_director_register_date>

            <s_supervisor_name>{self.supervisor_name}</s_supervisor_name>
            <s_supervisor_change_date>{self.supervisor_change_date}</s_supervisor_change_date>
            <s_supervisor_register_date>{self.supervisor_register_date}</s_supervisor_register_date>

            <s_ceo_address_line>{self.ceo_address_line}</s_ceo_address_line>
            <s_ceo_name_line>{self.ceo_name_line}</s_ceo_name_line>
            <s_ceo_line_change_date>{self.ceo_line_change_date}</s_ceo_line_change_date>
            <s_ceo_line_register_date>{self.ceo_line_register_date}</s_ceo_line_register_date>

            <s_ceo_address>{self.ceo_address}</s_ceo_address>
            <s_ceo_name>{self.ceo_name}</s_ceo_name>
            <s_ceo_change_date>{self.ceo_change_date}</s_ceo_change_date>
            <s_ceo_register_date>{self.ceo_register_date}</s_ceo_register_date>
          </s_record>
        </s>

        """
      )

    @classmethod
    def get_xml_tags(cls) -> list[str]:
        return [
          "<s>",
          "<s_record>",
          "<s_company_number>", "</s_company_number>",
          "<s_company_name_first>", "</s_company_name_first>",
          "<s_company_name_change_date_first>", "</s_company_name_change_date_first>",
          "<s_company_name_register_date_first>", "</s_company_name_register_date_first>",
          "<s_company_name_second>", "</s_company_name_second>",
          "<s_company_name_change_date_second>", "</s_company_name_change_date_second>",
          "<s_company_name_register_date_second>", "</s_company_name_register_date_second>",
          "<s_company_address_first>", "</s_company_address_first>",
          "<s_company_address_change_date_first>", "</s_company_address_change_date_first>",
          "<s_company_address_register_date_first>", "</s_company_address_register_date_first>",
          "<s_company_address_second>", "</s_company_address_second>",
          "<s_company_address_change_date_second>", "</s_company_address_change_date_second>",
          "<s_company_address_register_date_second>", "</s_company_address_register_date_second>",
          "<s_company_launch_date>", "</s_company_launch_date>",
          "<s_purpose_first>", "</s_purpose_first>",
          "<s_purpose_change_date_first>", "</s_purpose_change_date_first>",
          "<s_purpose_register_date_first>", "</s_purpose_register_date_first>",
          "<s_purpose_second>", "</s_purpose_second>",
          "<s_purpose_register_date_second>", "</s_purpose_register_date_second>",
          "<s_director_name>", "</s_director_name>",
          "<s_director_change_date>", "</s_director_change_date>",
          "<s_director_register_date>", "</s_director_register_date>",
          "<s_supervisor_name>", "</s_supervisor_name>",
          "<s_supervisor_change_date>", "</s_supervisor_change_date>",
          "<s_supervisor_register_date>", "</s_supervisor_register_date>",
          "<s_ceo_address_line>", "</s_ceo_address_line>",
          "<s_ceo_name_line>", "</s_ceo_name_line>",
          "<s_ceo_line_change_date>", "</s_ceo_line_change_date>",
          "<s_ceo_line_register_date>", "</s_ceo_line_register_date>",
          "<s_ceo_address>", "</s_ceo_address>",
          "<s_ceo_name>", "</s_ceo_name>",
          "<s_ceo_change_date>", "</s_ceo_change_date>",
          "<s_ceo_register_date>", "</s_ceo_register_date>",
          "</s_record>",
          "</s>",
      ]

    @classmethod
    def get_xml_tags1(cls) -> list[str]:
        return [
            "<s>",
            "<s_cert_title>",
            "</s_cert_title>",
            "<s_cert_title_detail>",
            "</s_cert_title_detail>",
            "<s_cert_title_detail_block>",
            "</s_cert_title_detail_block>",
            "<s_cert_detail_underline>",
            "</s_cert_detail_underline>",
            "<s_cert_detail_no_line>",
            "</s_cert_detail_no_line>",
            "<s_cert_title_detail_left_block>",
            "</s_cert_title_detail_left_block>",
            "<s_cert_title_detail_right_block>",
            "</s_cert_title_detail_right_block>",
            "<s_cert_title_detail_right_up_block>",
            "</s_cert_title_detail_right_up_block>",
            "<s_cert_title_detail_right_down_block>",
            "</s_cert_title_detail_right_down_block>"
            "</s>",
        ]


