def run():
    frase=input("Escribe una frase: ")
    for letra in frase:
        if letra == "o":
            break
        print (letra) 

if __name__ == "__main__":
    run()