import random

print("Bienvenido a 'Binario vs Decimal'")
intentos = 0
jugar_nuevamente = "s"

while jugar_nuevamente.lower() == "s":

    print("\n¿Qué querés hacer?")
    print("1. Convertí un número entre sistemas")
    print("2. Adiviná el número binario a partir de un decimal")

    modo_valido = False
    while modo_valido == False:
        modo = input("Seleccioná una opción (1 o 2): ")
        if modo == "1" or modo == "2":
            modo_valido = True
        else:
            print("❌ Opción no válida. Elegí 1 o 2.")

    if modo == "1":
        print("\n¿Qué tipo de número quiere convertir?")
        print("1. Sistema decimal.")
        print("2. Sistema binario.")
        print("3. Sistema octal.")

        modo_valido = False
        while modo_valido == False:
            modo = input("Seleccioná una opción (1 - 2 - 3: ")
            if modo == "1" or modo == "2" or modo == "3":
                modo_valido = True
            else:
                print("❌ Opción no válida. Elegí 1 o 2 o 3.")

        if modo == "1": # Usuario elige ingresar un número del sistema decimal, ingresa a condicional para elegir a qué sistema convertir su número
            numeroUsuario = int(input("Ingrese el número a convertir: "))
            print("\n¿A qué sistema lo quiere convertir?")
            print("1. Sistema binario.")
            print("2. Sistema octal.")

            modo_valido = False
            while modo_valido == False:
                modo = input("Seleccioná una opción (1 - 2): ")
                if modo == "1" or modo == "2":
                    modo_valido = True
                else:
                    print("❌ Opción no válida. Elegí 1 o 2.")

            if modo == "1": # Conversión de número decimal a binario
                numeroDecABin = numeroUsuario # Creamos una nueva variable con el mismo valor que el número que ingresó el usuario
                binario = 0 # Se inicializa variable binario en 0
                i = 0 # Se inicializa variable i en 0
                while numeroDecABin > 0: # Ciclo para convertir el número decimal a binario
                    resto = numeroDecABin % 2 # Dividimos el número decimal en 2 con % para obtener resto y lo guardamos en la variable resto
                    numeroDecABin = numeroDecABin // 2 # Divimos por 2 el número del usuario con // para obtener la parte entera y la guardamos en la misma variable que ingresó el usuario
                    binario += resto * (10**i) # Con cada repetición del ciclo acá hacemos el número binario. Multiplicamos el resto por (10 elevado al valor de i) y esto lo sumamos a binario
                    i+=1 # Sumamos 1 a i
                print(f"El número decimal {numeroUsuario} en binario es {binario}.")
            elif modo == "2": # Conversión de número decimal a octal
                octal = 0
                i = 0
                numeroDecAOct = numeroUsuario
                while numeroDecAOct > 0:
                    resto = numeroDecAOct % 8
                    octal = resto * (10**i) + octal
                    numeroDecAOct = numeroDecAOct // 8
                    i+=1
                print(f"El número en decimal {numeroUsuario} en octal es {octal}.")

        elif modo == "2": # Usuario elige ingresar un número del sistema binario, ingresa a condicional para elegir a qué sistema convertir su número
            numeroUsuario = input("Ingrese el número a convertir: ")
            print("\n¿A qué sistema lo quiere convertir?")
            print("1. Sistema decimal.")
            print("2. Sistema octal.")

            modo_valido = False
            while modo_valido == False:
                modo = input("Seleccioná una opción (1 - 2): ")
                if modo == "1" or modo == "2":
                    modo_valido = True
                else:
                    print("❌ Opción no válida. Elegí 1 o 2.")

            if modo == "1": # Conversión de número binario a decimal
                numeroBinADec = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroBinADec % 10
                    decimal = decimal + digito*(2**i)
                    i +=1
                    numeroBinADec = numeroBinADec // 10
                print(f"El número binario {numeroUsuario} en decimal es {decimal}.")
            elif modo == "2": # Conversión de número binario a octal
                numeroBinAOct = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroBinAOct % 10
                    decimal = decimal + digito*(2**i)
                    i +=1
                    numeroBinAOct = numeroBinAOct // 10
                octal = 0
                i = 0
                numeroDecAOct = decimal
                while numeroDecAOct > 0:
                    resto = numeroDecAOct % 8
                    octal = resto * (10**i) + octal
                    numeroDecAOct = numeroDecAOct // 8
                    i+=1
                print(f"El número binario {numeroUsuario} en octal es {octal}.")

        elif modo == "3": # Usuario elige ingresar un número del sistema octal, ingresa a condicional para elegir a qué sistema convertir su número
            numeroUsuario = input("Ingrese el número a convertir: ")
            print("\n¿A qué sistema lo quiere convertir?")
            print("1. Sistema decimal.")
            print("2. Sistema binario.")

            modo_valido = False
            while modo_valido == False:
                modo = input("Seleccioná una opción (1 - 2): ")
                if modo == "1" or modo == "2":
                    modo_valido = True
                else:
                    print("❌ Opción no válida. Elegí 1 o 2.")

            if modo == "1": # Conversión de octal a decimal
                numeroOctADec = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroOctADec % 10
                    decimal = decimal + digito*(8**i)
                    i +=1
                    numeroOctADec = numeroOctADec // 10
                print(f"El número octal {numeroUsuario} en decimal es {decimal}.")
            if modo == "2": # Conversion de octal a binario
                numeroOctADec = int(numeroUsuario)
                cantidadDeBin = int(len(numeroUsuario))
                decimal = 0
                i = 0
                while cantidadDeBin > i:
                    digito = numeroOctADec % 10
                    decimal = decimal + digito*(8**i)
                    i +=1
                    numeroOctADec = numeroOctADec // 10
                #numeroDecABin = decimal # Creamos una nueva variable con el mismo valor que el número que ingresó el usuario
                binario = 0
                i = 0
                while decimal > 0: 
                    resto = decimal % 2
                    decimal = decimal // 2
                    binario += resto * (10**i)
                    i+=1
                print(f"El número octal {numeroUsuario} en binario es {binario}.")

    elif modo == "2":
        print("\nADIVINÁ EL BINARIO A PARTIR DE UN DECIMAL")
        print("Elegí un nivel de dificultad:")
        print("1. Fácil (4 bits)")
        print("2. Medio (8 bits)")

        dificultad_valida = False
        while dificultad_valida == False:
            opcion = input("Seleccioná una opción (1 o 2): ")
            if opcion == "1":
                bits = 4
                dificultad_valida = True
            elif opcion == "2":
                bits = 8
                dificultad_valida = True
            else:
                print("❌ Opción no válida. Elegí 1 o 2.")

        max_numero = 2**bits - 1
        numero_decimal = random.randint(0, max_numero)
        numero_binario = bin(numero_decimal)[2:].zfill(bits)

        print(f"\nAdiviná el número binario del decimal: {numero_decimal}")
        intento = input("Tu respuesta (binario): ")

        solo_0_y_1 = True
        for caracter in intento:
            if caracter != "0" and caracter != "1":
                solo_0_y_1 = False

        if solo_0_y_1 and intento != "":
            intento_usuario = intento.zfill(bits)
            if intento_usuario == numero_binario:
                print("✅ ¡Correcto!")
            else:
                print(f"❌ Incorrecto. El valor correcto era: {numero_binario}")
                print("\n¿Cómo se convierte un número decimal a binario?")
                print(f"  Empezamos dividiendo {numero_decimal} sucesivamente por 2 y guardamos los restos.")

                temp = numero_decimal
                pasos = []

                while temp > 0:
                    cociente = temp // 2
                    resto = temp % 2
                    pasos.append(f"  {temp} ÷ 2 = {cociente}, resto = {resto}")
                    temp = cociente

                for paso in pasos:
                    print(paso)

                print(f"\n  El resultado en binario (leyendo los restos de abajo hacia arriba) es: {numero_binario}")
        else:
            print("❌ Entrada inválida. Solo se permiten 0 y 1.")
            print(f"El valor correcto era: {numero_binario}")

    jugar_nuevamente = input("\n¿Querés volver al menú principal? (s/n): ")

print("¡Gracias por usar Binario vs Decimal!")