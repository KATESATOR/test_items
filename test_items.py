from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_guest_should_see_add_button(browser):
    link = "http://selenium1py.pythonanywhere.com/" + "/catalogue/coders-at-work_207/"
    browser.get(link)
    WebDriverWait(browser, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))    # проверка доступности кнопки добавить
    add_to_basket_btn = browser.find_element_by_css_selector(".btn-add-to-basket")
    text_add_to_basket_btn = add_to_basket_btn.text     # получение названия кнопки добавить
    print("text of add to basket button:", text_add_to_basket_btn)
    value_add_to_basket_btn = add_to_basket_btn.get_attribute("value")  # получение параметра value кнопки добавить
    print("value of add to basket button:", value_add_to_basket_btn)
    assert text_add_to_basket_btn == value_add_to_basket_btn, "name of add basket button != value of this button"
