import allure
from .base_page import BasePage
from playwright.sync_api import Page, expect

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        # Localizadores
        self.cart_link = page.locator('#cartur')
        self.place_order_button = page.locator('button:has-text("Place Order")')
        self.name_input = page.locator('#name')
        self.country_input = page.locator('#country')
        self.city_input = page.locator('#city')
        self.card_input = page.locator('#card')
        self.month_input = page.locator('#month')
        self.year_input = page.locator('#year')
        self.purchase_button = page.locator('button:has-text("Purchase")')
        self.success_message = page.locator('text=Thank you for your purchase!')
        self.ok_button = page.locator('button:has-text("OK")')

    def go_to_cart(self):
        self.cart_link.click()
        # Esperamos a que cargue la tabla del carrito
        self.page.wait_for_selector('.success')

    def open_checkout_form(self):
        self.place_order_button.click()
        self.page.wait_for_selector('#name')

    def fill_checkout_form(self, name, country, city, card, month, year):
        self.name_input.fill(name)
        self.country_input.fill(country)
        self.city_input.fill(city)
        self.card_input.fill(card)
        self.month_input.fill(month)
        self.year_input.fill(year)

    def submit_order(self):
        self.purchase_button.click()

    def verify_success_purchase(self):
        expect(self.success_message).to_be_visible()

    def close_success_modal(self):
        self.ok_button.click()