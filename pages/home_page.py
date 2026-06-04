from pages.base_page import BasePage
from playwright.sync_api import Page

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        # Localizadores específicos
        self.first_product = page.locator('.card-title a').first
        self.add_to_cart_button = page.locator('text=Add to cart')

    def navigate(self):
        self.open_url('https://demoblaze.com')

    def select_first_product(self):
        self.click_element(self.first_product)

    def add_product_to_cart(self):
        # Configuramos el escuchador de la alerta antes del clic detonador
        self.page.on("dialog", lambda dialog: self._handle_dialog(dialog))
        self.click_element(self.add_to_cart_button)
        self.page.wait_for_timeout(1000)

    def _handle_dialog(self, dialog):
        assert "Product added" in dialog.message
        dialog.accept()