from selenium import webdriver
import pytest

import json
import os.path


def load_config(file_path):
    config_path = os.path.join(os.path.dirname
                               (os.path.abspath(__file__)), file_path)
    with open(config_path) as f:
        target = json.load(f)
    return target


def api_user_config_data():
    config_data = load_config("recourses/variables/user_api_data.json")
    return config_data['user_name'], \
           config_data['password'], config_data['new_user_name']


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def parameter_change():
    config_data = load_config("recourses/variables/parameter.json")
    return config_data['temperature,C'], \
           config_data['weight,oz'], config_data['length,m']
