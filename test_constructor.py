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

    profile_page.go_to_constructor()

    assert main_page.wait_for_topping() == "Начинки"

    main_page.click_to_chop()

    assert main_page.wait_for_chop() == "Калории,ккал"

    main_page.click_close_chop()

    assert main_page.wait_for_sauce() == "Соусы"

    main_page.click_to_galactic_sauce()

    assert main_page.wait_for_galactic_sauce() == "Белки, г"

    main_page.click_close_galactic_sauce()
    main_page.go_to_bread()
    main_page.click_to_crater_bread()

    assert main_page.wait_for_crater_bread() == "Углеводы, г"

    main_page.click_close_crater_bread()