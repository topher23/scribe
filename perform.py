from Models.LimitedPartner import *

def main():
    print("Welcome to Scribe Company Recommendation tool. This is a rudimentary tool for recommending you which "
          "companies to invest in based on a series of factors using machine learning. ")
    print("We will generate and train our model based on your input parameters. ")

    value = ""

    while value.lower() != "exit":
        value = input("What is your name?\n")
        LimitedPartner.name = value

        try:
            value = int(input("What is your Available Investment?\n"))
            if value < 100000:
                print("Sorry not enough funds!")
                break
            elif value >= 100000 and value < 500000:
                LimitedPartner.available_investment = 100000
            elif value >= 500000 and value < 1000000:
                LimitedPartner.available_investment = 500000
            elif value >= 1000000 and value < 25000000:
                LimitedPartner.available_investment = 1000000
            elif value >= 25000000 and value < 1000000000:
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

main()
