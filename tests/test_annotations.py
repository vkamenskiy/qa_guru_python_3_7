import json
import allure
from allure import attachment_type
from allure_commons.types import Severity


def test_attachments():
    allure.attach('Text content', name='Text', attachment_type=attachment_type.TEXT)
    allure.attach('<h1>Hello, world!</h1>', name='Html', attachment_type=attachment_type.HTML)
    allure.attach(json.dumps({'first': 1, 'second': 2}), name='Json', attachment_type=attachment_type.JSON)


def test_dynamic_labels():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Неавторизованный пользователь не может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')
    pass


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'eroshenkoam')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизованный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_decorator_labels():
    pass



