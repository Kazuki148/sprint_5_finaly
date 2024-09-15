from pages import MainPage, LoginPage, ProfilePage

def test_topping(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    main_page.click_enter_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()
    profile_page.go_to_profile()
    profile_page.go_to_constructor()
    main_page.click_to_chop()

    assert main_page.wait_for_chop() == "Калории,ккал"

def test_sauce(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    main_page.click_enter_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()
    profile_page.go_to_profile()
    profile_page.go_to_constructor()
    main_page.click_to_galactic_sauce()

    assert main_page.wait_for_galactic_sauce() == "Белки, г"

def test_bread(driver):
    main_page = MainPage(driver)
    login_page = LoginPage(driver)
    profile_page = ProfilePage(driver)
    main_page.click_enter_button()
    login_page.enter_email("Anton_Kazakov_6@yandex.ru")
    login_page.enter_password("123456")
    login_page.click_login_button()
    profile_page.go_to_profile()
    profile_page.go_to_constructor()
    main_page.click_to_crater_bread()

    assert main_page.wait_for_crater_bread() == "Углеводы, г"
