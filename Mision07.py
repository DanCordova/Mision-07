#Autor: Daniel Cordóva Bermúdez
#Grupo 02
#Descripción: El programa corre un menu el cual se puede elegir 3 opciones. Calcular residuo o cociente de divisiones, encontrar le mayyor numero y salir.


#LA función imrpime el menu para elegir la opción y regresa el dato.
def selecionarOpcion():

    print("""Misión 07. Ciclos while"
    Autor: Daniel Córdova Bermúdez
    Matrícula: A01377242
    1. Calcular divisiones
    2. Encontrar el mayor
    3. Salir""")
    opcion = int(input("Teclea tu opción: "))
    return opcion


#La funcion probarDivisiones ingresa los datos del menu para que en un ciclo while se calcule el residuo y el cociente.
def probarDivisiones(divisor, dividendo):
    residuo = dividendo
    cociente = 0

    while(divisor <= residuo):
        residuo -= divisor
        cociente += 1
    print("%d / %d = %d, sobra %d" % (dividendo, divisor, cociente, residuo))


#La funcion encontrarMayor encuentra el mayor de una serie de numeros.
def encontrarMayor():

    mayor = 0
    numero = 0

    while (numero != -1):
        numero = int(input("Teclea un número [-1 para salir]: "))
        if numero > mayor:
            mayor = numero

    if mayor == 0:
        print("No hay valor mayor")
    else:
        print("El mayor es:", mayor)

#Funcion principal se encarga de imprimir el menu y de llamar las otras funciones.
def main():
    
    opcion = 0
    while (opcion != 3):

        opcion = selecionarOpcion()

        if opcion == 1:
            print("Calculando divisiones")
            dividendo = int(input("Dividendo:"))
            divisor = int(input("Divisor:"))
            probarDivisiones(divisor,dividendo)
            print("")

        elif opcion == 2:
            print("Teclea una serie de números para encontrar el mayor.")
            encontrarMayor()
            print("")

        elif opcion == 3:
            print("Gracias por usar este programa,regresa pronto.")
            print("")

        else:
            print("ERROR, teclea 1, 2 o 3")
            print("")


# LLama a la funcion princial.
main()