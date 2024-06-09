from tarjetacredito import TarjetaCredito

tarjeta1 = TarjetaCredito(0, 1000, 0.02)
tarjeta2 = TarjetaCredito(0, 1000, 0.02)
tarjeta3 = TarjetaCredito(0, 1000, 0.02)

print(tarjeta1.compra(500),tarjeta1.compra(200),tarjeta1.pago(100))
tarjeta1.cobrar_interes()
tarjeta1.mostrar_info_tarjeta()

print(tarjeta2.compra(300),tarjeta2.compra(300),tarjeta2.compra(200), tarjeta2.pago(100), tarjeta2.pago(100))
tarjeta2.cobrar_interes()
tarjeta2.mostrar_info_tarjeta()

print(tarjeta3.compra(300),tarjeta3.compra(300),tarjeta3.compra(200),tarjeta3.compra(100),tarjeta3.compra(100))
tarjeta3.mostrar_info_tarjeta()
