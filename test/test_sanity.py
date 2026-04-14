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
