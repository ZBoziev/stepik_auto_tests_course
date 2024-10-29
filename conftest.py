import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language for browser: en, es, fr, etc.")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
