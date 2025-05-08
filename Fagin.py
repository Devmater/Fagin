class Organization:
    def __init__(self, name, registration_fee, annual_fee):
        self.name = name
        self.registration_fee = registration_fee
        self.annual_fee = annual_fee

    def total_cost(self, years):
        return self.registration_fee + (self.annual_fee * years)

def main():
    org_name = input("Введите название организации: ")
    registration_fee = float(input("Введите регистрационный сбор: "))
    annual_fee = float(input("Введите ежегодный сбор: "))
    years = int(input("Введите количество лет: "))

    organization = Organization(org_name, registration_fee, annual_fee)
    total = organization.total_cost(years)

    print(f"Общая стоимость для {org_name} за {years} лет: {total} руб.")

if __name__ == "__main__":
    main()

while True:
    pass
