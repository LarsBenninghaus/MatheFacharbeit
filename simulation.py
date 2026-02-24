from roulette import Game, Bet
import pandas as pd

count = 0
df = pd.DataFrame(columns=["Zahl", "Dozen", "Black/Red", "Even/Odd", "High/Low", "Column"])

while(count <= 10000):
    df.loc[len(df)]=Game.simulate_list()
    count += 1

print(df.head(5))
df.to_csv("./Data/RouletteStatistiken_simuliert3.csv")