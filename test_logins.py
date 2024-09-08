from pages import MainPage, LoginPage, ProfilePage
import time
def test_login_logout_flow(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)

    main_page.click_enter_button()

    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

    profile_page.go_to_profile()

    assert profile_page.wait_for_profile_tab() == "Профиль"

    profile_page.click_logout_button()

    assert profile_page.wait_for_login_button() == "Войти"

    main_page.click_go_to_main_page()

    profile_page.wait_for_login_button_from_main() == "Войти в аккаунт"

    main_page.click_personal_account_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

    profile_page.go_to_profile()

    assert profile_page.wait_for_profile_tab() == "Профиль"

    profile_page.click_logout_button()

    assert profile_page.wait_for_login_button() == "Войти"

    login_page.click_register_button()
    login_page.click_enter_button_from_register()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"

    profile_page.go_to_profile()

    assert profile_page.wait_for_profile_tab() == "Профиль"

    profile_page.click_logout_button()

    assert profile_page.wait_for_login_button() == "Войти"

    login_page.click_recover_password_button()
    login_page.click_enter_button_from_register()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()

    assert main_page.wait_for_place_order_button() == "Оформить заказ"
