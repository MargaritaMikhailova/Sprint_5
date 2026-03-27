import random
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestAdvert:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver

        yield

#Тест1.Создание объявления неавторизованным пользователем

#Проверить произошёл переход на главную страницу
    def test_create_advert_failed(self,driver):

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))

        time.sleep(3)

        card_of_announcement = self.driver.find_element(*Buttons.CREATE_AD)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(card_of_announcement))

#Кликнуть разместить объявление и проверить, что отображается модальное окно
        card_of_announcement.click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.CHECK_AUTH))
        popup_warning = self.driver.find_element(*Element_check.CHECK_AUTH)
        assert popup_warning.is_displayed()
        print("Чтобы разместить объявление, авторизуйтесь")

#Тест2.Создание объявления авторизованным пользователем
    def test_create_advert_success(self, driver):

#Выполнить авторизацию
        self.driver.find_element(*Buttons.LOGIN_BUTTON).click()

        time.sleep(3)

        self.driver.find_element(*Auth_user.EMAIL_USER).send_keys("user922@ya.ru")
        self.driver.find_element(*Auth_user.PASSWORD_USER).send_keys("Aa12345")

##time.sleep(3)

        self.driver.find_element(*Buttons.LOGIN_USER).click()


#Проверить произошёл переход на главную страницу
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))

        time.sleep(3)

#Создать объявление
        create_of_advert = self.driver.find_element(*Buttons.CREATE_AD)
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(create_of_advert))

        create_of_advert.click()

##time.sleep(3)

#Заполнить карточку
        advert_title = f"Куплю книги {random.randint(1000, 9999)} Гарри Поттера"

        advert = driver.find_element(By.NAME, "name")
        advert.send_keys(advert_title)

        describe_product = self.driver.find_element(*Auth_user.DESCRIBE_PRODUCT)
        self.driver.execute_script("arguments[0].scrollIntoView();",describe_product)
        describe_product.send_keys("Куплю все части")

        price_product = self.driver.find_element(*Auth_user.PRICE_PRODUCT)
        price_product.send_keys("1000000")

# Открываем выпадающий список и выбираем категорию
        dropdown_list_product = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Element_check.LIST))
        dropdown_list_product.click()
        type_product = self.driver.find_element(*Element_check.TYPE_PRODUCT)
        self.driver.execute_script("arguments[0].click();", type_product)
        selected = self.driver.find_element(*Element_check.DROPDOWN_LIST)

        time.sleep(3)

        category_product = self.driver.find_element(*Auth_user.CATEGORY_PRODUCT)
        assert category_product.get_attribute("value") == "Книги"

        dpopdown_list_city = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(Element_check.LIST))
        dpopdown_list_city[1].click()
        time.sleep(3)
        city_product = self.driver.find_element(*Element_check.TYPE_CITY)
        self.driver.execute_script("arguments[0].click();", city_product)
        selected_city = self.driver.find_element(*Element_check.DROPDOWN_LIST)
        #time.sleep(3)
        category_city = self.driver.find_element(*Auth_user.CATEGORY_CITY)
        assert category_city.get_attribute("value") == "Казань"

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.RADIO_BUTTON))
        not_new_product = self.driver.find_element(*Element_check.NAME_BUTTON)
        not_new_product.click()
        assert not_new_product.text == "Б/У"


        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Buttons.CREATE_AD_USER))
        create_advert = self.driver.find_element(*Buttons.CREATE_AD_USER).click()

#Проверить, что отобржается созданное объявление
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))

        time.sleep(3)

        avatar_user = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.PHOTO_USER))
        avatar_user.click()


        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MY_ADVERT))
        my_advert = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//h2[text()='{advert_title}']")))
        assert my_advert.text == advert_title



