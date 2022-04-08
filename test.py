from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def findWorks(dr, keywords, period):
    dr.get("https://elibrary.ru/querybox.asp?scope=newquery")
    elem = dr.find_element(By.NAME, 'ftext')
    elem.send_keys(keywords)
    elem = Select(dr.find_element(By.NAME, 'orderby'))
    elem.select_by_value('insdate')
    elem = Select(dr.find_element(By.NAME, 'issues'))
    elem.select_by_value(period)
    dr.execute_script("return query_message()")


dr = webdriver.Chrome()
findWorks(dr, "кредит скоринг машинное обучение банк", "all")
input()