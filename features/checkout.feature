Feature: Flujo de compra en la tienda DemoBlaze

  Scenario: Comprar un producto exitosamente como usuario invitado
    Given que el usuario navega a la página de inicio de Demoblaze
    When selecciona el primer producto de la lista
    And agrega el producto al carrito aceptando la alerta de confirmación
    And se dirige al carrito de compras
    And procede a realizar el pedido completando el formulario de compra
    Then la orden se procesa y se muestra el mensaje "Thank you for your purchase!"