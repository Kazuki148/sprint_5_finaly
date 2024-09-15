from selenium.webdriver.common.by import By


class MainPageLocators:
    ENTER_BUTTON = (By.XPATH, "/html/body/div/div/main/section[2]/div/button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a[@class='AppHeader_header__link__3D_hX']")
    PLACE_ORDER_BUTTON = (By.XPATH, "/html/body/div/div/main/section[2]/div/button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    GO_TO_MAIN_PAGE = (By.XPATH, "/html/body/div/div/header/nav/div/a")
    GO_TO_TOPPING = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    CLICK_TO_CHOP = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[3]/a[2]/img[@alt='Говяжий метеорит (отбивная)']")
    CALORIES_CHOP = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/ul/li[1]/p[@class='undefined text text_type_main-default text_color_inactive']")
    CLICK_TO_CLOSE_CHOP = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    GO_TO_SAUCE = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    CLICK_TO_GALACTIC_SAUCE = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[2]/a[3]/p[@class='BurgerIngredient_ingredient__text__yp3dH']")
    PROTEIN_GALACTIC_SAUCE = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/ul/li[2]/p[@class='undefined text text_type_main-default text_color_inactive']")
    CLICK_TO_CLOSE_GALACTIC_SAUCE = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    GO_TO_BREAD = (By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']")
    CLICK_TO_CRATER_BREAD = (By.XPATH, "/html/body/div/div/main/section[1]/div[2]/ul[1]/a[@class='BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8']")
    CARBOHYDRATES_CRATER_BREAD = (By.XPATH, "/html/body/div/div/section[1]/div[1]/div/ul/li[4]/p[@class='undefined text text_type_main-default text_color_inactive']")
    CLICK_TO_CLOSE_CRATER_BREAD = (By.XPATH, "/html/body/div/div/section[1]/div[1]/button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")

class LoginPageLocators:
    NAME_INPUT = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[1]/div[1]/div[1]/input[@class='text input__textfield text_type_main-default']")
    EMAIL_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input[@class='text input__textfield text_type_main-default']")
    EMAIL_INPUT_REGISTER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[2]/div[1]/div[1]/input[@class='text input__textfield text_type_main-default']")
    PASSWORD_INPUT = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']")
    PASSWORD_INPUT_REGISTER = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/fieldset[3]/div[1]/div[1]/input[@class='text input__textfield text_type_main-default']")
    LOGIN_BUTTON = (By.XPATH, "/html/body/div/div/main/div/form/button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    REGISTER_BUTTON = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/div[1]/p[1]/a[@class='Auth_link__1fOlj']")
    REGISTER_BUTTON_AFTER_FILLING = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[1]/form[1]/button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    ERROR_MESSAGE = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/p[@class='input__error text_type_main-default']")
    GO_TO_LOGIN_BUTTON_FROM_REGISTER = (By.XPATH, "/html/body/div/div/main/div/div/p/a[@class='Auth_link__1fOlj']")
    GO_TO_RECOVER_PASSWORD_BUTTON = (By.XPATH, "/html/body/div/div/main/div/div/p[2]/a[@class='Auth_link__1fOlj']")


class ProfilePageLocators:
    PROFILE_TAB = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[1]/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9']")
    LOGOUT_BUTTON = (By.XPATH, "/html/body/div/div/main/div/nav/ul/li[3]/button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']")
    GO_TO_PROFILE_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/a/p[@class='AppHeader_header__linkText__3q_va ml-2']")
    GO_TO_CONSTRUCTOR_BUTTON = (By.XPATH, "/html/body/div/div/header/nav/ul/li[1]/a/p[@class='AppHeader_header__linkText__3q_va ml-2']")
