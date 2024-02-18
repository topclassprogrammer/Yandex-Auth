import time

from environs import Env
from selenium.webdriver.common.by import By
from seleniumwire import webdriver


env = Env()
env.read_env()
URL = env('URL')
LOGIN = env('LOGIN')
PASSWORD = env('PASSWORD')
driver = webdriver.Chrome()
driver.get(URL)


def build_xpath(tag, attr, attr_value):
    return f'//{tag}[@{attr}="{attr_value}"]'


def click_on(tag, attr, attr_value):
    xpath_value = build_xpath(tag, attr, attr_value)
    element = driver.find_element(by=By.XPATH, value=xpath_value)
    element.click()
    return True


def input_in(tag, attr, attr_value, text):
    xpath_value = build_xpath(tag, attr, attr_value)
    element = driver.find_element(by=By.XPATH, value=xpath_value)
    element.send_keys(text)
    return True


if __name__ == '__main__':
    click_on('button', 'data-type', 'login')
    input_in('input', 'id', 'passp-field-login', LOGIN)
    click_on('button', 'id', 'passp:sign-in')
    time.sleep(1)
    input_in('input', 'id', 'passp-field-passwd', PASSWORD)
    click_on('button', 'id', 'passp:sign-in')
    time.sleep(5)
    driver.close()
