import random
from constants import (REG_NAME_BUTTON, REG_BUTTON, REG_PASSWORD_BUTTON, REG_EMAIL_BUTTON, ENTER, INCORRECT_PASSWORD,
                       REGISTER_URL, LOGIN_URL)
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def mail_generator(domain='@ya.ru'):
    return f'goncharenko_vladislav{random.randint(100, 999)}{domain}'


def test_authorization_with_valid_credentianals(driver):
    #Заходим на страницу регистрации
    driver.get(REGISTER_URL)
    #Авторизуемся с валидными данными
    driver.find_element(*REG_NAME_BUTTON).send_keys('Name')
    driver.find_element(*REG_EMAIL_BUTTON).send_keys(mail_generator())
    driver.find_element(*REG_PASSWORD_BUTTON).send_keys('password')
    #Нажимаем кнопку "Зарегистрировать" и проверяем, что мы попали на страницу входа
    driver.find_element(*REG_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((ENTER)))
    assert driver.current_url == LOGIN_URL
    #driver.quit()


def test_authorization_with_password_less_6_symbols(driver):
    driver.get(REGISTER_URL)
    # Авторизуемся с паролем длинной менее 6 символов
    driver.find_element(*REG_NAME_BUTTON).send_keys('Name')
    driver.find_element(*REG_EMAIL_BUTTON).send_keys(mail_generator())
    driver.find_element(*REG_PASSWORD_BUTTON).send_keys('passw')
    # Нажимаем кнопку "Зарегистрироваться" и проверяем, что отобразилась ошибка
    driver.find_element(*REG_BUTTON).click()
    assert driver.find_element(*INCORRECT_PASSWORD).text == "Некорректный пароль"
    driver.quit()
