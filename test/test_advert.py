import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from data import TestData

class TestAdvert:

#Тест1.Создание объявления неавторизованным пользователем

#Проверить произошёл переход на главную страницу
    def test_create_advert_failed(self,driver):

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))

        card_of_announcement = driver.find_element(*Buttons.CREATE_AD)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(card_of_announcement))

#Кликнуть разместить объявление и проверить, что отображается модальное окно
        card_of_announcement.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.CHECK_AUTH))
        popup_warning = driver.find_element(*Element_check.CHECK_AUTH)

#Тест2.Создание объявления авторизованным пользователем
    def test_create_advert_success(self, driver):
        wait = WebDriverWait(driver, 60, ignored_exceptions=[StaleElementReferenceException])

#Выполнить авторизацию
        login_user = WebDriverWait(driver, 180).until(expected_conditions.visibility_of_element_located(Buttons.LOGIN_BUTTON)).click()

        email = wait.until(expected_conditions.element_to_be_clickable(Auth_user.EMAIL_USER))
        email.send_keys(TestData.TEST_EMAIL)
        driver.find_element(*Auth_user.PASSWORD_USER).send_keys(TestData.VALID_PASS)

        driver.find_element(*Buttons.LOGIN_USER).click()


#Проверить произошёл переход на главную страницу
        main_page = WebDriverWait(driver, 180).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))
    


#Создать объявление
        
        create_of_advert = WebDriverWait(driver, 60).until(expected_conditions.element_to_be_clickable(Buttons.CREATE_AD))
        ActionChains(driver).double_click(create_of_advert).perform()

#Заполнить карточку
        advert_title = f"Куплю книги {random.randint(1000, 9999)} Гарри Поттера"

        advert = driver.find_element(*Auth_user.NAME_PRODUCT)
        advert.send_keys(advert_title)

        describe_product = driver.find_element(*Auth_user.DESCRIBE_PRODUCT)
        driver.execute_script("arguments[0].scrollIntoView();",describe_product)
        driver.execute_script("arguments[0].value = 'Куплю все части';", describe_product)

        price_product = driver.find_element(*Auth_user.PRICE_PRODUCT)
        price_product.send_keys("1000000")

# Открываем выпадающий список и выбираем категорию
        dropdown_list_product = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(Element_check.LIST))
        dropdown_list_product.click()
        type_product = driver.find_element(*Element_check.TYPE_PRODUCT)
        driver.execute_script("arguments[0].click();", type_product)
        selected = driver.find_element(*Element_check.DROPDOWN_LIST)

        category_product = driver.find_element(*Auth_user.CATEGORY_PRODUCT)
        assert category_product.get_attribute("value") == "Книги"

        dpopdown_list_city = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(Element_check.LIST))
        dpopdown_list_city[1].click()
        city_product = driver.find_element(*Element_check.TYPE_CITY)
        driver.execute_script("arguments[0].click();", city_product)
        selected_city = driver.find_element(*Element_check.DROPDOWN_LIST)
        category_city = driver.find_element(*Auth_user.CATEGORY_CITY)
        assert category_city.get_attribute("value") == "Казань"

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.RADIO_BUTTON))
        not_new_product = driver.find_element(*Element_check.NAME_BUTTON)
        not_new_product.click()
        assert not_new_product.text == "Б/У"


        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Buttons.CREATE_AD_USER))
        create_advert = driver.find_element(*Buttons.CREATE_AD_USER).click()

#Проверить, что отобржается созданное объявление
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))


        avatar_user = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.PHOTO_USER))
        avatar_user.click()

        my_advert = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Element_check.MYSELF_ADVERT))
        assert "Куплю книги" in my_advert.text





