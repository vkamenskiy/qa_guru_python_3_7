import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')

    with allure.step('Ищем mрепозиторий'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
        browser.element('.header-search-input').submit()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб Issues'):
        browser.element('#issues-tab').click()

    with allure.step('Проверяем наличие Issue с номером 76'):
        browser.element(by.partial_text('#76')).should(be.visible)
