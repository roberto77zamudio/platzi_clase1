pesos = input ("¿Cuantos pesos mexicanos tienes?: ")
pesos = float (pesos)
valor_dolar = 20.5486
dolares = pesos / valor_dolar
dolares = round (dolares, 2)
dolares = str (dolares)
print ("tienes $ " + dolares + " dolares" )
