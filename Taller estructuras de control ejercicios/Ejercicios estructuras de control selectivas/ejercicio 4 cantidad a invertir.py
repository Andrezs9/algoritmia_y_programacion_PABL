# Datos de entrada
monto_compra = float(input("Ingrese el monto total de la compra: "))

#caja negra
if monto_compra > 5000000:
    inversion_empresa = monto_compra * 0.55
    prestamo_banco = monto_compra * 0.30
    credito_fabricante = monto_compra * 0.15
    intereses_credito = credito_fabricante * 0.20
else:
    inversion_empresa = monto_compra * 0.70
    prestamo_banco = 0  # No se requiere préstamo del banco
    credito_fabricante = monto_compra * 0.30
    intereses_credito = credito_fabricante * 0.20

# salida
print(f"Cantidad a invertir de los fondos de la empresa: {inversion_empresa:} COP")
print(f"Cantidad a pagar a crédito al fabricante: {credito_fabricante:} COP")
print(f"Monto a pagar por intereses: {intereses_credito:} COP")
if prestamo_banco > 0:
    print(f"Cantidad prestada al banco: {prestamo_banco:} COP")
else:
    print("No se necesita un préstamo del banco.")

