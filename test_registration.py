from pages import MainPage, LoginPage
import random

def test_registration(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)

    email = random.randint(20, 90)
    password = random.randint(10000, 99999)

    main_page.click_enter_button()
    login_page.click_register_button()
    login_page.enter_username_registration("Anton")
    login_page.enter_email_registration(f'Anton_Kazakov_{email}@yandex.ru')
    login_page.enter_password_registration(password)
    login_page.click_register_button_after_filling()

    assert "Некорректный пароль" == main_page.wait_for_error()

    login_page.enter_password_registration("6")
    login_page.click_register_button_after_filling()
