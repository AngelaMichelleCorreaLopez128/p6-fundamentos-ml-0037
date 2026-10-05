# Angela Correa NC = 0037
print("Python Variables")
print("--+-+-+-++--+-++--+")
print("Ejemplo 1")
x = 10
y = "Ariana"
print(x)
print(y)
print("--+-+-+-++--+-++--+")
print("Ejemplo 2")
x = 8       # x is of type int
x = "Jeff" # x is now of type str
print(x)
print("--+-+-+-++--+-++--+")
print("Ejemplo 3" )
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print("--+-+-+-++--+-++--+")
print("Python Variables - Asignar Múltiples Valores")
print("--+-+-+-++--+-++--+")
print("Ejemplo 1")
x, y, z = "Manzana", "Fresa", "Mango"
print(x)
print(y)
print(z)
print("--+-+-+-++--+-++--+")
print("Ejemplo 2")
x = y = z = "Platano"
print(x)
print(y)
print(z)
print("--+-+-+-++--+-++--+")
print("Ejemplo 3")
fruits = ["Piña", "Coco", "Lima"]
x, y, z = fruits
print(x)
print(y)
print(z)
print("--+-+-+-++--+-++--+")
print("Tipos de datos en Python")
print("--+-+-+-++--+-++--+")
print("Ejemplo 1")
edad = 25          # int
precio = 19.99     # float

print("--- 1. Números ---")
print("Edad:", edad, "| Tipo:", type(edad))
print("Precio:", precio, "| Tipo:", type(precio))
print("--+-+-+-++--+-++--+")
print("Ejemplo 2")
nombre = "Ana"
mensaje = 'Hola, ¿cómo estás?'

print("\n--- 2. Cadenas de Texto ---")
print("Nombre:", nombre, "| Tipo:", type(nombre))
print("Mensaje:", mensaje)
frutas = ["manzana", "banana", "cereza"]
numeros = [10, 20, 30]

print("--+-+-+-++--+-++--+")
print("Ejemplo 3")
print("\n--- 3. Listas ---")
print("Lista de frutas:", frutas, "| Tipo:", type(frutas))
print("Primera fruta:", frutas[0])  # Muestra 'manzana'
print("--+-+-+-++--+-++--+")
print("Operadores aritmeticos en Python")
print("--+-+-+-++--+-++--+")
print("Ejemplo 1")
x = 20
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
print("--+-+-+-++--+-++--+")
print("Ejemplo 2")
x = 14
y = 6

print(x / y)
print("--+-+-+-++--+-++--+")
print("Ejemplo 3")
x = 15
y = 3

print(x // y)
print("--+-+-+-++--+-++--+")
print("Python Comparasion de Operadores")
print("--+-+-+-++--+-++--+")
print("Ejemplo 1")
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print("--+-+-+-++--+-++--+")
print("Ejemplo 2")
x = 5

print(1 < x < 10)

print(1 < x and x < 10)
print("--+-+-+-++--+-++--+")
print("Ejemplo 3")
a = 10
b = 5

# 1. Igual a (==)
print("¿a es igual a b?:", a == b)           # False

# 2. Diferente / No igual a (!=)
print("¿a es diferente de b?:", a != b)       # True

# 3. Mayor que (>)
print("¿a es mayor que b?:", a > b)           # True

# 4. Menor que (<)
print("¿a es menor que b?:", a < b)           # False

# 5. Mayor o igual que (>=)
print("¿a es mayor o igual que 10?:", a >= 10) # True

# 6. Menor o igual que (<=)
print("¿b es menor o igual que 3?:", b <= 3)   # False


# ==========================================
# Ejemplo práctico usando condicionales (if)
# ==========================================
edad = 18

if edad >= 18:
    print("\nAcceso concedido: Eres mayor de edad.")
else:
    print("\nAcceso denegado: Eres menor de edad.")
print("--+-+-+-++--+-++--+")
print("Operadores Lógicos en Python")
print("--+-+-+-++--+-++--+")
print("Ejemplo 1")
x = 5

print(x > 0 and x < 10)
print("--+-+-+-++--+-++--+")
print("Ejemplo 2")
x = 5

print(x < 5 or x > 10)
print("--+-+-+-++--+-++--+")
print("Ejemplo 3")
x = 5

print(not(x > 3 and x < 10))