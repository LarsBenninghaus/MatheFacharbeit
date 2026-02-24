from roulette import Bet, Game

bet = Bet()
bet.addBet(money=250, betType=17)
bet.addBet(money=20, betType="Black")

print(Game.simulate(bet))

