# Video Game Collection Manager

A Python command-line application for managing a personal video game collection.

## Features

- Add and remove games
- View all games
- Search for games by name
- Mark games as finished
- Rate games from 1–10
- Filter games by platform
- View finished and unfinished games
- Sort games alphabetically
- Prevent duplicate game entries
- Save and load collection data using JSON
- Validate user input

## Project Structure

- `main.py` — Handles the menu and user input
- `game_manager.py` — Manages the game collection and JSON save/load
- `video_game.py` — Defines the `VideoGame` class and individual game behavior
- `games.json` — Stores saved game data

## How to Run

Make sure Python 3 is installed.

Run:

```bash
python3 main.py
```

## Technologies

- Python
- Object-Oriented Programming
- JSON
- File I/O
