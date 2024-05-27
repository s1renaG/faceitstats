from demoparser2 import DemoParser
import pandas as pd
import glob
pd.set_option('display.max_rows', 500)

parser = DemoParser("/Users/vitaliy/Documents/demoscraper/faceitgames/lazerdogs.dem")

df = parser.parse_event("player_death", player=["last_place_name", "team_name"], other=["total_rounds_played", "is_warmup_period"])

df = df[df["attacker_team_name"] != df["user_team_name"]]
df = df[df["is_warmup_period"] == False]

df = df.groupby(["total_rounds_played", "attacker_name"]).size().to_frame(name='total_kills').reset_index()
