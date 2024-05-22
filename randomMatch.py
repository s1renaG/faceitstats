import random


def simulate_cs2_match():
    team1 = 0
    team2 = 0

    while team1 < 16 and team2 < 16:
        if random.random() > 0.5:
            team1 += 1
        else:
            team2 += 1

    return team1, team2
team1, team2 = simulate_cs2_match()
print(f"CS:GO Match Score: {team1} - {team2}")
