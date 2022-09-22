import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    if numero_elegido > 100:
        print ("Elige un numero entre 1 y 100")
    numero_elegido=int(input("Elige otro número: "))
    while numero_elegido!=numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número mas grande")
        else:
            print("Busca un número más pequeño")
        numero_elegido=int(input("Elige otro número: "))
    print("¡Ganaste!")


if  __name__ == "__main__":
    run()


    