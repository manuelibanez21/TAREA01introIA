\# 🤖 Tarea 01 - Introducción a Inteligencia Artificial



Este repositorio contiene la implementación de la \*\*Tarea 01\*\* de la asignatura \*\*Introducción a la IA\*\*.  

El ejercicio consiste en simular un robot en una cuadrícula que tiene una batería limitada y recibe recompensas o penalizaciones según sus acciones.



---



\## 📌 Requerimientos de la tarea



1\. \*\*Modificar la función `mover\_robot` para que la batería baje en cada movimiento.\*\*

2\. \*\*Si la batería llega a 0, el robot no se puede mover hasta recargar.\*\*

3\. \*\*Añadir más recompensas o castigos:\*\*

&nbsp;  - Castigo por intentar moverse sin batería (\*\*-5 puntos\*\*).

&nbsp;  - Bonus por llegar al objetivo rápido (\*\*+20 puntos si lo logra en menos de 5 pasos\*\*).

4\. \*\*Probar diferentes estrategias de movimiento para maximizar la recompensa.\*\*



---



\## ⚙️ Implementación



\### 🔹 Estado del robot

El robot tiene:

\- Una \*\*posición\*\* en una cuadrícula 3x3.

\- Una \*\*batería\*\* (100 al inicio).

\- Un indicador de si alcanzó el \*\*objetivo\*\*.

\- Un contador de \*\*pasos dados\*\*.



Ejemplo de estado inicial:

```python

estado\_robot = {

&nbsp;   "posicion": (0, 0),

&nbsp;   "bateria": 100,

&nbsp;   "objetivo\_alcanzado": False,

&nbsp;   "pasos": 0

}



