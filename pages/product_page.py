from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_success_message(self):
        assert self.browser.find_elements(*ProductPageLocators.SUCCESS_MESSAGE), "No message on the page"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_SUCCESS_MESSAGE).text \
               == self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, \
               "No product name in the message"

    def should_be_right_basket_sum(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text \
               == self.browser.find_element(*ProductPageLocators.BASKET_SUM).text, \
               "Price not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message isn't disappeared"

