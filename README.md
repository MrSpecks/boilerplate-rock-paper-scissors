
# Rock Paper Scissors

## Overview

A Python implementation of the classic Rock Paper Scissors game featuring multiple AI opponents and a customizable player strategy. The project is designed for learning, experimentation, and testing AI strategies against various built-in bots.

## Purpose

- Practice and experiment with AI strategies for Rock Paper Scissors.
- Compete your custom player against several built-in bots.
- Run automated tests to validate your strategy's effectiveness.

## Main Functionality

- Play Rock Paper Scissors against different AI bots.
- Implement your own strategy in `RPS.py`.
- Run automated matches and view win rates.
- Interactive play mode for human vs bot.

## Installation & Prerequisites

- **Python 3.7+** is required.
- Recommended: Use a virtual environment.

```bash
git clone https://github.com/MrSpecks/boilerplate-rock-paper-scissors.git
cd boilerplate-rock-paper-scissors
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # (if you add dependencies)
```

## Running the Application

To run automated matches and see results:

```bash
python main.py
```

To play interactively against a bot, uncomment the relevant line in `main.py`:

```python
# play(human, abbey, 20, verbose=True)
```

## Testing

Unit tests are provided in `test_module.py`. To run all tests:

```bash
python test_module.py
```

Or, run tests automatically by uncommenting the last line in `main.py`.

## Main Features & Usage

- **Custom Player**: Implement your strategy in `RPS.py` (`player` function).
- **Built-in Bots**: Challenge `quincy`, `abbey`, `kris`, `mrugesh`, and `random_player` (see `RPS_game.py`).
- **Human Play**: Play interactively via the console.
- **Results**: Win rates and match statistics are printed after each run.

## Architecture & Key Modules

- `main.py`: Entrypoint for running matches and tests.
- `RPS_game.py`: Core game logic, bot implementations, and match runner.
- `RPS.py`: Your custom player strategy.
- `test_module.py`: Unit tests to validate your player against bots.

### Data Flow

- Each bot/player is a function that receives the opponent's previous move.
- The `play` function runs matches, tracks results, and prints statistics.

## Environment Variables & Configuration

- No environment variables required.
- Configuration is handled via code (e.g., number of games, verbose mode).

## Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Submit a pull request with a clear description.
4. Ensure your code passes all tests.

## License

This project is provided for educational purposes. If you wish to use or distribute it, please add your preferred license.
