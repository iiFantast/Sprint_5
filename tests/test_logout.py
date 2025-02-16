from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import (EMAIL, PASS, AUTH_EMAIL_BUTTON, AUTH_PASS_BUTTON, AUTH_BUTTON, MAIN_URL, ENTER,
                       MODAL_PAGE, PERS_ACC_BUTTON, LOGOUT_BUTTON, LOGIN_URL, LOGIN_BUTTON)


def test_logout(driver):
    # Переходим на главную страницу
    driver.get(MAIN_URL)
    # На главной странице нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*LOGIN_BUTTON).click()
    # Проверяем переход на страницу входа в аккаунт
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located(ENTER))
    # Заполняем поля email и пароль и нажимаем кнопку "Войти"
    driver.find_element(*AUTH_EMAIL_BUTTON).send_keys(EMAIL)
    driver.find_element(*AUTH_PASS_BUTTON).send_keys(PASS)
    driver.find_element(*AUTH_BUTTON).click()
    #Задаем ожидание, пока не пропадет модалка и кнопка не станет кликабельной
    WebDriverWait(driver, 3).until(expected_conditions.invisibility_of_element_located(MODAL_PAGE))
    #Нажимаем на кнопку "Личный кабинет"
    driver.find_element(*PERS_ACC_BUTTON).click()
    #Нажимаем на кнопку "Выход"
    WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON)).click()
    #Задаем ожидание, пока не убедимся, что попали на страницу логина
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(ENTER))
    assert driver.current_url == LOGIN_URL
    driver.quit()
