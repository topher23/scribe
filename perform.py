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
                LimitedPartner.available_investment = 100000
            elif 500000 <= value < 1000000:
                LimitedPartner.available_investment = 500000
            elif 1000000 <= value < 25000000:
                LimitedPartner.available_investment = 1000000
            elif 25000000 <= value < 1000000000:
                LimitedPartner.available_investment = 25000000
            elif value >= 1000000000:
                LimitedPartner.available_investment = 1000000000
            else:
                print("Sorry wrong input!")
                break
        except:
            print("Sorry wrong input!")

        value = input("What is your preferred sector? \nAvailable sectors as of today: MILITARY, FOOD, PHARMA, FINANCE, TECH, CONSUMER\n")
        LimitedPartner.sector = value

        value = input("What is your strategy? \nAvailable strategies as of today: Low, Medium Low, Medium, Medium High, High\n")
        LimitedPartner.risk = value

        print("Thank you for your time! We will get back to you shortly!")
        value = "exit"

        # print ML model result
        ml.predict_ml([
            LimitedPartner.fundsize,
            LimitedPartner.region,
            LimitedPartner.risk,
            LimitedPartner.sector,
            LimitedPartner.strategy])

