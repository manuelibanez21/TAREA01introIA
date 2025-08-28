# =========================================
# Inteligencia Artificial - Tarea práctica
# Conceptos: Estado, Espacio de Estados, Acciones, Recompensa y Ambiente
# =========================================

import random

# ========================
# 1. VARIABLES DE ESTADO
# ========================
estado_robot = {
    "posicion": (0, 0),
    "bateria": 50,               # Batería inicial
    "objetivo_alcanzado": False,
    "pasos": 0                   # Contador de pasos
}

print("Estado inicial del robot:", estado_robot)

# ========================
# 2. ESPACIO DE ESTADOS
# ========================
posiciones = [(x, y) for x in range(3) for y in range(3)]
baterias = list(range(0, 101, 10))  # batería de 0 a 100 en intervalos de 10

espacio_estados = [(p, b) for p in posiciones for b in baterias]
print("\nTotal de estados posibles:", len(espacio_estados))
print("Ejemplos de estados:", espacio_estados[:5])

# ========================
# 3. ESPACIO DE ACCIONES
# ========================
acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]
print("\nAcciones posibles:", acciones)

# ========================
# 4. FUNCIÓN DE RECOMPENSA
# ========================
def recompensa(accion, estado, intento_invalido=False):
    # Intento de moverse sin batería
    if intento_invalido:
        return -5
    
    if accion == "recargar":
        return 5
    
    elif estado["objetivo_alcanzado"]:
        # Bonus si llegó rápido
        if estado["pasos"] <= 5:
            return 20
        return 10
    
    elif accion in ["adelante", "atras", "izquierda", "derecha"]:
        return -1  # costo por moverse
    
    return 0

# ========================
# 5. AMBIENTE Y SIMULACIÓN
# ========================
def mover_robot(estado, accion):
    x, y = estado["posicion"]

    # Si batería es 0 y no se recarga → no se mueve
    if estado["bateria"] <= 0 and accion != "recargar":
        return estado, True  # intento inválido

    if accion == "adelante":
        x = min(x + 1, 2)
    elif accion == "atras":
        x = max(x - 1, 0)
    elif accion == "derecha":
        y = min(y + 1, 2)
    elif accion == "izquierda":
        y = max(y - 1, 0)
    elif accion == "recargar":
        estado["bateria"] = 100

    # Actualizar posición solo si no es recarga
    if accion != "recargar":
        estado["posicion"] = (x, y)
        estado["bateria"] -= 10  # cada movimiento gasta batería

    # Si llega al objetivo
    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    estado["pasos"] += 1
    return estado, False

# ========================
# 6. SIMULACIÓN DEL ROBOT
# ========================
estado = {"posicion": (0, 0), "bateria": 50, "objetivo_alcanzado": False, "pasos": 0}
recompensa_total = 0

for paso in range(10):
    accion = random.choice(acciones)
    estado, invalido = mover_robot(estado, accion)
    r = recompensa(accion, estado, intento_invalido=invalido)
    recompensa_total += r

    print(f"Paso {paso+1}: Acción = {accion}, Estado = {estado}, Recompensa = {r}")

print("\nRecompensa total obtenida:", recompensa_total)
