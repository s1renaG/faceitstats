import random
class RandomGenerator:
    def random_library(self):
        randomizer = random.sample(range(0, 50), 30)
        return randomizer

    def stat_library(self) -> dict:
        randomizer = self.random_library()
        w = randomizer[0]
        l = randomizer[1]
        k = randomizer[2]
        a = randomizer[3]
        d = randomizer[4]
        return {'w': w, 'l': l, 'k': k, 'a': a, 'd': d}

random_gen = RandomGenerator()
player_stats = f'{random_gen.stat_library()["k"]}-{random_gen.stat_library()["a"]}-{random_gen.stat_library()["d"]}'
match_score = f'{random_gen.stat_library()["w"]}-{random_gen.stat_library()["l"]}'
def stats(match_score:str, player_stats:str) -> dict:
  team1_score, team2_score = map(int, match_score.split('-'))
  kills, assists, deaths = map(int, player_stats.split('-'))
  total_rounds = team1_score + team2_score
  kd = kills / deaths if deaths != 0 else kills
  kr = kills / total_rounds
  survival_rate = deaths / total_rounds if deaths != 0 else 0
  result = {
  'kd': kd,
  'kr': kr,
  'assists' : assists,
  'survival_rate':survival_rate
  }

  with open("results.txt","a") as file:
    file.write(str(result))
  print(result)
  return
random_stats = stats(match_score, player_stats)
for _ in range(10):
  player_stats = f'{random_gen.stat_library()["k"]}-{random_gen.stat_library()["a"]}-{random_gen.stat_library()["d"]}'
  match_score = f'{random_gen.stat_library()["w"]}-{random_gen.stat_library()["l"]}'
  stats(match_score, player_stats)
