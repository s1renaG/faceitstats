import random


class RandomGenerator:
  def random_library(self):
    return random.sample(range(0, 50), 5)
    
  def stats(self, w, l, k, a, d):
    total_rounds = w + l
    kd = k / d if d != 0 else k
    kr = k / total_rounds
    assists = a
    survival_rate = d / total_rounds if d != 0 else 0
    result = {
      'kd': kd,
      'kr': kr,
      'assists' : assists,
      'survival_rate':survival_rate
      }
    return {'kd': kd, 'kr': kr, 'assists': assists, 'survival_rate': survival_rate}
random_gen = RandomGenerator()
with open("results.cvs", "w") as file:
  for _ in range(4):
      w, l, k, a, d = random_gen.random_library()
      stats_result = random_gen.stats(w, l, k, a, d)
      file.write(f"Stats: {stats_result}\n")
