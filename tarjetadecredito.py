class TarjetaCredito:

   lista_tarjetas = []

   def __init__(self, saldo_pagar, limite_credito, intereses):

       self.saldo_pagar = saldo_pagar
       self.limite_credito = limite_credito
       self.intereses = intereses
       TarjetaCredito.lista_tarjetas.append(self)

   def compra(self, monto):
       if self.limite_credito > (self.saldo_pagar + monto):
           self.saldo_pagar += monto
           print(f"¡Realizaste una compra! Monto facturado: ${self.saldo_pagar} pesos.")
       else:
           print(f"Tarjeta Rechazada, has alcanzado tu límite de crédito.")

   def pago(self, monto):
        self.saldo_pagar -= monto
        print(f"Abonaste ${monto} y el nuevo monto a pagar es de ${self.saldo_pagar} pesos.")
   
   def mostrar_info_tarjeta(self):
       print(f"Saldo a Pagar: ${self.saldo_pagar} pesos.")

   def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        print(f"Se adicionó: ${self.intereses} pesos en intereses, el nuevo monto a pagar es de: ${self.saldo_pagar}")
