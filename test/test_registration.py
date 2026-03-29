import random
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from selenium.common.exceptions import StaleElementReferenceException

class TestRegistration:

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver

        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(Buttons.LOGIN_BUTTON)).click()

        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable(Buttons.REGISTER_BUTTON)).click()

        yield

#Тест1. Регистрация пользователя успешная
    def test_success_registration(self,generate_email):
        wait = WebDriverWait(self.driver, 60, ignored_exceptions=[StaleElementReferenceException])
        email = generate_email

# Выполнить авторизацию

        email_test = wait.until(expected_conditions.element_to_be_clickable(Auth_user.EMAIL_USER))
        email_test.send_keys(email)
        password_test = wait.until(expected_conditions.element_to_be_clickable(Auth_user.PASSWORD_USER))
        password_test.send_keys("Aa12345")
        submit_test = wait.until(expected_conditions.element_to_be_clickable(Auth_user.SUBMIT_PASSWORD))
        submit_test.send_keys("Aa12345")

        create_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Buttons.CREATE_ACCOUNT))
        create_button.click()


#Проверить отображается аватар пользователя и имя User
        photo = WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(Element_check.PHOTO_USER))
        assert photo.is_displayed()

        name = WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(Element_check.NAME_USER))
        assert name.is_displayed()
        assert name.text == "User."

#Тест2.Регистрация пользователя неуспешная

    def test_failed_registration(self,generate_email):
        wait = WebDriverWait(self.driver, 60, ignored_exceptions=[StaleElementReferenceException])
        

        email = wait.until(expected_conditions.element_to_be_clickable(Auth_user.EMAIL_USER))
        email.send_keys("test.test")
        password = wait.until(expected_conditions.element_to_be_clickable(Auth_user.PASSWORD_USER))
        password.send_keys("Aa12345")
        submit = wait.until(expected_conditions.element_to_be_clickable(Auth_user.SUBMIT_PASSWORD))
        submit.send_keys("Aa12345")

        create_button = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(Buttons.CREATE_ACCOUNT))
        create_button.click()

#Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным
        error_fields = WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(Element_check.FAIL_CHECK))
        assert len(error_fields) > 0

#Проверить под полем Email отображается сообщение «Ошибка».pytest

        error = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(Element_check.ERROR_CHECK))
        assert error.is_displayed()

#Тест3.Проверить регистрацию существующего пользователя

    def test_registration_exist_user(self):
        wait = WebDriverWait(self.driver, 60, ignored_exceptions=[StaleElementReferenceException])

        email_field = wait.until(expected_conditions.element_to_be_clickable(Auth_user.EMAIL_USER))
        email_field.send_keys("user1234@ya.ru")
        password_field = wait.until(expected_conditions.element_to_be_clickable(Auth_user.PASSWORD_USER))
        password_field.send_keys("Aa12345")
        submit_field = wait.until(expected_conditions.element_to_be_clickable(Auth_user.SUBMIT_PASSWORD))
        submit_field.send_keys("Aa12345")

        create_button = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(Buttons.CREATE_ACCOUNT))
        create_button.click()


# Проверить: поля Email, «Пароль», «Повторите пароль» выделены красным
        error_fields = WebDriverWait(self.driver, 60).until(EC.presence_of_all_elements_located(Element_check.FAIL_CHECK))
        assert len(error_fields) > 0

# Проверить под полем Email отображается сообщение «Ошибка».

        error = WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(Element_check.ERROR_CHECK))
        assert error.is_displayed()

