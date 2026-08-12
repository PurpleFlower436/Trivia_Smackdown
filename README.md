# Trivia_Smackdown

This is a single player Python trivia game played in GitHub Codespaces. Each player chooses from four categories (Marvel, History, Disney World, Pop Culture) and an easy or hard difficulty, then answers five questions per round. After each round, players can choose to continue with a new category/difficulty or quit and see their final scores and the winner. 


Here is a demo of Trivia Smackdown being played in GitHub Codespaces. 

<img width="900" alt="Trivia_Smackdown_demo" src="https://github.com/user-attachments/assets/cd06e04c-9f26-4075-89c1-62d9c01d6a33" />





![Python Badge](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Commit Activity](https://img.shields.io/github/commit-activity/m/PurpleFlower436/Trivia_Smackdown)
![GitHub last commit](https://img.shields.io/github/last-commit/PurpleFlower436/Trivia_Smackdown)
[![Python application](https://github.com/PurpleFlower436/Trivia_Smackdown/actions/workflows/python-app.yml/badge.svg)](https://github.com/PurpleFlower436/Trivia_Smackdown/actions/workflows/python-app.yml)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/PurpleFlower436/Trivia_Smackdown)


## Features
- Single-player terminal-based game in Python
- Category and difficulty selection for each player
- Scoring system that tracks correct answers
- Basic input validation and game flow control
- Two computer opponents with easy and medium difficulty modes
- Persistent leaderboard for storing and displaying final scores using SQLAlchemy
- Automated testing and deployment through GitHub Actions CI/CD
- Deployed for easy access and review through GitHub Codespaces


## Tech Stack
- Python 3
- SQLite
- Pytest
- GitHub Actions
- GitHub Codespaces

## How to Run
1. Click on the Open in GitHub Codespaces badge. 
2. Click Create Codespace.
3. Run:
   python3 -m src.trivia_v2


## What I Implemented
- Game loop and user input flow for player
- Scoring and category-selection logic
- Tested the game by playing it repeatedly to debug issues and ensure correct game flow and results
- Wrote 19 Pytest unit tests covering input validation, answer checking, scoring, and winner logic
- Added two AI computer bots using randomized and probabilistic decision logic
- Integrated SQLite to persist and display leaderboard data
- Configured GitHub Actions to automate testing and deployment workflows
