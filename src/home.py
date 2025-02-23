from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os
import subprocess
import io
import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from assertpy import assert_that

class HomePage():

    implicit_wait = 10
    TIMEOUT = 30

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(self.implicit_wait)

    def select_home_section(self, section_name):

        """

        메인 페이지 > 해당 섹션 진입
        :param(str): section_name
        :return 없음
        :example: HomeGnbPageParam.__select_home_section(self,section_name)

        """

        # 메인 페이지 > 탭+버튼 클릭
        time.sleep(2)
        runtext = '메인 페이지 > 탭+버튼 클릭'
        print("#", runtext, "시작")
        xpath = '//android.widget.ImageButton[@content-desc="메뉴 편집"]'
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print("#", runtext, "종료")

        xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tvTitle" and @text="{0}"]'.format(
            section_name)
        HomePage.__scroll_mobile_app(self, "1", xpath, 3, 30)

        runtext = '해당섹션 클릭'
        print("#", runtext, "시작")
        xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tvTitle" and @text="{0}"]'.format(
            section_name)
        time.sleep(10)
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print("#", runtext, "종료")

    def ss_1_2_1_1(self, use_type, *args):
        """
        1.2.1-1) 베스트 > 기본기능
        :param (int) use_type: 사용 여부 (1: 미사용 / 2:사용)
        :param (list) args[0]: 위로 가기 버튼
        :param (str) args[1]: 전체 베스트 버튼
        :return: 없음
        :example: gmarket_regression_vip_page_param.ss_1_2_1_1(2,*args)
        """

        if use_type == 2:
            print("#", "LP 1.2.1-1 Test Case 실행")
            runtext = '메인페이지 > 베스트 섹션 으로 이동'
            print("#", runtext, "시작")
            HomePage.__select_home_section(self, "베스트")
            print("#", runtext, "종료")

            runtext = '메인페이지 > 베스트 섹션 탑버튼 노출 확인'
            time.sleep(2)
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/topButton"
            HomePage.__scroll_mobile_app_type(self, "1", "id", id, 5, 10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            value = element.get_attribute('content-desc')
            assert_that(value).is_in(args[0])  # 위로 가기
            print("#", runtext, "종료")

            runtext = '메인페이지 > 베스트 섹션 탑버튼 클릭시 동작 확인'
            time.sleep(2)
            print("#", runtext, "시작")
            element.click()
            xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tv_title" and @text="전체 베스트"]'
            HomePage.__scroll_mobile_app(self, "2", xpath, 10, 10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            value = element.text
            assert_that(value).is_in(args[1])  # 전체 베스트
            print("#", runtext, "종료")

            # 베스트 > 새로고침 동작 확인
            runtext = '베스트 > 새로고침 동작 확인'
            print("#", runtext, "시작")
            xpath = '//android.widget.TextView[@resource-id="com.ebay.kr.gmarket:id/tv_title" and @text="전체 베스트"]'
            HomePage.__scroll_mobile_app(self, "2", xpath, 10, 10)
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            value = element.text
            assert_that(value).is_in(args[1])  # 전체 베스트
            print("#", runtext, "종료")


        else:
            print("#", "BEST 1.2.1-1 Test Case 실행 생략")

    def ss_1_5_1_1(self, use_type, *args):
        """
        1.2.1-1) 베스트 > 기본기능
        :param (int) use_type: 사용 여부 (1: 미사용 / 2:사용)
        :param (str) args[0]: 검색어
        :return: 없음
        :example: home_page.ss_1_5_1_1(2,*args)
        """

        if use_type == 2:
            print("#", "1.5.1-1 Test Case 실행")
            # 검색 페이지 진입
            runtext = '검색 페이지 진입'
            print("#", runtext, "시작")
            # id = 'com.ebay.kr.gmarket:id/tvSearchBar'
            # xpath = '//android.widget.RelativeLayout[@content-desc="무엇을 찾아드릴까요?"]'
            id = 'com.ebay.kr.gmarket:id/rlSearchBar'
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            element.click()
            print("#", runtext, "종료")

            # 지마켓메인 검색창 텍스트 입력
            runtext = '메인 페이지 > 검색창 텍스트 입력'
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/searchEditText"
            goods_name = args[0]
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, id)))
            element.send_keys(goods_name)
            print("#", runtext, "종료")

            # 지마켓메인 검색창 리턴
            runtext = '메인 페이지 > 검색창 텍스트 리턴'
            print("#", runtext, "시작")
            xpath = '//android.widget.ImageView[@content-desc="입력된 단어로 검색"]'
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            print("#", runtext, "종료")

            # 입력 및 검색된 텍스트 비교
            runtext = '메인 페이지 > 검색창 텍스트 리턴 > 입력 및 검색된 텍스트 비교'
            print("#", runtext, "시작")
            id = "com.ebay.kr.gmarket:id/searchKeyword"
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))
            value = element.text
            assert value in goods_name, f"'{value}' not found in '{goods_name}'"
            print("#", runtext, "종료")

        else:
            print("#", "1.5.1-1 Test Case 실행 생략")