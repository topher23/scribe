# Private Equity Company

class Company:

    company_data = [Company.name, Company.available_fund_size]

    def __init__(self, name, available_fund_size=0):
        self.name = name
        self.available_fund_size = available_fund_size

