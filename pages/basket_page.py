from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_not_products(self):
        assert self.is_not_element_present(*BasketPageLocators.TABLE_ITEMS), \
            "There are products in the basket"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), \
               "No message about empty basket"
