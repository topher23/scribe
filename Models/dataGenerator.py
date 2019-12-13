import csv
import random

from Models.Company import Company
from Models.Aggregables import FundSize, Regions, Risks, Sector, Strategy
from Models.LimitedPartner import LimitedPartner

list_of_funds = []
list_of_regions = []
list_of_risks = []
list_of_sectors = []
list_of_strategies = []

list_of_companies = []
list_of_investors = []


def generate_investors():
    for i in range(0, 150):
        list_of_investors.append(
            LimitedPartner(
                "Investor " + str(i),
                random.randint(0, len(list_of_funds) - 1),
                random.randint(0, len(list_of_regions) - 1),
                random.randint(0, len(list_of_sectors) - 1),
                random.randint(0, len(list_of_strategies) - 1),
                random.randint(0, len(list_of_risks) - 1)
            )
        )


def generate_companies():
    for i in range(0, 20):
        list_of_companies.append(
            Company(
                "Company " + str(i),
                random.randint(0, len(list_of_funds) - 1),
                random.randint(0, len(list_of_regions) - 1),
                random.randint(0, len(list_of_sectors) - 1),
                random.randint(0, len(list_of_strategies) - 1),
                random.randint(0, len(list_of_risks) - 1)
            )
        )

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
            "Investor Desired Strategy",
            "Invested"
        ])
        for i in range(0, 150):
            lp = list_of_investors[random.randint(0, len(list_of_investors) - 1)]
            comp = list_of_companies[random.randint(0, len(list_of_companies) - 1)]

            writer.writerow(
                [
                    i,
                    "Company " + str(i),
                    list_of_funds[comp.fundsize].value,
                    list_of_regions[comp.region].value,
                    list_of_risks[comp.risk].value,
                    list_of_sectors[comp.sector].value,
                    list_of_strategies[comp.strategy].value,

                    "Investor " + str(i),
                    list_of_funds[lp.fundsize].value,
                    list_of_regions[lp.region].value,
                    list_of_risks[lp.risk].value,
                    list_of_sectors[lp.sector].value,
                    list_of_strategies[lp.strategy].value,
                    random.randint(0, 1)
                ])


generate_lists_of_aggregables()

generate_investors()
generate_companies()

generateCompanies()
