from pages import MainPage, LoginPage, ProfilePage

def test_login_enter_button(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.click_enter_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

def test_profile(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    main_page.click_enter_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    profile_page.go_to_profile()

    assert profile_page.wait_for_profile_tab() == "Профиль"

def test_login_personal_account_button(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.click_personal_account_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

def test_login_from_register_button(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    main_page.click_enter_button()
    login_page.click_register_button()
    login_page.click_enter_button_from_register()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

def test_login_from_recover_password(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    profile_page.go_to_profile()
    login_page.click_recover_password_button()
    login_page.click_enter_button_from_register()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

def test_logout(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    main_page.click_enter_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()
    main_page.click_go_to_main_page()
    profile_page.go_to_profile()
    profile_page.wait_for_profile_tab() == "Профиль"
    profile_page.click_logout_button()

    assert profile_page.wait_for_login_button() == "Войти"
