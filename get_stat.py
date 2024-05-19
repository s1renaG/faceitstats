def stats(match_score:str, player_stats:str) -> dict:
  team1_score, team2_score = map(int, match_score.split('-'))
  kills, deaths, assists = map(int, player_stats.split('-'))

  total_rounds = team1_score + team2_score

  kd = kills / deaths if deaths != 0 else kills
  kr = kills / total_rounds
  survival_rate = deaths/total_rounds

  result = {
  'kd': kd,
  'kr': kr,
  'assists' : assists,
  'survival_rate':survival_rate
  }

  with open("results.txt","w") as file:
    file.write(str(result))
  return

print(stats("13-10", "25-0-5"))

