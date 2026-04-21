# League Ranking Table — Setup & Usage

## Requirements

- Python 3.7+
- `pytest` (for running tests)

Verify your Python version:

```bash
python3 --version
```

---

## Project Structure

```
league/
├── league_rankings.py        # Main application
└── test_league_rankings.py   # Test suite
```

---

## Installation

No external dependencies are required to run the app itself. To install the test runner:

```bash
pip3 install pytest
```

---

## Running the Application

### Option 1 — Via stdin

```bash
echo "Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0" | python3 league_rankings.py
```

### Option 2 — Via input file

```bash
python3 league_rankings.py input.txt
```

Where `input.txt` contains one match result per line, e.g.:

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0
```

### Expected Output

```
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
```

### Option 3 — Make it executable (optional)

```bash
chmod +x league_rankings.py
./league.py input.txt
```

---

## Running Tests

```bash
pytest test_league_rankings.py -v
```

### Expected test output

```
test_league.py::test_sample_output          PASSED
test_league.py::test_draw                   PASSED
test_league.py::test_win_loss               PASSED
test_league.py::test_alphabetical_tiebreak  PASSED
test_league.py::test_singular_pt_label      PASSED
test_league.py::test_empty_input            PASSED
```

---

## Scoring Rules

| Result | Points |
|--------|--------|
| Win    | 3 pts  |
| Draw   | 1 pt   |
| Loss   | 0 pts  |

- Teams with equal points share the same rank.
- Tied teams are listed in alphabetical order.
- `1 pt` (singular) is used when a team has exactly 1 point; `pts` otherwise.
