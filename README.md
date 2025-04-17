# Akinator_Python
A simple Python guessing game where the program tries to guess the animal you're thinking of by asking yes/no questions. The game learns new animals and questions based on your answers.

🐾 Simple Animal Akinator in Python

This project is a small **animal guessing game** written in Python.  
The player thinks of an animal, and the program tries to guess it by asking yes/no questions.

---

💡 How it works

- The game starts with a basic question:  
  **"Does your animal like bananas?"**
- If the answer is **yes**, it guesses the animal is a **monkey**.
- If the answer is **no**, the game asks:
  - What animal were you thinking of?
  - What question would differentiate that animal from the previous one?
- The new question and answer are added to the list, so the game **learns** with every round.

---

🧠 Core logic

- A list of questions and animals (`perguntas`) is used as memory.
- In each round, the game loops through the list to try to guess correctly.
- If it fails, it asks the user for a new animal and a custom question, then adds it to the list.

---

📦 Requirements

- Python 3.x
