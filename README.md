# Python Terminal RPG

A turn-based RPG built in Python for the terminal.  
This project was created to practice object-oriented programming, software architecture and game system design.

The game is structured in a modular way, separating the game engine, characters, abilities and interface.

---

## Features

- Turn-based combat system
- Character and enemy classes
- Ability system
- Inventory system
- Item system
- Colored terminal interface
- Modular architecture

---

## Project Structure

PythonProject-rpg2
│
├── engine
│ ├── combate.py
│ ├── personagem.py
│ ├── inventario.py
│ ├── item.py
│
├── habilidades
│ ├── habilidade_base.py
│ ├── habilidades_comuns.py
│
├── personagens
│ ├── heroi
│ └── inimigo
│
├── interface
│ └── menu_combate.py
│
├── utils
│ ├── cores.py
│ └── atalhos.py
│
└── main.py

yaml
Copiar código

---

## How the Game Works

The game follows a simple turn-based combat flow:

Start Game
↓
Create Characters
↓
Combat Menu
↓
Player Turn
↓
Enemy Turn
↓
Check Victory or Defeat

yaml
Copiar código

Players can:

- Attack enemies
- Use abilities
- View ability descriptions
- Fight until one side is defeated

---

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- Modular software architecture

---

## Purpose of the Project

This project was built to improve skills in:

- Object-oriented programming
- Code organization
- Software architecture
- Game logic design

---

## Future Improvements

Planned features for future versions:

- Mana system for abilities
- Ability cooldowns
- Different enemy types
- Experience and leveling system
- Weapon abilities
- AI improvements for enemies

---

## Author

Adriano Laguiosta
