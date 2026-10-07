while True:
    print("\n1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("Adiós")
        break

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida")
        continue

    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
    except ValueError:
        print("Error: debes escribir números.")
        continue

    if opcion == "1":
        print("Resultado:", a + b)

    elif opcion == "2":
        print("Resultado:", a - b)

    elif opcion == "3":
        print("Resultado:", a * b)

    elif opcion == "4":
        if b == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            print("Resultado:", a / b)