import random


def run():
    numero_aleatorio = random.randint(1, 200)
    numero_elegido = int(input("Elige un número del 1 al 200: "))
    if numero_elegido > 200:
        print ("Elige un numero entre 1 y 200")
    numero_elegido=int(input("Elige otro número: "))
    while numero_elegido!=numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número mas grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido=int(input("Elige otro número, no seas menso: "))
    print("¡Ganaste!")


if  __name__ == "__main__":
    run()


    