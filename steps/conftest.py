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

# Clase contenedora profesional para organizar tus Page Objects
class TestContext:
    def __init__(self, page):
        self.page = page
        self.home_page = HomePage(page)
        self.cart_page = CartPage(page)

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        # Se cambia headless a True para que corra perfectamente en servidores Jenkins sin interfaz gráfica
        browser = playwright.chromium.launch(headless=True, slow_mo=100)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page_context(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    
    # Entregamos el contenedor estructurado con las páginas listas para usar
    test_context = TestContext(page)
    yield test_context
    
    context.close()