def stats(match_score:str, player_stats:str) -> dict:
	match_won, match_lost = map(int, match_score.split('-'))
	kills, deaths, assists = map(int, player_stats.split('-'))

	total_rounds = match_won + match_lost

	kd = kills / deaths if deaths != 0 else kills
	kr = kills / total_rounds
	survival_rate = round(((deaths / total_rounds)*100), 3)

	result = {
	'kd': kd,
	'kr': kr,
	'assists' : assists,
	'survival_rate':survival_rate
	}


	return result

print(stats("13-10", "25-0-5"))
