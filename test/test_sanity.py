import pytest

from pages.joom_abstract import JoomAbstract


class TestSanity:
    @pytest.mark.navigate_shopping_cart
    def test_navigate_shopping_cart(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_shopping_cart()
        assert main_page.get_toolbar_title() == "My cart", "Toolbar title should be: My cart"

    @pytest.mark.navigate_shopping_cart_and_return_back
    def test_navigate_shopping_cart_and_return_back(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_shopping_cart()
        main_page.click_back_button()
        assert main_page.is_search_bar_displayed() is True, "Search bar should be displayed"

    @pytest.mark.navigate_favourites
    def test_navigate_favourites(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_favourites()
        assert main_page.get_toolbar_title() == "Favourites", "Toolbar title should be: Favourites"

    @pytest.mark.navigate_favourites_and_return_back
    def test_navigate_favourites_and_return_back(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_favourites()
        main_page.click_back_button()
        assert main_page.is_search_bar_displayed() is True, "Search bar should be displayed"

    @pytest.mark.navigate_search
    def test_navigate_search(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_search_menu()
        assert main_page.is_search_bar_displayed() is True, "Search bar should be displayed"

    @pytest.mark.navigate_profile
    def test_navigate_profile(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_profile_menu()
        assert main_page.get_profile_header_name() == "Log in", "The default profile name: Log in"

    @pytest.mark.navigate_my_orders
    def test_navigate_my_orders(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_profile_menu()
        main_page.click_my_orders()
        assert main_page.get_toolbar_title() == "My orders", "Toolbar title should be: My orders"
        main_page.click_back_button()
        assert main_page.get_profile_header_name() == "Log in", "The default profile name: Log in"

    @pytest.mark.navigate_refunds
    def test_navigate_refunds(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_profile_menu()
        main_page.click_refunds()
        assert main_page.get_toolbar_title() == "My orders", "Toolbar title should be: My orders"
        main_page.click_back_button()
        assert main_page.get_profile_header_name() == "Log in", "The default profile name: Log in"

    @pytest.mark.navigate_favourites_from_profile
    def test_navigate_favourites_from_profile(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_profile_menu()
        main_page.click_favorites()
        assert main_page.get_toolbar_title() == "Favourites", "Toolbar title should be: Favourites"
        main_page.click_back_button()
        assert main_page.get_profile_header_name() == "Log in", "The default profile name: Log in"

    @pytest.mark.navigate_notifications
    def test_navigate_notifications(self, main_page: JoomAbstract):
        main_page.driver.start_recording_screen()
        main_page.close_initial_dialog()
        main_page.close_wheel_of_fortune_dialog()
        main_page.click_profile_menu()
        main_page.click_notifications()
        assert main_page.get_toolbar_title() == "Notifications", (
            "Toolbar title should be: Notifications"
        )
        main_page.click_back_button()
        assert main_page.get_profile_header_name() == "Log in", "The default profile name: Log in"
