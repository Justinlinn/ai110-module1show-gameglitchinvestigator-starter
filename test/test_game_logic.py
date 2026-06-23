"""Tests targeting the specific logic bugs fixed in logic_utils.py."""

from logic_utils import check_guess, update_score, get_range_for_difficulty


# --- Bug 1: high/low hints were reversed ---

def test_too_high_guess_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_guess_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_exact_guess_wins():
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


# --- Bug 2: scoring was asymmetric (a wrong guess could ADD points) ---

def test_wrong_guess_always_loses_points():
    # "Too High" used to gain +5 on even attempts; now every wrong guess loses 5.
    assert update_score(50, "Too High", attempt_number=2) == 45
    assert update_score(50, "Too High", attempt_number=3) == 45
    assert update_score(50, "Too Low", attempt_number=4) == 45


# --- Bug 3: New Game used the wrong range; the range source must match difficulty ---

def test_range_matches_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)
