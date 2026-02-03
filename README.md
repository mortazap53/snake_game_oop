### snake_game_oop
It is the famous snake game that all of you may have heard. I build this project using the oop object-oriented programming in python in order to make it reusable and be an easy changeable project. Simple to change logic and other things you want to change. 

### more explaination:



---

##  Features

- Smooth snake movement
- Random food spawning
- Snake growth after eating food
- Live score tracking
- Wall collision detection
- Self-collision detection
- Game over display
- Modular and readable code structure

---

##  Concepts Used

This project demonstrates core programming and game-development concepts:

- Object-Oriented Programming (OOP)
- Class design and responsibility separation
- Game loop control
- Keyboard event handling
- Coordinate-based movement
- Collision detection using distance calculation
- Screen refresh optimization using `tracer()`

---

##  Project Structure

snake-game/
│
├── main.py # Main game loop and screen setup
├── snake.py # Snake creation, movement, and growth logic
├── food.py # Food behavior and random placement
├── score.py # Score tracking and game-over display
└── README.md # Project documentation

---

## Controls
Key	Action
W	Move Up
S	Move Down
A	Move Left
D	Move Right

---

## Game Logic Overview
Snake Movement

The snake body moves from tail to head, with each segment copying the position of the segment in front of it.
The head moves forward after all body segments update.
This prevents overlapping and ensures smooth movement.

---

## Food Collision
When the snake head is close enough to the food:
The food moves to a new random location
A new snake segment is added
The score increases

---

## Game Over Conditions
Snake hits the wall
Snake collides with its own body

---

## Code Quality Highlights
Clear separation of concerns (each class has a single responsibility)
Consistent use of data types for positions
Clean and readable method structure
Easy to extend and maintain
Beginner-friendly but professionally structured

---
 
## Author
Mortaza Panahi

This project was built to strengthen understanding of my own objective are:
* Python fundamentals
* Object-Oriented Programming
* Game logic and debugging
* Clean code practices
