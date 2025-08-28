# =========================================
# Inteligencia Artificial - Tarea práctica
# Estrategia de movimiento hacia el objetivo con batería limitada
# =========================================

# ========================
# 1. VARIABLES DE ESTADO
# ========================
estado_robot = {
    "posicion": (0, 0),
    "bateria": 30,               # Batería inicial reducida para forzar recargas
    "objetivo_alcanzado": False,
    "pasos": 0
}

objetivo = (2, 2)

print("Estado inicial del robot:", estado_robot)

# ========================
# 2. ACCIONES POSIBLES
# ========================
acciones = ["adelante", "atras", "izquierda", "derecha", "recargar"]

# ========================
# 3. FUNCIÓN DE RECOMPENSA
# ========================
def recompensa(accion, estado, intento_invalido=False):
    if intento_invalido:
        return -5
    if accion == "recargar":
        return 5
    elif estado["objetivo_alcanzado"]:
        if estado["pasos"] <= 5:
            return 20
        return 10
    elif accion in ["adelante", "atras", "izquierda", "derecha"]:
        return -1
    return 0

# ========================
# 4. FUNCIÓN DE MOVIMIENTO
# ========================
def mover_robot(estado, accion):
    x, y = estado["posicion"]

    # Si batería es 0 y no recarga → inválido
    if estado["bateria"] <= 0 and accion != "recargar":
        return estado, True

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

    if accion != "recargar":
        estado["posicion"] = (x, y)
        estado["bateria"] -= 10

    if estado["posicion"] == (2, 2):
        estado["objetivo_alcanzado"] = True

    estado["pasos"] += 1
    return estado, False

# ========================
# 5. ESTRATEGIA DEL ROBOT
# ========================
def estrategia_robot(estado, objetivo):
    x, y = estado["posicion"]
    gx, gy = objetivo

    # Si batería es baja, priorizar recargar
    if estado["bateria"] <= 0:
        return "recargar"

    # Mover hacia la meta en eje X primero
    if x < gx:
        return "adelante"
    elif x > gx:
        return "atras"

    # Luego mover en eje Y
    if y < gy:
        return "derecha"
    elif y > gy:
        return "izquierda"

    # Si ya está en el objetivo
    return None

# ========================
# 6. SIMULACIÓN
# ========================
estado = estado_robot.copy()
recompensa_total = 0

for paso in range(15):
    if estado["objetivo_alcanzado"]:
        break

    accion = estrategia_robot(estado, objetivo)
    if accion is None:
        break

    estado, invalido = mover_robot(estado, accion)
    r = recompensa(accion, estado, intento_invalido=invalido)
    recompensa_total += r

    print(f"Paso {paso+1}: Acción = {accion}, Estado = {estado}, Recompensa = {r}")

print("\nRecompensa total obtenida:", recompensa_total)

