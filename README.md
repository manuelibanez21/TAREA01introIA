# 🤖 Tarea 01 – Introducción a Inteligencia Artificial

Este repositorio contiene el desarrollo de la **Tarea 01**, donde se implementa un robot en un ambiente simple.  
Se trabajan conceptos de **estado, espacio de estados, acciones, recompensas y ambiente**.

---

## 📂 Archivos del repositorio

- `tarea01_original.py` → Código base entregado.  
- `tarea01_modificado.py` → Código modificado con batería, recompensas y castigos.  
- `README.md` → Documentación del procedimiento y explicación de los códigos.  

---

## 📌 Código original: `tarea01_original.py`

Este código define un robot que se mueve en una grilla de **3x3**, con un estado compuesto por:

- **Posición** `(x, y)`  
- **Batería** (solo considerada como "alta" o "baja")  
- **Objetivo alcanzado** (True/False)  

### 🔹 Principales partes del código
1. **Estado del robot**  
   Se inicializa la posición, batería y si alcanzó el objetivo.  

2. **Espacio de estados**  
   Se generan todas las combinaciones posibles de posición y niveles de batería.  

3. **Acciones**  
   El robot puede: *adelante, atrás, izquierda, derecha, recargar*.  

4. **Función de recompensa**  
   - Recargar → `+5`  
   - Alcanzar objetivo → `+10`  
   - Moverse → `-1`  

5. **Función `mover_robot`**  
   Actualiza la posición del robot según la acción. Si llega a `(2,2)`, marca que alcanzó el objetivo.  

6. **Simulación**  
   Se ejecutan 10 pasos al azar y se acumulan recompensas.  

---

## 📌 Código modificado: `tarea01_modificado.py`

Este archivo implementa las **mejoras pedidas en la tarea**:

### 🔹 Cambios realizados
1. **Descenso de batería en cada movimiento**  
   Cada vez que el robot se mueve, la batería baja `-10`.  

2. **Bloqueo si la batería es 0**  
   Si intenta moverse sin batería, no se desplaza hasta recargar.  

3. **Nuevas recompensas y castigos**
   - Intentar moverse sin batería → `-5 puntos`.  
   - Alcanzar objetivo en menos de 5 pasos → `+20 puntos extra`.  

4. **Estrategias de movimiento**  
   Se prueban movimientos aleatorios y se observa cómo afectan la recompensa total.  

---

## ⚙️ Procedimiento realizado

1. Se creó un **repositorio en GitHub** llamado `TAREA01introIA`.  
2. Se clonó el repositorio en la PC con:
   ```bash
   git clone https://github.com/manuelibanez21/TAREA01introIA.git

# 🤖 Tarea 01 – Introducción a Inteligencia Artificial

Este repositorio contiene el desarrollo de la **Tarea 01**, donde se implementa un robot en un ambiente simple.  
Se trabajan conceptos de **estado, espacio de estados, acciones, recompensas y ambiente**.

---

## 📂 Archivos del repositorio

- `tarea01_original.py` → Código base entregado.  
- `tarea01_modificado.py` → Código modificado con batería, recompensas y castigos.  
- `README.md` → Documentación del procedimiento y explicación de los códigos.  

---

## 📌 Código original: `tarea01_original.py`

Este código define un robot que se mueve en una grilla de **3x3**, con un estado compuesto por:

- **Posición** `(x, y)`  
- **Batería** (solo considerada como "alta" o "baja")  
- **Objetivo alcanzado** (True/False)  

### 🔹 Principales partes del código
1. **Estado del robot**  
   Se inicializa la posición, batería y si alcanzó el objetivo.  

2. **Espacio de estados**  
   Se generan todas las combinaciones posibles de posición y niveles de batería.  

3. **Acciones**  
   El robot puede: *adelante, atrás, izquierda, derecha, recargar*.  

4. **Función de recompensa**  
   - Recargar → `+5`  
   - Alcanzar objetivo → `+10`  
   - Moverse → `-1`  

5. **Función `mover_robot`**  
   Actualiza la posición del robot según la acción. Si llega a `(2,2)`, marca que alcanzó el objetivo.  

6. **Simulación**  
   Se ejecutan 10 pasos al azar y se acumulan recompensas.  

---

## 📌 Código modificado: `tarea01_modificado.py`

Este archivo implementa las **mejoras pedidas en la tarea**:

### 🔹 Cambios realizados
1. **Descenso de batería en cada movimiento**  
   Cada vez que el robot se mueve, la batería baja `-10`.  

2. **Bloqueo si la batería es 0**  
   Si intenta moverse sin batería, no se desplaza hasta recargar.  

3. **Nuevas recompensas y castigos**
   - Intentar moverse sin batería → `-5 puntos`.  
   - Alcanzar objetivo en menos de 5 pasos → `+20 puntos extra`.  

4. **Estrategias de movimiento**  
   Se prueban movimientos aleatorios y se observa cómo afectan la recompensa total.  

---

## ⚡ Mejora en la eficiencia

El código modificado mejora la eficiencia en comparación con el original en los siguientes aspectos:

1. **Gestión realista de batería**  
   - Antes la batería era solo "alta/baja".  
   - Ahora baja en intervalos de 10 y obliga al robot a planificar mejor los movimientos.  
   - 🔹 Evita que el robot desperdicie pasos innecesarios.  

2. **Restricción cuando no hay batería**  
   - Antes el robot se podía mover siempre.  
   - Ahora, si la batería está en 0, el robot no se mueve hasta recargar.  
   - 🔹 Esto elimina movimientos inútiles que no aportan al objetivo.  

3. **Recompensas y castigos optimizados**  
   - Intentar moverse sin batería → `-5` (castigo).  
   - Llegar en menos de 5 pasos → `+20` (bonus por eficiencia).  
   - 🔹 Promueve trayectorias más cortas y efectivas.  

4. **Mayor control del ambiente**  
   - Se agregaron contadores de pasos y batería precisa.  
   - 🔹 Esto permite medir mejor la eficiencia del comportamiento del robot.  

📌 **Conclusión:**  
El sistema pasa de un robot que se movía aleatoriamente sin restricciones a uno que **optimiza su ruta, gestiona batería y maximiza la recompensa total**, simulando un ambiente más realista y eficiente.

---

## ⚙️ Procedimiento realizado

1. Se creó un **repositorio en GitHub** llamado `TAREA01introIA`.  
2. Se clonó el repositorio en la PC con:
   ```bash
   git clone https://github.com/manuelibanez21/TAREA01introIA.git

