import random
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    yield driver

    driver.quit()

@pytest.fixture
def generate_email():

    return f"user{random.randint(1000, 9999)}@test.ru"

