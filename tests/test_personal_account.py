from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import (PASS, EMAIL, AUTH_PASS_BUTTON, AUTH_BUTTON, AUTH_EMAIL_BUTTON, MODAL_PAGE, ENTER_ACC_BUTTON,
                       ENTER, PERS_ACC_BUTTON, MAIN_URL, PERS_ACC_URL)


def test_redirect_on_personal_acc_auth_person(driver):
    # Переходим на главную страницу
    driver.get(MAIN_URL)
    # На главной странице нажимаем на кнопку "Войти в аккаунт"
    driver.find_element(*ENTER_ACC_BUTTON).click()
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
    #Проверяем, что мы перешли в личный кабинет
    assert WebDriverWait(driver, 3).until(expected_conditions.url_to_be(PERS_ACC_URL))

