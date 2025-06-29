# 🎯 Number Guessing Game - Django Web App

A web-based Number Guessing Game built with **Python** and **Django**, where players guess a randomly generated number based on chosen difficulty. 
It’s a fun and interactive way to apply Django concepts like sessions, views, and templates.

---

## 📚 Table of Contents

- [🧠 About the Project](#about-the-project)
- [🎮 Game Features](#game-features)
- [🛠️ Tech Stack](#tech-stack)
- [⚙️ Setup Instructions](#setup-instructions)
- [🕹️ How to Play](#how-to-play)
- [📁 Folder Structure](#folder-structure)
- [🤝 Contributing](#contributing)
- [📝 License](#license)

---

## 🧠 About the Project

This project is a classic Number Guessing Game where:
- A number is randomly selected by the system.
- You pick a difficulty level (Easy/Medium/Hard).
- You guess the number within a limited number of attempts.
- Feedback is given for each guess: too low, too high, or correct.
- Everything is managed with Django views, templates, and sessions.

---

## 🎮 Game Features

- 🎚️ Difficulty Levels:
  - Easy (1–50, 10 attempts)
  - Medium (1–100, 7 attempts)
  - Hard (1–150, 5 attempts)
- 🔁 Session-based game state management
- ⚡ Instant feedback on guesses
- 📱 Responsive web UI
- ♻️ Replay option after game ends

---

## 🛠️ Tech Stack

| Tech         | Usage                  |
|--------------|------------------------|
| Python       | Core programming       |
| Django       | Web framework          |
| HTML/CSS     | Frontend templates     |
| SQLite       | Default Django DB      |

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/your-username/number-guess-game.git
cd number-guess-game

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver
