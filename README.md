# Interactive Hand Cricket (Python)

A console-based Hand Cricket game built in Python featuring both classic rules and a custom high-stakes **Crazy Mode**.

## Game Modes
- **Normal Mode:** Classic Hand Cricket rules—matching the bowler's number dismisses the batsman; otherwise, the batsman scores the number chosen.
- **Crazy Mode:** A custom twist with higher risk and higher scoring:
  - **Squared Runs:** Matching the bowler's number squares the batsman's chosen runs instead of causing a dismissal.
  - **±1 Dismissal Rule:** To get the batsman out, the bowler must pick a number that is 1 higher or 1 lower than the batsman's choice (e.g., if the batsman plays `9`, the bowler dismisses them with `8` or `10`).

## Features
- **Toss System:** Odd/Even toss mechanic to decide batting or bowling first.
- **Full Innings Gameplay:** Dynamic switching between innings with automatic target chase tracking.
- **AI Opponent:** Randomized move selection for bowling and batting.
- **Input Validation:** Handles invalid inputs cleanly without breaking the game loop.

## How to Run
1. Ensure Python 3 is installed on your system.
2. Run the script in your terminal:
   ```bash
   python hand_cricket.py
