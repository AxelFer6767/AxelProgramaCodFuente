a = 1.5
b = 2
c = 2.5
cantPa = 0
cantCho = 0
cantRe = 0
dinero = float(input("Ingrese su dinero: "))
if dinero < 1.5:
    print("No cuentas con suficiente dinero")
else:
    while dinero >= c:
        dinero = dinero - c
        cantRe = cantRe + 1
    while dinero >= b:
        dinero = dinero - b
        cantCho = cantCho + 1
    while dinero >= a:
        dinero = dinero - a
        cantPa = cantPa + 1
    total = cantPa + cantCho + cantRe
    print("Se pueden comprar:")
    print("Refrescos:", cantRe)
    print("Chocolates:", cantCho)
    print("Papas:", cantPa)
    print("Total de productos:", total)
    print("Sobrante:", dinero)