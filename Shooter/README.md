# Shooter Game

A fast-paced 2D side-scrolling shooter built with Python and Pygame. This project combines platforming, combat, pickups, enemy AI, and multiple levels into a compact arcade-style action game.

## Overview

You play as a soldier who must move through three handcrafted levels, fight hostile enemies, collect supplies, and reach the exit portal. The game includes shooting, grenade attacks, health pickups, ammo drops, and an animated background that gives the level a polished arcade feel.

The final playable version is contained in `shooter_tut13.py`, which acts as the main game loop and scene manager for the experience.

## Features

- Side-scrolling platform gameplay
- Player movement with jumping, running, and shooting
- Enemy AI that patrols and attacks when the player is in range
- Weapon system with rifle bullets and grenade throws
- Health, ammo, and grenade pickups
- 3 playable levels with progression
- Start menu and restart screen
- Animated sprite-based characters and explosions
- Background layers and tile-based world design

## Gameplay

The player starts in a menu screen, then enters the first level. The objective is to survive enemy encounters, gather items, and reach the level exit. Each level introduces a slightly different layout and challenge.

### Core mechanics

- Move left and right to navigate the level
- Jump over hazards and reach higher platforms
- Fire bullets to defeat enemies
- Throw grenades when facing crowded or dangerous situations
- Pick up health, ammo, and grenade crates for support
- Advance to the next stage by reaching the exit gate

## Controls

| Action | Key |
| --- | --- |
| Move left | A |
| Move right | D |
| Jump | W |
| Shoot | Space |
| Throw grenade | Q |
| Exit game | Esc |

## Requirements

- Python 3.9+
- Pygame

## Installation

1. Open a terminal in the project folder.
2. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
```

3. Activate the virtual environment:

On Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

4. Install the dependency:

```bash
pip install pygame
```

5. Run the game:

```bash
python shooter_tut13.py
```

## Project Structure

```text
Shooter/
├── audio/                  # Sound effects and music
├── img/                   # Sprites, tiles, UI assets, animations
├── button.py              # Reusable button UI class
├── level1_data.csv        # Level 1 layout data
├── level2_data.csv        # Level 2 layout data
├── level3_data.csv        # Level 3 layout data
├── shooter_tut13.py       # Main game file
├── README.md              # Project documentation
└── .gitignore             # Git ignore configuration
```

## How the game is organized

- `shooter_tut13.py` contains the main loop, game state, background rendering, animations, levels, input handling, and player/enemy logic.
- `button.py` handles clickable start, exit, and restart buttons.
- `level*_data.csv` files store the tile map layouts for each stage.
- `img/` and `audio/` provide all artwork and sound assets.

## Notes

This project is structured as a beginner-friendly Pygame shooter and is a good example of: 

- sprite-based game development
- tile map level design
- input handling and state management
- object collisions and enemy logic
- simple UI overlays and menus

## License

This project is intended for educational and personal use. If you are using it for a portfolio, learning project, or modification, feel free to adapt it as needed.

## Acknowledgements

This game follows a classic Pygame side-scroller style and was built using free sprite assets, sound effects, and programming patterns commonly used in simple arcade games.

## Future Ideas

- Add boss fights
- Introduce score and timer systems
- Add mobile controls or keyboard remapping
- Expand the level count and enemy variety


---

Enjoy the game and happy coding!
