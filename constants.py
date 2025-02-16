from selenium.webdriver.common.by import By

#Данные для авторизации
EMAIL = "name12@ya.ru"
PASS = "123456"

#URL приложения
MAIN_URL = "https://stellarburgers.nomoreparties.site/"  #Урл главной страницы
REGISTER_URL = 'https://stellarburgers.nomoreparties.site/register'  #Урл страницы регистрации
LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"  #Урл страницы логина
RESTORE_PASS_URL = "https://stellarburgers.nomoreparties.site/forgot-password"  #Урл страницы восстановления пароля
PERS_ACC_URL = "https://stellarburgers.nomoreparties.site/account/profile"

#Локаторы для страницы регистрации
REG_NAME_BUTTON = (By.XPATH, ".//fieldset[1]/div/div/input[@name='name']")  #Поле для ввода имени
REG_EMAIL_BUTTON = (By.XPATH, ".//fieldset[2]/div/div/input[@name='name']")  #Поле для ввода email
REG_PASSWORD_BUTTON = (By.NAME, 'Пароль')  # поле для ввода пароля
REG_BUTTON = (By.XPATH, ".//form/button[text()='Зарегистрироваться']")  #Кнопка "Зарегистрироваться"
ENTER = (By.XPATH, ".//h2[text()='Вход']")  # Надпись "Вход" на странице логина
INCORRECT_PASSWORD = (By.CSS_SELECTOR, ".input__error")  #Ошибка "Некорректный пароль"

#Локаторы кнопок авторизации
AUTH_EMAIL_BUTTON = (By.XPATH, ".//fieldset[1]/div/div/input[@name='name']")  #поле для ввода email
AUTH_PASS_BUTTON = (By.NAME, 'Пароль')  #Поле для ввода пароля
AUTH_BUTTON = (By.XPATH, ".//form/button[text()='Войти']")  #кнопка "Войти"
PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  #кнопка "Оформить заказ"
ENTER_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj")  #Кнопка "Войти" на странице Регистрации
PERS_ACC_BUTTON = (By.XPATH, ".//nav/a/p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
ENTER_ACC_BUTTON = (By.XPATH, ".//section[2]/div/button[text()='Войти в аккаунт']")  #Кнопка "Войти в аккаунт"

#Локаторы личного кабинета
MODAL_PAGE = (
By.XPATH, "/html/body/div/div/div/div[@class='Modal_modal_overlay__x2ZCr']")  #Модальное окно после авторизации
LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button[text()='Выход']")  #Кнопка "Выход" в ЛК
LOGIN_BUTTON = (By.XPATH, ".//section[2]/div/button[text()='Войти в аккаунт']")  #Кнопка "Войти в аккаунт"
CONSTRUCTOR_BUTTON = (By.XPATH, ".//a/p[text()='Конструктор']")
BURGER_LOGO = (By.CLASS_NAME, 'AppHeader_header__logo__2D0X2')

#Локаторы на главной странице
SAUCE_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[2]/span[text()='Соусы']")  #Кнопка "Соусы"
BUN_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[1]/span[text()='Булки']")  # Кнопка "Булки"
FILLING_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[3]/span[text()='Начинки']")  # Кнопка "Начинки"
SAUCE_TITLE = (By.XPATH, ".//section[1]/div[2]/h2[2][text()='Соусы']")  # Заголовок "Соусы"
BUN_TITLE = (By.XPATH, ".//section[1]/div[2]/h2[1][text()='Булки']")  # Заголовок "Булки"
FILLING_TITLE = (By.XPATH, ".//section[1]/div[2]/h2[3][text()='Начинки']")  # Заголовок "Начинки"
LAST_ELEMENT = (
    By.XPATH,
    ".//section[1]/div[2]/ul[3]/a[9]/p[text()='Сыр с астероидной плесенью']")  # Последний элемент в конструкторе
