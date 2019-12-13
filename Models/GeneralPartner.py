class GeneralPartner:

    limited_partners = []

    companies = []

    def __init__(self, name):
        self.name = name

    def add_company(self, company):
        self.companies.append(company)

    def add_limited_partner(self, limited_partner):
        self.limited_partners.append(limited_partner)
