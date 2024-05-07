#leonel pavez 
#FUNDAMENTOS DE PROGRAMACION_003D
#Evaluación Parcial N°2 Forma-C


#definir los artefactos y sus consumos diarios
artefactos = {
    1: "Hervidor",
    2: "Microondas 800 watts",
    3: "Refrigerador Clase A",
    4: "Aspiradora",
    5: "Secador de pelo",
    6: "Lavadora/Secadora"
}

consumosdiarios = [5.9, 0.8, 7.6, 4.0, 4.5, 2.1]

#funcion para calcular el consumo semanal por persona de un artefacto
def consumosemanalporpersona(artefacto):
    return consumosdiarios[artefacto - 1] * 7

#Función para calcular el consumo semanal total del grupo familiar
def consumo_semanal_total(integrantes, artefactos_por_persona):
    consumo_total = 0
    for artefacto in artefactos_por_persona:
        consumo_total += consumosemanalporpersona(artefacto)
    return consumo_total

#funcion principal del programa
def main():
    # Imprimir la tabla de datos
    print("Tabla de datos:")
    print("+----+-------------------------+---------------------------+")
    print("| No.|        Artefacto        | Consumo diario por persona|")
    print("+----+-------------------------+---------------------------+")
    for i in range(1, 7):
        print(f"| {i:<2} | {artefactos[i]:<24} | {consumosdiarios[i-1]:^25} |")
    print("+----+-------------------------+---------------------------+")

    # Solicitar el número de integrantes del grupo familiar
    integrantes = int(input("\nIngrese el número de integrantes del grupo familiar (máximo 5): "))
    if integrantes < 1 or integrantes > 5:
        print("El número de integrantes debe estar entre 1 y 5.")
        return

#pedir los artefactos utilizados por cada integrante
    consumo_por_persona = {}
    for i in range(integrantes):
        print(f"\nIntegrante {i+1}:")
        consumo_por_persona[i] = []
        print("Ingrese los números de los artefactos utilizados por el integrante (separados por espacios):")
        artefactos_utilizados = list(map(int, input().strip().split()))
        for artefacto in artefactos_utilizados:
            if artefacto < 1 or artefacto > 6:
                print("El número de artefacto ingresado no es válido.")
                continue
            consumo_por_persona[i].append(artefacto)

#calcular el consumo semanal total del grupo familiar
    consumo_total = consumo_semanal_total(integrantes, [artefacto for artefactos in consumo_por_persona.values() for artefacto in artefactos])

#imprimir el resultado
    print(f"\nEl consumo semanal total para una familia de {integrantes} integrantes es de {consumo_total} kWh.")

#ejecutar la función principal
if __name__ == "__main__":
    main()