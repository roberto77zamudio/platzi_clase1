menu =  """
Bienvenido al conversor de monedas

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = input (menu)

if opcion == "1":
    pesos = input ("¿Cuantos pesos colombianos tienes?: ")
    pesos = float (pesos)
    valor_dolar = 3000
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print ("tienes $ " + dolares + " dolares" )
elif opcion == "2":
    pesos = input ("¿Cuantos pesos argentinos tienes?: ")
    pesos = float (pesos)
    valor_dolar = 60
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print ("tienes $ " + dolares + " dolares" )
elif opcion == "3":
    pesos = input ("¿Cuantos pesos mexicanos tienes?: ")
    pesos = float (pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str (dolares)
    print ("tienes $ " + dolares + " dolares" )
else:
    print ("Elige una opcion correcta")