from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import (LOGIN_BUTTON, MAIN_URL, FILLING_BUTTON, FILLING_TITLE,
                       SAUCE_BUTTON, SAUCE_TITLE, LAST_ELEMENT, BUN_BUTTON, BUN_TITLE)


def test_click_on_fillings(driver):
    #Переходим на главную страницу
    driver.get(MAIN_URL)
    #Ожидаем, пока страница не загрузится
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON))
    #Нажимаем на кнопку "Начинки"
    driver.find_element(*FILLING_BUTTON).click()
    filling_element = WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(FILLING_TITLE))
    #Проверяем, что отображается заголовок "начинки" отображается в видимой части
    assert filling_element.is_displayed()
    driver.quit()


def test_click_on_sauce(driver):
    #Переходим на главную страницу
    driver.get(MAIN_URL)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON))
    #Нажимаем на кнопку "Соусы"
    driver.find_element(*SAUCE_BUTTON).click()
    sauce_element = WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(SAUCE_TITLE))
    # Проверяем, что отображается заголовок "Соусы" отображается в видимой части
    assert sauce_element.is_displayed()
    driver.quit()


def test_click_on_buns(driver):
    #Переходим на главную страницу
    driver.get(MAIN_URL)
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON))
    #Делаем скролл до самого нижнего элемента в разделе, чтобы кнопка "Булки" стала кликабельной
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*LAST_ELEMENT))
    driver.find_element(*BUN_BUTTON).click()
    bun_element = WebDriverWait(driver, 3).until(
        expected_conditions.presence_of_element_located(BUN_TITLE))
    #Проверяем, что отображается заголовок "Булки" отображается в видимой части
    assert bun_element.is_displayed()
    driver.quit()
