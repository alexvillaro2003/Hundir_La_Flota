# 🚢 **Hundir la Flota** 🎯

¡Bienvenido a **Hundir la Flota**, el clásico juego de estrategia naval desarrollado en **Python**! 🎉 Prepárate para desafiar a la máquina, hundir sus barcos y demostrar tu habilidad estratégica.

---

## 🌟 **Descripción del Proyecto**

Este proyecto recrea el famoso juego de mesa "Hundir la Flota" (o "Battleship") en un entorno interactivo por consola. El jugador y la máquina colocan sus barcos en un tablero, y ambos intentan hundir la flota rival disparando en posiciones específicas.

El juego incluye:

- **Tableros personalizados:** El jugador puede ver su tablero con los barcos y el progreso de los disparos hacia la máquina.
- **Máquina con IA básica:** Dispara aleatoriamente al tablero del jugador.
- **Sistema de turnos:** Alterna entre el jugador y la máquina hasta que uno de los dos gane.
- **Indicadores visuales claros:**
  - **'O':** Barcos en tu tablero.
  - **'X':** Barcos tocados.
  - **'A':** Agua (disparos fallidos).

---

## 🛠️ **Tecnologías Utilizadas**

El proyecto utiliza exclusivamente **Python 3.x** y las siguientes librerías estándar:

- **`numpy`**: Para crear y gestionar los tableros como matrices.
- **`random`**: Para generar posiciones aleatorias de barcos y disparos de la máquina.
- **`time`**: Para simular pausas entre turnos y mejorar la experiencia de juego.

---

## 🎮 **Cómo Jugar**

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tuusuario/hundir-la-flota.git
   cd hundir-la-flota
   ```

2. Ejecuta el archivo main.py:

   ```bash
   python main.py
   ```

3. ¡Sigue las instrucciones en la consola y disfruta del juego!

---

## ⚓ **Reglas del Juego**

1. **Inicio:**

   - Ambos jugadores colocan barcos automáticamente en tableros de 10x10.
   - Los barcos tienen tamaños de **2, 3 y 4 casillas**.

2. **Turnos:**

   - Elige quién dispara primero: jugador o máquina.
   - Introduce coordenadas para disparar a los barcos enemigos (ejemplo: fila = 2, columna = 3).
   - Los disparos acertados marcan **'X'** y los fallidos **'A'**.

3. **Victoria:**
   - Gana el primer jugador en hundir todos los barcos del oponente.

---

## 📂 **Estructura del Proyecto**

```plaintext
hundir-la-flota/
│
├── utils.py         # Lógica principal del juego (tableros, disparos, IA)
├── main.py          # Flujo principal para iniciar la partida
└── README.md        # Documentación del proyecto
```

---

## 🏆 **Autor**

Proyecto desarrollado por Alejandro Villarreal Rodríguez.
Si tienes ideas para mejorar este proyecto o simplemente quieres conectar, ¡escríbeme! 📧
