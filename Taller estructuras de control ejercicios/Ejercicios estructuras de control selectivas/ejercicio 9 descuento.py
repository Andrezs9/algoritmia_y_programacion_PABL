# Entradas
nombre_cliente = input("Ingrese el nombre del cliente: ")
monto_compra = float(input("Ingrese el monto de la compra en COP: "))

# caja negra
descuento = 0.0

if monto_compra < 50000:
    descuento = 0.0
elif monto_compra <= 100000:
    descuento = 0.05
elif monto_compra <= 700000:
    descuento = 0.11
elif monto_compra <= 1500000:
    descuento = 0.18
else:
    descuento = 0.25

monto_descuento = monto_compra * descuento
monto_a_pagar = monto_compra - monto_descuento

# salida
print(f"Nombre del cliente: {nombre_cliente}")
print(f"Monto de la compra: {monto_compra:,} COP")
print(f"Descuento recibido: {monto_descuento:,} COP ({descuento*100}%)")
print(f"Monto a pagar: {monto_a_pagar:,} COP")

