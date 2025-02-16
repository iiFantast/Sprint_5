from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import (EMAIL, PASS, AUTH_EMAIL_BUTTON, AUTH_PASS_BUTTON, AUTH_BUTTON, MAIN_URL, REGISTER_URL,
                       RESTORE_PASS_URL, PLACE_ORDER, ENTER, ENTER_BUTTON, PERS_ACC_BUTTON, ENTER_ACC_BUTTON)


def test_login_from_main_page(driver):
    #Переходим на главную страницу
    driver.get(MAIN_URL)
    #На главной странице нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*ENTER_ACC_BUTTON).click()
    #Проверяем переход на страницу входа в аккаунт
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((ENTER)))
    #Заполняем поля email и пароль и нажимаем кнопку "Войти"
    driver.find_element(*AUTH_EMAIL_BUTTON).send_keys(EMAIL)
    driver.find_element(*AUTH_PASS_BUTTON).send_keys(PASS)
    driver.find_element(*AUTH_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PLACE_ORDER))
    assert driver.find_element(*PLACE_ORDER).text == "Оформить заказ"

def test_login_from_personal_account_button(driver):
    # Переходим на главную страницу
    driver.get(MAIN_URL)
    # На главной странице нажимаем на кнопку "Личный кабинет"
    driver.find_element(*PERS_ACC_BUTTON).click()
    # Проверяем переход на страницу входа в аккаунт
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((ENTER)))
    # Заполняем поля email и пароль и нажимаем кнопку "Войти"
    driver.find_element(*AUTH_EMAIL_BUTTON).send_keys(EMAIL)
    driver.find_element(*AUTH_PASS_BUTTON).send_keys(PASS)
    driver.find_element(*AUTH_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PLACE_ORDER))
    assert driver.find_element(*PLACE_ORDER).text == "Оформить заказ"


def test_login_from_registration_button(driver):
    #Переходим на страницу регистрации
    driver.get(REGISTER_URL)
    #Нажимаем на кнопку "Войти"
    driver.find_element(*ENTER_BUTTON).click()
    # Проверяем переход на страницу входа в аккаунт
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((ENTER)))
    # Заполняем поля email и пароль и нажимаем кнопку "Войти"
    driver.find_element(*AUTH_EMAIL_BUTTON).send_keys(EMAIL)
    driver.find_element(*AUTH_PASS_BUTTON).send_keys(PASS)
    driver.find_element(*AUTH_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PLACE_ORDER))
    assert driver.find_element(*PLACE_ORDER).text == "Оформить заказ"


def test_login_from_restore_password_form(driver):
    # Переходим на страницу восстановления пароля
    driver.get(RESTORE_PASS_URL)
    # Нажимаем на кнопку "Войти"
    driver.find_element(*ENTER_BUTTON).click()
    # Проверяем переход на страницу входа в аккаунт
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((ENTER)))
    # Заполняем поля email и пароль и нажимаем кнопку "Войти"
    driver.find_element(*AUTH_EMAIL_BUTTON).send_keys(EMAIL)
    driver.find_element(*AUTH_PASS_BUTTON).send_keys(PASS)
    driver.find_element(*AUTH_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(PLACE_ORDER))
    assert driver.find_element(*PLACE_ORDER).text == "Оформить заказ"
