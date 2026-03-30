import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from data import TestData


class TestLogoutUser:

# Выполнить авторизацию
    def test_user_login(self,driver):
        wait = WebDriverWait(driver, 20)

        login_user = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Buttons.LOGIN_BUTTON)).click()

        email = wait.until(expected_conditions.element_to_be_clickable(Auth_user.EMAIL_USER))
        email.send_keys(TestData.USER_2)
        password = wait.until(expected_conditions.element_to_be_clickable(Auth_user.PASSWORD_USER))
        password.send_keys(TestData.VALID_PASS)

        driver.find_element(*Buttons.LOGIN_USER).click()

#Проверить произошёл переход на главную страницу и отображается аватар пользователя и имя User.
        page_main = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))

        card_of_announcement = driver.find_element(*Buttons.CREATE_AD)
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of(card_of_announcement))

        photo = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.AVATAR_PHOTO))
        assert photo.is_displayed()

        name = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.USER_NAME_CHECK))
        assert name.is_displayed()
        assert name.text == "User."

#Выйти из приложения
        driver.find_element(*Buttons.LOGOUT_USER).click()

#Проверить, что аватар и User больше не отображаются
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Element_check.MAIN_PAGE))

        card_of_announcement = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Buttons.CREATE_AD))
        assert card_of_announcement.is_displayed()

        photo_user = WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located(Element_check.AVATAR_PHOTO))
        assert photo_user is True

        name_user = driver.find_elements(*Element_check.USER_NAME_CHECK)
        assert len(name_user) == 0

