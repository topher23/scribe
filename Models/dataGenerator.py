import csv
import random

from Models.Aggregables import FundSize, Regions, Risks, Sector, Strategy

list_of_funds = []
list_of_regions = []
list_of_risks = []
list_of_sectors = []
list_of_strategies = []


def generate_lists_of_aggregables():
    for i in FundSize.FundSize:
        list_of_funds.append(i)
    for i in Regions.Regions:
        list_of_regions.append(i)
    for i in Risks.Risks:
        list_of_risks.append(i)
    for i in Sector.Sector:
        list_of_sectors.append(i)
    for i in Strategy.Strategy:
        list_of_strategies.append(i)

def generateCompanies():
    with open('companies.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Row",
            "Company Name",
            "Company Fund Size",
            "Company Region",
            "Company Risk",
            "Company Sector",
            "Company Strategy",
            "Investor Name",
            "Investor Desired Fund Size",
            "Investor Desired Region",
            "Investor Desired Risk",
            "Investor Desired Sector",
            "Investor Desired Strategy"
        ])
        for i in range(0, 20):
            writer.writerow(
                [
                    i,
                    "Company " + str(i),
                    list_of_funds[random.randint(0, len(list_of_funds) - 1)].value,
                    list_of_regions[random.randint(0, len(list_of_regions) - 1)].value,
                    list_of_risks[random.randint(0, len(list_of_risks) - 1)].value,
                    list_of_sectors[random.randint(0, len(list_of_sectors) - 1)].value,
                    list_of_strategies[random.randint(0, len(list_of_strategies) - 1)].value,

                    "Investor " + str(i),
                    list_of_funds[random.randint(0, len(list_of_funds) - 1)].value,
                    list_of_regions[random.randint(0, len(list_of_regions) - 1)].value,
                    list_of_risks[random.randint(0, len(list_of_risks) - 1)].value,
                    list_of_sectors[random.randint(0, len(list_of_sectors) - 1)].value,
                    list_of_strategies[random.randint(0, len(list_of_strategies) - 1)].value
                ])


generate_lists_of_aggregables()
generateCompanies()
