from Models.Aggregables.Regions import Regions
from Models.Aggregables.Risks import Risks
from Models.Aggregables.Sector import Sector
from Models.Aggregables.Strategy import Strategy
from Models.LimitedPartner import *
from machine_learning.ml import *
import pandas as pd


def main(arg):
    print("Welcome to Scribe Company Recommendation tool. This is a rudimentary tool for recommending you which "
          "companies to invest in based on a series of factors using machine learning. ")
    print("We will generate and train our model based on your input parameters. ")

    d = pd.read_csv("../Models/companies.csv")
    mach = ml(d, arg)
    mach.train_ml()

    value = ""

    while value.lower() != "exit":
        value = input("What is your name?\n")
        LimitedPartner.name = value

        try:
            value = int(input("What is your Available Investment?\n"))
            if value < 100000:
                print("Sorry not enough funds!")
                break
            elif 100000 <= value < 500000:
                LimitedPartner.fundsize = 100000
            elif 500000 <= value < 1000000:
                LimitedPartner.fundsize = 500000
            elif 1000000 <= value < 25000000:
                LimitedPartner.fundsize = 1000000
            elif 25000000 <= value < 1000000000:
                LimitedPartner.fundsize = 25000000
            elif value >= 1000000000:
                LimitedPartner.fundsize = 1000000000
            else:
                print("Sorry wrong input!")
                break
        except:
            print("Sorry wrong input!")

        value = input("What is your preferred sector? \nAvailable sectors as of today: MILITARY, FOOD, PHARMA, FINANCE, TECH, CONSUMER\n")
        if value == "MILITARY":
            sector_val = 0
        elif value == "FOOD":
            sector_val = 1
        elif value == "PHARMA":
            sector_val = 2
        elif value == "FINANCE":
            sector_val = 3
        elif value == "TECH":
            sector_val = 4
        elif value == "CONSUMER":
            sector_val = 5
        else:
            print("Sorry wrong input!")
            break

        value = input("What is your strategy? \nAvailable strategies as of today: DISTRESSED, GROWTH, INDUSTRY_FOCUSED, VENTURE_CAPITAL, MIDDLE_BUYOUT, LARGE_BUYOUT\n")
        if value == "DISTRESSED":
            strategy_val = 0
        elif value == "GROWTH":
            strategy_val = 1
        elif value == "INDUSTRY_FOCUSED":
            strategy_val = 2
        elif value == "VENTURE_CAPITAL":
            strategy_val = 3
        elif value == "MIDDLE_BUYOUT":
            strategy_val = 4
        elif value == "LARGE_BUYOUT":
            strategy_val = 5
        else:
            print("Sorry wrong input!")
            break

        value = input("What is your risk? \nAvailable risks as of today: None, Low, Medium Low, Medium, Medium High, High\n")
        if value == "None":
            risk_val = 0
        elif value == "Low":
            risk_val = 1
        elif value == "Medium Low":
            risk_val = 2
        elif value == "Medium":
            risk_val = 3
        elif value == "Medium High":
            risk_val = 4
        elif value == "High":
            risk_val = 5
        else:
            print("Sorry wrong input!")
            break
        LimitedPartner.risk = value

        value = input("What is your region of preference? \nAvailable regions as of today: NORTH_AMERICA, SOUTH_AMERICA, ASIA, ANTARTICA, AFRICA, EUROPE, AUSTRALIA\n")
        if value == "NORTH_AMERICA":
            region_val = 0
        elif value == "SOUTH_AMERICA":
            region_val = 1
        elif value == "ASIA":
            region_val = 2
        elif value == "ANTARTICA":
            region_val = 3
        elif value == "AFRICA":
            region_val = 4
        elif value == "EUROPE":
            region_val = 5
        elif value == "AUSTRALIA":
            region_val = 6
        else:
            print("Sorry wrong input!")
            break


        print("Thank you for your time! We will get back to you shortly!")
        value = "exit"

        # print ML model result
        ml.predict_ml([
            LimitedPartner.fundsize,
            region_val,
            risk_val,
            sector_val,
            strategy_val])

