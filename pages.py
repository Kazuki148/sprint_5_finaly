from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_enter_button(self):
        self.driver.find_element(*MainPageLocators.ENTER_BUTTON).click()

    def click_personal_account_button(self):
        self.driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

    def wait_for_place_order_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.PLACE_ORDER_BUTTON))
        return self.driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).text

    def wait_for_error(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.ERROR_MESSAGE))
        return self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE).text

    def wait_for_topping(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.GO_TO_TOPPING))
        return self.driver.find_element(*MainPageLocators.GO_TO_TOPPING).text

    def wait_for_sauce(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.GO_TO_SAUCE))
        return self.driver.find_element(*MainPageLocators.GO_TO_SAUCE).text

    def click_to_chop(self):
        self.driver.find_element(*MainPageLocators.CLICK_TO_CHOP).click()

    def wait_for_chop(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CALORIES_CHOP))
        return self.driver.find_element(*MainPageLocators.CALORIES_CHOP).text

    def click_close_chop(self):
        self.driver.find_element(*MainPageLocators.CLICK_TO_CLOSE_CHOP).click()

    def click_to_galactic_sauce(self):
        self.driver.find_element(*MainPageLocators.CLICK_TO_GALACTIC_SAUCE).click()

    def wait_for_galactic_sauce(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.PROTEIN_GALACTIC_SAUCE))
        return self.driver.find_element(*MainPageLocators.PROTEIN_GALACTIC_SAUCE).text

    def click_close_galactic_sauce(self):
        self.driver.find_element(*MainPageLocators.CLICK_TO_CLOSE_GALACTIC_SAUCE).click()

    def go_to_bread(self):
        self.driver.find_element(*MainPageLocators.GO_TO_BREAD).click()

    def click_to_crater_bread(self):
        self.driver.find_element(*MainPageLocators.CLICK_TO_CRATER_BREAD).click()
    def wait_for_crater_bread(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.CARBOHYDRATES_CRATER_BREAD))
        return self.driver.find_element(*MainPageLocators.CARBOHYDRATES_CRATER_BREAD).text

    def click_close_crater_bread(self):
        self.driver.find_element(*MainPageLocators.CLICK_TO_CLOSE_CRATER_BREAD).click()

    def click_go_to_main_page(self):
        self.driver.find_element(*MainPageLocators.GO_TO_MAIN_PAGE).click()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def enter_password_registration(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT_REGISTER).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def click_register_button(self):
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

    def enter_email_registration(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT_REGISTER).send_keys(email)

    def click_register_button_after_filling(self):
        self.driver.find_element(*LoginPageLocators.REGISTER_BUTTON_AFTER_FILLING).click()

    def enter_username_registration(self, name):
        self.driver.find_element(*LoginPageLocators.NAME_INPUT).send_keys(name)

    def click_enter_button_from_register(self):
        self.driver.find_element(*LoginPageLocators.GO_TO_LOGIN_BUTTON_FROM_REGISTER).click()

    def click_recover_password_button(self):
        self.driver.find_element(*LoginPageLocators.GO_TO_RECOVER_PASSWORD_BUTTON).click()

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_profile_tab(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(ProfilePageLocators.PROFILE_TAB))
        return self.driver.find_element(*ProfilePageLocators.PROFILE_TAB).text

    def click_logout_button(self):
        self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()

    def wait_for_login_button(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        return self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).text

    def wait_for_login_button_from_main(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(MainPageLocators.ENTER_BUTTON))
        return self.driver.find_element(*MainPageLocators.ENTER_BUTTON).text

    def go_to_profile(self):
        self.driver.find_element(*ProfilePageLocators.GO_TO_PROFILE_BUTTON).click()

    def go_to_constructor(self):
        self.driver.find_element(*ProfilePageLocators.GO_TO_CONSTRUCTOR_BUTTON).click()
