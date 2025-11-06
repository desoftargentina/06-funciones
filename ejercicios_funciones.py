# =========================================================================================================
# Ejercicio N°.1

# Bloque principal del programa
if __name__ == "__main__":
    # La parte principal del programa comienza aquí.
    #print("--- Inicio del programa principal ---")
    
    # Llamada a la función
    imprimir_hola_mundo()
    
    #print("--- Fin del programa principal ---")
# =========================================================================================================


# =========================================================================================================
# Ejercicio N°.2
# Bloque principal del programa
if __name__ == "__main__":
    
    print("--- Generador de Saludos Personalizados ---")
    
    # 1. Solicitar el nombre al usuario
    # La función input() pausa el programa y espera a que el usuario escriba algo
    nombre_usuario = input("Por favor, introduce tu nombre: ")
    
    # 2. Llamar a la función y guardar el valor devuelto
    # La variable 'mensaje' contendrá el string "¡Hola [Nombre]!"
    mensaje = saludar_usuario(nombre_usuario)
    
    # 3. Imprimir el resultado
    print("-" * 30)
    print(mensaje)
    print("-" * 30)
# =========================================================================================================


# =========================================================================================================
# Ejercicio N°.3
# 1. Definición de la función con cuatro parámetros
def informacion_personal(nombre, apellido, edad, residencia):
    """
    Recibe los datos personales e imprime una oración de presentación formateada.
    
    Parámetros:
      nombre (str): Nombre de la persona.
      apellido (str): Apellido de la persona.
      edad (int): Edad de la persona.
      residencia (str): Lugar de residencia de la persona.
    """
    
    # Construcción de la frase usando f-strings
    frase = (
        f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."
    )
    
    # Impresión de la frase
    print("-" * 40)
    print(frase)
    print("-" * 40)

# 2. Bloque principal para la interacción con el usuario y la llamada
if __name__ == "__main__":
    
    print("--- Recolección de Datos Personales ---")
    
    # 2.1. Solicitar los datos al usuario
    input_nombre = input("Por favor, introduce tu nombre: ")
    input_apellido = input("Por favor, introduce tu apellido: ")
    # Nota: Aunque la edad es un número, input() siempre devuelve un string.
    # No es estrictamente necesario convertirlo a int para este ejercicio, 
    # pero es buena práctica si se fuera a hacer cálculos.
    input_edad = input("¿Qué edad tienes?: ")
    input_residencia = input("¿Dónde resides actualmente?: ")
    
    print("\nGenerando tu presentación...")
    
    # 2.2. Llamar a la función con los valores obtenidos del usuario
    # Los argumentos se pasan en el mismo orden que los parámetros de la función.
    informacion_personal(
        input_nombre, 
        input_apellido, 
        input_edad, 
        input_residencia
    )
    
    print("¡Proceso completado!")
    
# =========================================================================================================

# =========================================================================================================
# Ejercicio N°.4
import math # Necesario para obtener el valor de Pi (math.pi)

# 1. Función para calcular el área del círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo usando la fórmula: Área = π * radio^2
    
    Parámetros:
      radio (float): El radio del círculo.
      
    Devuelve:
      float: El área calculada.
    """
    area = math.pi * (radio ** 2)
    return area

# 2. Función para calcular el perímetro del círculo
def calcular_perimetro_circulo(radio):
    """
    Calcula el perímetro (circunferencia) de un círculo usando la fórmula: Perímetro = 2 * π * radio
    
    Parámetros:
      radio (float): El radio del círculo.
      
    Devuelve:
      float: El perímetro calculado.
    """
    perimetro = 2 * math.pi * radio
    return perimetro

# 3. Bloque principal para la interacción con el usuario y la llamada a las funciones
if __name__ == "__main__":
    
    print("--- Calculadora de Área y Perímetro de Círculo ---")
    
    # 3.1. Solicitar el radio al usuario
    while True:
        try:
            # Usamos float() para convertir la entrada del usuario a un número decimal
            radio_ingresado = float(input("Por favor, introduce el valor del radio del círculo: "))
            if radio_ingresado < 0:
                print("El radio no puede ser un valor negativo. Inténtalo de nuevo.")
                continue
            break # Salir del bucle si la entrada es válida
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
    
    print("\nCalculando resultados...")
    
    # 3.2. Llamar a la función de área y almacenar el valor devuelto
    area_resultante = calcular_area_circulo(radio_ingresado)
    
    # 3.3. Llamar a la función de perímetro y almacenar el valor devuelto
    perimetro_resultante = calcular_perimetro_circulo(radio_ingresado)
    
    # 3.4. Mostrar los resultados
    print("\n" + "=" * 40)
    print(f"Para un círculo con Radio = {radio_ingresado:.2f}:")
    # Utilizamos :.2f para mostrar solo 2 decimales y que el resultado sea limpio.
    print(f" Área (π * r²) = {area_resultante:.2f} unidades cuadradas")
    print(f" Perímetro (2 * π * r) = {perimetro_resultante:.2f} unidades")
    print("=" * 40)

# =========================================================================================================



# =========================================================================================================
# Ejercicio N°.5
# 1. Definición de la función de conversión
def segundos_a_horas(segundos):
    """
    Convierte una cantidad de segundos a horas.
    
    Fórmula: horas = segundos / 3600
    
    Parámetros:
      segundos (float/int): Cantidad de segundos a convertir.
      
    Devuelve:
      float: Cantidad equivalente en horas.
    """
    # 3600 es el número de segundos en una hora
    horas = segundos / 3600
    return horas

# 2. Bloque principal para la interacción con el usuario y la lógica condicional
if __name__ == "__main__":
    
    print("--- Conversor de Segundos a Horas (Validación con if/else) ---")
    
    # 2.1. Solicitar los segundos al usuario
    # ADVERTENCIA: Esta línea FALLARÁ si el usuario ingresa texto, ya que no hay try/except.
    segundos_ingresados = float(input("Introduce la cantidad de segundos a convertir: "))
            
    # 2.2. Usar un IF/ELSE para validar que el tiempo sea lógico (no negativo)
    if segundos_ingresados >= 0:
        # Lógica de conversión
        
        # Llamar a la función
        horas_calculadas = segundos_a_horas(segundos_ingresados)
        
        # Mostrar el resultado
        print("\n" + "=" * 40)
        print(f"{segundos_ingresados} segundos equivalen a:")
        # Usamos el formato :.4f para mostrar con 4 decimales
        print(f" {horas_calculadas:.4f} horas") 
        print("=" * 40)
        
    else:
        # Lógica de error/advertencia
        print("\n Error: La cantidad de segundos no puede ser un número negativo.")

# =========================================================================================================



# =========================================================================================================
# Ejercicio N°.6
# 1. Definición de la función
def tabla_multiplicar(numero):
    """
    Recibe un número y imprime su tabla de multiplicar del 1 al 10.
    
    Parámetros:
      numero (int/float): El número cuya tabla se desea calcular.
    """
    
    print(f"\n--- Tabla de multiplicar del {numero} ---")
    
    # Usamos un bucle 'for' para iterar 10 veces (del 1 al 10)
    for i in range(1, 11):
        # Cálculo de la multiplicación
        resultado = numero * i
        
        # Impresión del resultado: Número x i = Resultado
        print(f"{numero} x {i:2} = {resultado}") 
    
    print("--------------------------------------")

# 2. Bloque principal para solicitar datos y llamar a la función
if __name__ == "__main__":
    
    print("--- Generador Simple de Tablas de Multiplicar ---")
    
    # 2.1. Solicitar el número al usuario y convertir directamente a float.
    # ADVERTENCIA: Esta línea FALLARÁ si el usuario ingresa texto en lugar de un número.
    num_str = input("Introduce el número del que deseas la tabla: ")
    num_ingresado = float(num_str)
    
    # 2.2. Llamar a la función con el valor ingresado
    tabla_multiplicar(num_ingresado)
    
    print("¡Proceso finalizado!")

# =========================================================================================================



# =========================================================================================================
# Ejercicio N°.7
# 1. Definición de la función
def operaciones_basicas(a, b):
    """
    Realiza las cuatro operaciones aritméticas básicas entre dos números.
    Devuelve una tupla con (suma, resta, multiplicacion, division).
    
    Parámetros:
      a (float/int): El primer número.
      b (float/int): El segundo número.
      
    Devuelve:
      tuple: (suma, resta, multiplicacion, division).
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    
    # Manejar el caso de división por cero usando un IF simple (sin try/except)
    if b != 0:
        division = a / b
    else:
        # Devolvemos un string para indicar que la operación es indefinida
        division = "Indefinida" 
        
    # Devolvemos los cuatro resultados dentro de una tupla
    return (suma, resta, multiplicacion, division)

# 2. Bloque principal para la interacción con el usuario y la llamada a la función
if __name__ == "__main__":
    
    print("--- Calculadora de Operaciones Básicas Simple ---")
    
    # 2.1. Solicitar los dos números al usuario
    # ADVERTENCIA: Esta parte FALLARÁ si se ingresa texto, ya que no hay try/except.
    num1_str = input("Introduce el primer número (a): ")
    num2_str = input("Introduce el segundo número (b): ")
    
    # Conversión directa a float
    num1 = float(num1_str)
    num2 = float(num2_str)
    
    # 2.2. Llamar a la función y desempaquetar la tupla devuelta
    suma_r, resta_r, mult_r, div_r = operaciones_basicas(num1, num2)
    
    # 2.3. Mostrar los resultados de forma clara
    print("\n" + "=" * 35)
    print(f"Resultados de operar {num1} y {num2}:")
    print("=" * 35)
    print(f"Suma (a + b):          {suma_r}")
    print(f"Resta (a - b):         {resta_r}")
    print(f"Multiplicación (a * b): {mult_r}")
    print(f"División (a / b):       {div_r}")
    print("=" * 35)

# =========================================================================================================



# =========================================================================================================
# Ejercicio N°.8
# 1. Definición de la función para calcular el IMC
def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    Fórmula: IMC = peso / (altura * altura)
    
    Parámetros:
      peso (float): Peso corporal en kilogramos (kg).
      altura (float): Altura en metros (m).
      
    Devuelve:
      float: El valor del Índice de Masa Corporal, o None si la altura es inválida.
    """
    # Usamos un IF simple para prevenir la división por cero o números no válidos
    if altura > 0:
        imc = peso / (altura ** 2)
        return imc
    else:
        # Devuelve None si la altura es cero o negativa.
        return None 

# 2. Bloque principal para la interacción con el usuario y la llamada a la función
if __name__ == "__main__":
    
    print("--- Calculadora de Índice de Masa Corporal (IMC) Simple ---")
    
    # 2.1. Solicitar los datos al usuario.
    # ADVERTENCIA: Estas líneas FALLARÁN si el usuario ingresa texto en lugar de un número.
    peso_usuario = float(input("Introduce tu peso en kilogramos (ej: 75.5): "))
    altura_usuario = float(input("Introduce tu altura en metros (ej: 1.70): "))
    
    # 2.2. Llamar a la función
    resultado_imc = calcular_imc(peso_usuario, altura_usuario)
    
    # 2.3. Mostrar el resultado usando IF/ELSE para manejar el resultado de la función
    print("\n" + "=" * 40)
    
    if resultado_imc is not None:
        # El resultado es válido
        print(f"Tu peso: {peso_usuario} kg, Tu altura: {altura_usuario} m")
        # Usamos :.2f para formatear el resultado a dos decimales
        print(f" Tu Índice de Masa Corporal (IMC) es: {resultado_imc:.2f}")
    else:
        # La función devolvió None debido a una altura inválida
        print(" Error: No se pudo calcular el IMC. La altura debe ser mayor a cero.")
        
    print("=" * 40)

# =========================================================================================================



# =========================================================================================================
# Ejercicio N°.9
# 1. Definición de la función
def celsius_a_fahrenheit(celsius):
    """
    Convierte una temperatura de grados Celsius a grados Fahrenheit.
    
    Fórmula: F = (C * 9/5) + 32
    
    Parámetros:
      celsius (float): La temperatura en grados Celsius.
      
    Devuelve:
      float: La temperatura equivalente en grados Fahrenheit.
    """
    # 9/5 puede ser 1.8. Usamos la multiplicación y suma.
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# 2. Bloque principal para la interacción con el usuario y la llamada a la función
if __name__ == "__main__":
    
    print("--- Conversor de Celsius a Fahrenheit ---")
    
    # 2.1. Solicitar la temperatura al usuario
    # ADVERTENCIA: Esta línea FALLARÁ si el usuario ingresa texto en lugar de un número.
    celsius_str = input("Introduce la temperatura en grados Celsius (°C): ")
    
    # Conversión directa a float
    celsius_ingresado = float(celsius_str)
    
    # 2.2. Usar IF/ELSE para validar que la temperatura no es absurdamente baja
    # (Aunque no siempre es necesario, muestra el uso de condicionales)
    if celsius_ingresado >= -273.15: # -273.15 °C es el cero absoluto
        
        # 2.3. Llamar a la función
        fahrenheit_calculado = celsius_a_fahrenheit(celsius_ingresado)
        
        # 2.4. Mostrar el resultado
        print("\n" + "=" * 40)
        print(f"Temperatura ingresada: {celsius_ingresado:.2f} °C")
        # Usamos :.2f para mostrar el resultado con dos decimales
        print(f"  Equivalente en Fahrenheit: {fahrenheit_calculado:.2f} °F")
        print("=" * 40)
        
    else:
        # Lógica de error/advertencia
        print("\n Error: La temperatura ingresada está por debajo del cero absoluto.")

# =========================================================================================================




# =========================================================================================================
# Ejercicio N°.10
# 1. Definición de la función
def calcular_promedio(a, b, c):
    """
    Calcula el promedio (media aritmética) de tres números.
    
    Parámetros:
      a (float): Primer número.
      b (float): Segundo número.
      c (float): Tercer número.
      
    Devuelve:
      float: El valor del promedio.
    """
    # Sumamos los tres números y dividimos por 3
    suma = a + b + c
    promedio = suma / 3
    return promedio

# 2. Bloque principal para la interacción con el usuario y la llamada a la función
if __name__ == "__main__":
    
    print("--- Calculadora de Promedio (3 Números) ---")
    
    # 2.1. Solicitar los tres números al usuario
    # ADVERTENCIA: Estas líneas FALLARÁN si el usuario ingresa texto en lugar de un número.
    num1_str = input("Introduce el primer número: ")
    num2_str = input("Introduce el segundo número: ")
    num3_str = input("Introduce el tercer número: ")
    
    # Conversión directa a float
    num1 = float(num1_str)
    num2 = float(num2_str)
    num3 = float(num3_str)
    
    # 2.2. Validar si los números son positivos usando IF
    if num1 >= 0 and num2 >= 0 and num3 >= 0:
        
        # 2.3. Llamar a la función
        promedio_calculado = calcular_promedio(num1, num2, num3)
        
        # 2.4. Mostrar el resultado
        print("\n" + "=" * 40)
        print(f"Números ingresados: {num1}, {num2}, {num3}")
        # Usamos :.2f para mostrar el resultado con dos decimales
        print(f" El promedio de los tres números es: {promedio_calculado:.2f}")
        print("=" * 40)
        
    else:
        # Lógica de advertencia si algún número es negativo
        print("\n Advertencia: Se detectó un número negativo. El cálculo se realizó,")
        print("   pero si solo esperas promediar cantidades positivas, revisa la entrada.")

# =========================================================================================================




