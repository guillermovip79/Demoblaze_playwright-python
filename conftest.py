"""
Configuración de pytest-bdd y Playwright.
Define los fixtures compartidos entre todos los steps.
Incluye captura automática de pantalla en fallos para evidencias en Allure.
"""
import allure
import pytest
from playwright.sync_api import sync_playwright
from pages.home_page import HomePage
from pages.cart_page import CartPage

# Clase contenedora para organizar tus Page Objects limpiamente
class TestContext:
    def __init__(self, page):
        self.page = page
        self.home_page = HomePage(page)
        self.cart_page = CartPage(page)

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, slow_mo=100) # Headless=True recomendado para Jenkins
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page_context(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    
    # Entregamos el contenedor con las páginas ya instanciadas internamente
    test_context = TestContext(page)
    yield test_context
    
    context.close()