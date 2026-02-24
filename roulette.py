import random #Bibliotek für Zufälle
import pandas as pd

class Roulette:
    _instance = None

    def __init__(self) -> None:
        self.payouts = {
            # Einfache Chancen (1:1)
            "Red": 1,
            "Black": 1,
            "Even": 1,
            "Odd": 1,
            "Low": 1,
            "High": 1,

            # Dutzende & Kolonnen (2:1)
            "Dozen 1": 2,
            "Dozen 2": 2,
            "Dozen 3": 2,
            "Column 1": 2,
            "Column 2": 2,
            "Column 3": 2,
        }

        self.numbers = []
        for i in range(37):
            self.numbers.append(i)
        
        self.red = [
            1, 3, 5, 7, 9,
            12, 14, 16, 18,
            19, 21, 23, 25,
            27, 30, 32, 34, 36
        ]

        self.black = []
        for i in self.numbers:
            if((i not in self.red) and (i != 0)):
                self.black.append(i)

        self.column_1 = [
            1, 4, 7, 10, 13, 16,
        19, 22, 25, 28, 31, 34
        ]

        self.column_2 = [
            2, 5, 8, 11, 14, 17,
            20, 23, 26, 29, 32, 35
        ]

        self.column_3 = [
            3, 6, 9, 12, 15, 18,
            21, 24, 27, 30, 33, 36
        ]

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Roulette, cls).__new__(cls)
        return cls._instance

class Bet():
    def __init__(self, betData={}):
        if betData != None:
            self.__listData = betData
        else:
            self.__listData = {}
        self.__numberBets = 0
        self.__roulette = Roulette()
        
    
    def __str__(self) -> str:
        ret = "Du hast auf "

        for i in self.__listData:
            ret = ret + str(i) + " mit " + str(self.__listData[i]) + "€" 
            if i != self.__numberBets:
                ret = ret + ", "
        
        return ret
    
    def payout(self, listWin) -> tuple: #Nimmt Liste, welche Wetten gewonnen haben, und gibt gewonnenes Geld zurück
        payout = 0
        for win in listWin:
            if win in self.__listData:
                if win in self.__roulette.payouts:
                    payout += self.__listData[win] * (self.__roulette.payouts[win]+1)
                else: 
                    payout += self.__listData[win] * 36
        
        return payout
    
    def addBet(self, money, betType) -> None:
        self.__numberBets += 1
        
        self.__listData[betType] = money
    
    def clear(self):
        self.__listData = {}
    


class Game():
    def __init__(self):
        self.count_real = 0
    
    def __str__() -> str:
        return ""

    def simulate(bet) -> int:
        roulette = Roulette()
        simulatedNumber = random.choice(roulette.numbers)
        listWin = [simulatedNumber]

        if(simulatedNumber<=12 and simulatedNumber != 0):
            listWin.append("Dozen 1")
        if(simulatedNumber>12 and simulatedNumber<=24):
            listWin.append("Dozen 2")
        if(simulatedNumber>24):
            listWin.append("Dozen 3")
        if(simulatedNumber in roulette.red):
            listWin.append("Red")
        if(simulatedNumber in roulette.black):
            listWin.append("Black")
        if(simulatedNumber%2==0 and simulatedNumber != 0):
            listWin.append("Even")   
        if(simulatedNumber%2!=0 and simulatedNumber != 0):
            listWin.append("Odd")      
        if(simulatedNumber>18 and simulatedNumber != 0):
            listWin.append("High")
        if(simulatedNumber<=18 and simulatedNumber != 0):
            listWin.append("Low")
        if(simulatedNumber in roulette.column_1):
            listWin.append("Column 1")
        if(simulatedNumber in roulette.column_2):
            listWin.append("Column 2")
        if(simulatedNumber in roulette.column_3):
            listWin.append("Column 3")

        return bet.payout(listWin)

        
    def simulate_list():
        roulette = Roulette()
        simulatedNumber = random.choice(roulette.numbers)
        listWin = [simulatedNumber]

        if(simulatedNumber<=12 and simulatedNumber != 0):
            listWin.append("Dozen 1")
        elif(simulatedNumber>12 and simulatedNumber<=24):
            listWin.append("Dozen 2")
        elif(simulatedNumber>24):
            listWin.append("Dozen 3")
        else:
            listWin.append(0)
        if(simulatedNumber in roulette.red):
            listWin.append("Red")
        elif(simulatedNumber in roulette.black):
            listWin.append("Black")
        else:
            listWin.append(0)
        if(simulatedNumber%2==0 and simulatedNumber != 0):
            listWin.append("Even")   
        elif(simulatedNumber%2!=0 and simulatedNumber != 0):
            listWin.append("Odd") 
        else:
            listWin.append(0)     
        if(simulatedNumber>18 and simulatedNumber != 0):
            listWin.append("High")
        elif(simulatedNumber<=18 and simulatedNumber != 0):
            listWin.append("Low")
        else:
            listWin.append(0)
        if(simulatedNumber in roulette.column_1):
            listWin.append("Column 1")
        elif(simulatedNumber in roulette.column_2):
            listWin.append("Column 2")
        elif(simulatedNumber in roulette.column_3):
            listWin.append("Column 3")
        else:
            listWin.append(0)
        
        return listWin

    def simulate_real(self, path, bet):
        df = pd.read_csv(path,sep=';')


        roulette = Roulette()
        simulatedNumber = df["Zahl"][self.count_real]
        self.count_real += 1
        listWin = [simulatedNumber]

        if(simulatedNumber<=12 and simulatedNumber != 0):
            listWin.append("Dozen 1")
        if(simulatedNumber>12 and simulatedNumber<=24):
            listWin.append("Dozen 2")
        if(simulatedNumber>24):
            listWin.append("Dozen 3")
        if(simulatedNumber in roulette.red):
            listWin.append("Red")
        if(simulatedNumber in roulette.black):
            listWin.append("Black")
        if(simulatedNumber%2==0 and simulatedNumber != 0):
            listWin.append("Even")   
        if(simulatedNumber%2!=0 and simulatedNumber != 0):
            listWin.append("Odd")      
        if(simulatedNumber>18 and simulatedNumber != 0):
            listWin.append("High")
        if(simulatedNumber<=18 and simulatedNumber != 0):
            listWin.append("Low")
        if(simulatedNumber in roulette.column_1):
            listWin.append("Column 1")
        if(simulatedNumber in roulette.column_2):
            listWin.append("Column 2")
        if(simulatedNumber in roulette.column_3):
            listWin.append("Column 3")

        return bet.payout(listWin)

    def martingal(self, numberGames, bet_start, path="", budget=0, ignoreBudget=False, real=False) -> pd.DataFrame:
        counter = 1
        df = pd.DataFrame(columns=["Money"])
        while((budget >= 0 or ignoreBudget) and counter<=numberGames):
            win = False

            money = bet_start
            if not ignoreBudget and money>=budget:
                money = budget

            budget -= money
    
            while win == False:
                bet = Bet()
                bet.addBet(money=money, betType="Black") 

                if real:
                    profit = self.simulate_real(path=path, bet=bet)
                else:
                    profit = Game.simulate(bet)

                if profit>0:
                    budget += profit
                    win = True
                else:
                    money *= 2
                
                    if not ignoreBudget and money>=budget:
                        break

                    budget -= money
                
                df.loc[len(df)] = [budget]
                counter += 1

        return df


    def alambert(self, numberGames, betStart, unit, path = "", budget=0, ignoreBudget=True, real=False) -> pd.DataFrame:
        df = pd.DataFrame(columns=["money"])
        money = betStart
        counter=1

        while (budget>=0 or ignoreBudget) and counter<numberGames:
            df.loc[len(df)] = [budget]
            bet = Bet()
            bet.addBet(money, "Black")
            
            if real:
                profit = self.simulate_real(path,bet)
            else:
                profit = Game.simulate(bet)

            if profit>0:
                budget += profit
                if money>unit: 
                    money -= unit
                else: 
                    money=unit
            else:
                money += unit

            budget -= money 
            counter += 1

        return df