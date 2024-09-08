from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTER_BUTTON = (By.XPATH, "/html/body/div/div/main/section[2]/div/button")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a")
    PLACE_ORDER_BUTTON = (By.XPATH, "/html/body/div/div/main/section[2]/div/button")
    GO_TO_MAIN_PAGE = (By.XPATH, "/html/body/div/div/header/nav/div/a")
    GO_TO_TOPPING = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]")
    CLICK_TO_CHOP = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[3]/a[2]/img")
    CALORIES_CHOP = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/ul/li[1]/p[1]")
    CLICK_TO_CLOSE_CHOP = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button")
    GO_TO_SAUCE = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]")
    CLICK_TO_GALACTIC_SAUCE = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]/a[3]/p")
    PROTEIN_GALACTIC_SAUCE = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/ul/li[2]/p[1]")
    CLICK_TO_CLOSE_GALACTIC_SAUCE = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button")
    GO_TO_BREAD = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]")
    CLICK_TO_CRATER_BREAD = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[2]")
    CARBOHYDRATES_CRATER_BREAD = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/ul/li[4]/p[1]")
    CLICK_TO_CLOSE_CRATER_BREAD = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button")

class LoginPageLocators:
    NAME_INPUT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[1]")
    EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")
    EMAIL_INPUT_REGISTER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[1]")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input")
    PASSWORD_INPUT_REGISTER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[1]")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button")
    REGISTER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[1]")
    REGISTER_BUTTON_AFTER_FILLING = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[1]")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p")
    GO_TO_LOGIN_BUTTON_FROM_REGISTER = (By.XPATH, "/html/body/div/div/main/div/div/p/a")
    GO_TO_RECOVER_PASSWORD_BUTTON = (By.XPATH, "/html/body/div/div/main/div/div/p[2]/a")


class ProfilePageLocators:
    PROFILE_TAB = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]/a")
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button")
    GO_TO_PROFILE_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a/p")
    GO_TO_CONSTRUCTOR_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p")
