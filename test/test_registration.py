import random
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Buttons.LOGIN_BUTTON)).click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Buttons.REGISTER_BUTTON)).click()

        yield

#Тест1. Регистрация пользователя успешная
    def test_success_registration(self,generate_email):
        email = generate_email

        time.sleep(3)

# Выполнить авторизацию
        self.driver.find_element(*Auth_user.EMAIL_USER).send_keys(email)
        self.driver.find_element(*Auth_user.PASSWORD_USER).send_keys("Aa12345")
        self.driver.find_element(*Auth_user.SUBMIT_PASSWORD).send_keys("Aa12345")

        create_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Buttons.CREATE_ACCOUNT))
        create_button.click()

        time.sleep(3)

#Проверить отображается аватар пользователя и имя User
        photo = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.PHOTO_USER))
        assert photo.is_displayed()

        name = WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.NAME_USER))
        assert name.is_displayed()
        assert name.text == "User."

#Тест2.Регистрация пользователя неуспешная

    def test_failed_registration(self,generate_email):

        time.sleep(3)

        self.driver.find_element(*Auth_user.EMAIL_USER).send_keys("test.test")
        self.driver.find_element(*Auth_user.PASSWORD_USER).send_keys("Aa12345")
        self.driver.find_element(*Auth_user.SUBMIT_PASSWORD).send_keys("Aa12345")

        create_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Buttons.CREATE_ACCOUNT))
        create_button.click()

        time.sleep(3)

#Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным
        error_fields = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(Element_check.FAIL_CHECK))
        assert len(error_fields) > 0

#Проверить под полем Email отображается сообщение «Ошибка».pytest

        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Element_check.ERROR_CHECK))
        assert error.is_displayed()

#Тест3.Проверить регистрацию существующего пользователя

    def test_registration_exist_user(self):

        time.sleep(3)

        self.driver.find_element(*Auth_user.EMAIL_USER).send_keys("user1234@ya.ru")
        self.driver.find_element(*Auth_user.PASSWORD_USER).send_keys("Aa12345")
        self.driver.find_element(*Auth_user.SUBMIT_PASSWORD).send_keys("Aa12345")

        create_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Buttons.CREATE_ACCOUNT))
        create_button.click()

        time.sleep(3)

# Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным
        error_fields = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(Element_check.FAIL_CHECK))
        assert len(error_fields) > 0

# Проверить под полем Email отображается сообщение «Ошибка».

        error = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Element_check.ERROR_CHECK))
        assert error.is_displayed()

