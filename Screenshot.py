from selenium import webdriver
# from PIL import Image
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

chrome_driver_path = "C:\\Users\\superuser\\PycharmProjects\\tindde\\tinder_bot\\chromedriver.exe"


def driver_generic():
    # run first time to get scrollHeight
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(
        executable_path=chrome_driver_path,
        options=chrome_options)
    return driver


driver_initial = driver_generic()


class ScreenshotCreator:
    def read_data(self, path):
        df = pd.read_csv(path, header=None)
        # Selecting a column or converting to a list
        return list(df[0][:])

    def create_screenshot(self, index_no, url):

        driver_initial.get(url)

        time.sleep(3)
        # get scroll Height
        height = driver_initial.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, "
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight )")
        print(height)


        # Open another headless browser with height extracted above
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument(f"--window-size=1920,{height}")
        chrome_options.add_argument("--hide-scrollbars")
        driver = webdriver.Chrome(
            executable_path=chrome_driver_path, options=chrome_options)

        driver.get(url)
        # pause 3 second to let page loads
        time.sleep(3)
        # save screenshot
        driver.save_screenshot('screenshot' + str(index_no) + '.png')
        # driver.exit()
        driver.close()
