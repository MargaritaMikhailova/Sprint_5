import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import TestData


class TestLoginUser:

# Выполнить авторизацию
    def test_login_user(self,driver):
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable(Buttons.LOGIN_BUTTON)).click()

        email = wait.until(expected_conditions.element_to_be_clickable(Auth_user.EMAIL_USER))
        email.send_keys(TestData.USER_2)
        password = wait.until(expected_conditions.element_to_be_clickable(Auth_user.PASSWORD_USER))
        password.send_keys(TestData.VALID_PASS)

        driver.find_element(*Buttons.LOGIN_USER).click()


#Проверить произошёл переход на главную страницу и отображается аватар пользователя и имя User.
        main_page = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))
        assert main_page.is_displayed()

        card_of_announcement = driver.find_element(*Buttons.CREATE_AD)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of(card_of_announcement))
        assert card_of_announcement.is_displayed()

        photo = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.AVATAR_PHOTO))
        assert photo.is_displayed()

        name = driver.find_element(*Element_check.USER_NAME_CHECK)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.USER_NAME_CHECK))
        assert name.is_displayed()
        assert name.text == "User."


