from sensitive_data import SensitiveData


class TestData:
    VALID_USERNAME = SensitiveData.VALID_USERNAME
    INVALID_USERNAME = "a@a.com"
    VALID_PASSWORD = SensitiveData.VALID_PASSWORD
    BASE_URL = "https://career-control.com/"
    CHROME_DRIVER_LOCATION = "../drivers/chromedriver.exe"
    LOGIN_ERROR_MESSAGE = "Invalid username or password."
    COMPANY_NAME = "KokoSoft"

