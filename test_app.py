from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
import pytest

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    options.headless = True
    
    driver = webdriver.Remote(
        command_executor=f"http://localhost:5555/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
        options=options,
    )

    yield driver
    driver.quit()


def test_bold(browser):
    try:        
        browser.get('http://web:5000')
        browser.find_element_by_tag_name("b")
    except Exception as e:
        print(e)
    finally:
        browser.close()
