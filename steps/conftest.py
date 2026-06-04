"""
Configuración de pytest-bdd y Playwright.
Define los fixtures compartidos entre todos los steps.
Incluye captura automática de pantalla en fallos para evidencias en Allure.
"""
import allure
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser_instance():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=200)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page_context(browser_instance):
    context = browser_instance.new_context()
    page = context.new_page()
    yield page
    context.close()