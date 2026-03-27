from selenium.webdriver.common.by import By

# Кнопки

class Buttons:

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    CREATE_ACCOUNT = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_USER = (By.XPATH, "//button[text()='Войти']")
    LOGOUT_USER = (By.XPATH, "//button[text()='Выйти']")
    CREATE_AD = (By.XPATH, "//button[text()='Разместить объявление']")
    CREATE_AD_USER = (By.XPATH, "//button[text()='Опубликовать']")




#Поля ввода
class Auth_user:

    EMAIL_USER = (By.NAME, "email")
    PASSWORD_USER = (By.NAME, "password")
    SUBMIT_PASSWORD = (By.NAME, "submitPassword")
    DESCRIBE_PRODUCT = (By.CLASS_NAME, "textarea_inputStandart__IoNxq")
    PRICE_PRODUCT = (By.NAME, "price")
    CATEGORY_PRODUCT = (By.NAME, "category")
    CATEGORY_CITY = (By.NAME, "city")


#Элементы проверок
class Element_check:

    PHOTO_USER = (By.CLASS_NAME, "svgSmall")
    NAME_USER = (By.XPATH, "//h3[text()='User.']")
    FAIL_CHECK = (By.CLASS_NAME, "input_inputError__fLUP9")
    ERROR_CHECK = (By.XPATH, "//*[contains(text(), 'Ошибка')]")
    MAIN_PAGE = (By.CLASS_NAME, "homePage_homepageStyle__WP-Y1")
    AVATAR_PHOTO = (By.CLASS_NAME, "circleSmall")
    USER_NAME_CHECK = (By.XPATH, "//h3[text()='User.']")
    CHECK_AUTH = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    MY_ADVERT = (By.XPATH, "//h1[text()='Мои объявления']")
    MY_BOOKS = (By.XPATH, "//h2[text()='Куплю книги Гарри Поттера']")
    LIST = (By.CLASS_NAME, "dropDownMenu_arrowDown__pfGL1")
    TYPE_PRODUCT = (By.XPATH, "//button/span[text()='Книги']")
    DROPDOWN_LIST = (By.CLASS_NAME, "dropDownMenu_noDefault__wSKsP")
    TYPE_CITY = (By.XPATH, "//button/span[text()='Казань']")
    RADIO_BUTTON = (By.CLASS_NAME, "radioUnput_shell__Wtdwe")
    NAME_BUTTON = (By.XPATH, "//label[text()='Б/У']")



