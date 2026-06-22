from logic_utils import check_guess, get_hint, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- New tests targeting the bugs fixed in Phase 2 ---

def test_too_high_hint_tells_player_to_go_lower():
    # Bug 1 fix: a guess that is too high must tell the player to go LOWER.
    outcome = check_guess(60, 50)
    assert "LOWER" in get_hint(outcome)

def test_too_low_hint_tells_player_to_go_higher():
    # Bug 1 fix: a guess that is too low must tell the player to go HIGHER.
    outcome = check_guess(40, 50)
    assert "HIGHER" in get_hint(outcome)

def test_wrong_guess_never_increases_score():
    # Bug 2 fix: a wrong guess always costs 5 points, regardless of attempt
    # parity. The starter added 5 for "Too High" on even attempts.
    assert update_score(100, "Too High", 2) == 95   # even attempt
    assert update_score(100, "Too High", 3) == 95   # odd attempt
    assert update_score(100, "Too Low", 2) == 95
