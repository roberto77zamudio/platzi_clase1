def run():
    costo_iphone={
        "iphone_12":12000,
        "iphone_13":13000,
        "iphone_14":14000,
        "iphone_15":15000,
    }
    # print (costo_iphone)

    # print(" El iphone 12 cuesta " + str(costo_iphone["iphone_12"]))

    # for costo in costo_iphone.keys():
    #     print (costo)

    # for costo in costo_iphone.values():
    #     print(costo)

    for celular, costo in costo_iphone.items():
        print("El " + celular + " tiene un costo de " + str(costo))


if __name__ == "__main__":
    run()

