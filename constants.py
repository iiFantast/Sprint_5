from selenium.webdriver.common.by import By

#Данные для авторизации
EMAIL = "name12@ya.ru"
PASS = "123456"

#Локаторы для страницы регистрации
REG_NAME_BUTTON = (By.XPATH, ".//fieldset[1]/div/div/input[@name='name']")  #Поле для ввода имени
REG_EMAIL_BUTTON = (By.XPATH, ".//fieldset[2]/div/div/input")  #Поле для ввода email
REG_PASSWORD_BUTTON = (By.NAME, 'Пароль')  # поле для ввода пароля
REG_BUTTON = (By.XPATH, ".//form/button")  #Кнопка "Зарегистрироваться"
ENTER = (By.XPATH, ".//h2[text()='Вход']")  # Надпись "Вход" на странице логина
INCORRECT_PASSWORD = (By.CSS_SELECTOR, ".input__error") #Ошибка "Некорректный пароль"
REGISTER_URL = 'https://stellarburgers.nomoreparties.site/register' #Урл страницы регистрации
LOGIN_URL = "https://stellarburgers.nomoreparties.site/login" #Урл страницы логина

#Локаторы кнопок авторизации
AUTH_EMAIL_BUTTON = (By.XPATH, ".//fieldset[1]/div/div/input") #поле для ввода email
AUTH_PASS_BUTTON = (By.XPATH, ".//fieldset[2]/div/div/input") #Поле для ввода пароля
AUTH_BUTTON = (By.XPATH, ".//form/button") #кнопка "Войти"
MAIN_URL = "https://stellarburgers.nomoreparties.site/" #Урл главной страницы
RESTORE_PASS_URL = "https://stellarburgers.nomoreparties.site/forgot-password" #Урл страницы восстановления пароля
PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']") #кнопка "Оформить заказ"
ENTER_BUTTON = (By.XPATH, ".//p/a[@class='Auth_link__1fOlj']") #Кнопка "Войти" на странице Регистрации
PERS_ACC_BUTTON = (By.XPATH, ".//nav/a/p")# Кнопка "Личный кабинет"
ENTER_ACC_BUTTON = (By.XPATH, ".//section[2]/div/button") #Кнопка "Войти в аккаунт"

#Локаторы личного кабинета
MODAL_PAGE = (By.XPATH, "/html/body/div/div/div/div") #Модальное окно после авторизации
LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button") #Кнопка "Выход" в ЛК
LOGIN_BUTTON = (By.XPATH, ".//section[2]/div/button[text()='Войти в аккаунт']") #Кнопка "Войти в аккаунт"
PERS_ACC_URL = "https://stellarburgers.nomoreparties.site/account/profile"
CONSTRUCTOR_BUTTON = (By.XPATH, ".//a/p[text()='Конструктор']")
BURGER_LOGO = (By.XPATH, "/html/body/div/div/header/nav/div/a")

#Локаторы на главной странице
SAUCE_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[2]/span[text()='Соусы']") #Кнопка "Соусы"
BUN_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[1]/span[text()='Булки']") # Кнопка "Булки"
FILLING_BUTTON = (By.XPATH, ".//section[1]/div[1]/div[3]/span[text()='Начинки']") # Кнопка "Начинки"
SAUCE_TITLE = (By.XPATH, ".//section[1]/div[2]/h2[2][text()='Соусы']") # Заголовок "Соусы"
BUN_TITLE = (By.XPATH, ".//section[1]/div[2]/h2[1][text()='Булки']") # Заголовок "Булки"
FILLING_TITLE = (By.XPATH, ".//section[1]/div[2]/h2[3][text()='Начинки']") # Заголовок "Начинки"
LAST_ELEMENT = (By.XPATH, ".//section[1]/div[2]/ul[3]/a[9]/p[text()='Сыр с астероидной плесенью']") # Последний элемент в конструкторе
