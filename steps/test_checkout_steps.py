"""
Step definitions para la feature: Agregar artículo al carrito.
Usa pytest-bdd para mapear los pasos Gherkin a código Python.
Incluye decoradores Allure para enriquecer el reporte.
"""
import allure
import pytest
from pytest_bdd import scenarios, given, when, then
from pages.home_page import HomePage
from pages.cart_page import CartPage

# Vinculación directa con el archivo de la feature
scenarios('../features/checkout.feature')

@allure.feature("Flujo de Checkout de DemoBlaze")
@allure.story("Comprar como invitado de forma exitosa")
@allure.severity(allure.severity_level.CRITICAL)
@given('que el usuario navega a la página de inicio de Demoblaze')
def navegar_a_inicio(page_context):
    with allure.step("Abrir el sitio web de DemoBlaze"):
        page_context.home_page = HomePage(page_context)
        page_context.cart_page = CartPage(page_context)
        page_context.home_page.navigate()
        page_context.home_page.take_screenshot("Página de inicio cargada")

@when('selecciona el primer producto de la lista')
def seleccionar_producto(page_context):
    with allure.step("Seleccionar el primer producto de las tarjetas"):
        page_context.home_page.select_first_product()
        page_context.home_page.take_screenshot("Detalle del producto visible")

@when('agrega el producto al carrito aceptando la alerta de confirmación')
def agregar_al_carrito(page_context):
    with allure.step("Hacer clic en 'Add to cart' y gestionar alerta"):
        page_context.home_page.add_product_to_cart()

@when('se dirige al carrito de compras')
def ir_al_carrito(page_context):
    with allure.step("Acceder a la sección del carrito"):
        page_context.cart_page.go_to_cart()
        page_context.cart_page.take_screenshot("Contenido de la tabla del carrito")

@when('procede a realizar el pedido completando el formulario de compra')
def completar_formulario(page_context):
    with allure.step("Abrir pasarela y rellenar campos de compra"):
        page_context.cart_page.open_checkout_form()
        
        allure.attach(
            "Nombre: Guillermo Viniegra\nPaís: Mexico\nCiudad: CDMX",
            name="Datos del Comprador",
            attachment_type=allure.attachment_type.TEXT
        )
        
        page_context.cart_page.fill_checkout_form(
            name="Guillermo Viniegra",
            country="Mexico",
            city="CDMX",
            card="1234567890123456",
            month="12",
            year="2028"
        )
        page_context.cart_page.take_screenshot("Formulario completado")
        page_context.cart_page.submit_order()

@then('la orden se procesa y se muestra el mensaje "Thank you for your purchase!"')
def verificar_compra(page_context):
    with allure.step("Validar mensaje de éxito en el modal"):
        page_context.cart_page.verify_success_purchase()
        page_context.cart_page.take_screenshot("Orden completada con éxito")
        page_context.cart_page.close_success_modal()