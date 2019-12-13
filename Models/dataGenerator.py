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
                i,
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
                i,
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
                    comp.name,
                    comp.fundsize,
                    comp.region,
                    comp.risk,
                    comp.sector,
                    comp.strategy,

                    lp.name,
                    lp.fundsize,
                    lp.region,
                    lp.risk,
                    lp.sector,
                    lp.strategy
                ])


generate_lists_of_aggregables()

generate_investors()
generate_companies()

generateCompanies()
