def stats(match_score:str, player_stats:str) -> dict:
  team1, team2 = map(int, match_score.split('-'))
  k, d = map(int,player_stats.split('-'))
  rounds = team1 + team2
  kd = k / d
  kr = k / rounds
  survival_rate = (team1 / rounds) * 100
  return {'kd': kd,'kr': kr,'survival_rate': survival_rate}

match_score, player_stats = "13-11", "25-10"
result = stats(match_score, player_stats)
print(result)

