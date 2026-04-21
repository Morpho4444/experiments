import subprocess

SAMPLE = """Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0"""

def run(input_str):
    result = subprocess.run(
        ["python3", "league_rankings.py"],
        input=input_str, capture_output=True, text=True
    )
    return result.stdout.strip()

def test_sample_output():
    expected = (
        "1. Tarantulas, 6 pts\n"
        "2. Lions, 5 pts\n"
        "3. FC Awesome, 1 pt\n"
        "3. Snakes, 1 pt\n"
        "5. Grouches, 0 pts"
    )
    assert run(SAMPLE) == expected

def test_draw():
    assert "1 pt" in run("A 1, B 1")

def test_win_loss():
    out = run("A 2, B 0").splitlines()
    assert out[0].startswith("1. A, 3 pts")
    assert out[1].startswith("2. B, 0 pts")

def test_alphabetical_tiebreak():
    out = run("Zebra 1, Apple 1")
    assert out.index("Apple") < out.index("Zebra")

def test_singular_pt_label():
    assert "1 pt" in run("Solo 1, Other 1")

def test_empty_input():
    assert run("") == ""