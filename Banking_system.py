import json

class Personnel:
    def __init__(self, personID, person_type, name, address, contact_info):
        self.personID = personID
        self.person_type = person_type
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def display_details(self):
        print(f"ID: {self.personID}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact Info: {self.contact_info}")


class Customers(Personnel):
    def __init__(self, personID,person_type, name, address, contact_info, customerID, customer_type):
        super().__init__(personID, person_type, name, address, contact_info)
        self.customerID = customerID
        self.customer_type = customer_type
        self.accounts = []

    def viewAccountDetails(self):
        if self.accounts:
            for account in self.accounts:
                print(f"Account Type: {account.accountType}")
                print(f"Account ID: {account.accountID}")
                print(f"Balance: {account.balance}")
                print("--------------------")
        else:
            print("No accounts found.")

    def makeTransaction(self, from_account, to_account, amount):
        # Logic for making a transaction between accounts
        pass
    
    def avail_service(self, service):
        # Method to avail a service by appending the service to the customer's services list
        self.services.append(service)

    def show_services(self):
        # Method to display the services availed or interested in by the customer
        if self.services:
            print(f"Services for {self.name}:")
            for service in self.services:
                print(f"- {service.serviceName}")
        else:
            print(f"No services availed for {self.name}.")


class Employees(Personnel):
    def __init__(self, personID, person_type, name, address, contact_info, employeeID, jobTitle, employeeType, salary):
        super().__init__(personID, person_type, name, address, contact_info)
        self.employeeID = employeeID
        self.jobTitle = jobTitle
        self.employeeType = employeeType
        self.salary = salary
    
    def display_details(self):
        print(f"Person ID: {self.personID}")
        print(f"Person Type: {self.person_type}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Contact Info: {self.contact_info}")
        print(f"Employee ID: {self.employeeID}")
        print(f"Job Title: {self.jobTitle}")
        print(f"Employee Type: {self.employeeType}")
        print(f"Salary: {self.salary}")

    def get_employee_details(self):
        # Return employee details as a dictionary
        return {
            "personID": self.personID,
            "person_type": self.person_type,
            "name": self.name,
            "address": self.address,
            "contact_info": self.contact_info,
            "employeeID": self.employeeID,
            "jobTitle": self.jobTitle,
            "employeeType": self.employeeType,
            "salary": self.salary
        }

    def authenticate_user(self, customer, password):
        # Logic for employee to authenticate customer
        pass

    def process_transaction(self, account_from, account_to, amount):
        # Logic for employee to process a transaction
        pass

class BankAccount:
    def __init__(self, accountID, accountType, balance):
        self.accountID = accountID
        self.accountType = accountType
        self.balance = balance
        #self.customerID = customerID
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
            print(f"Balance: {self.balance}")
        else:
            print("Insufficient funds.")
    #def deposit(self, customerID, amount):
        #if customer.personID == self.customerID:
            #self.balance += amount
            #print(f"Deposited: {amount}")
            #print(f"New Balance: {self.balance}")
        #else:
            #print("Customer ID does not match the account's customer.")
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")
        print(f"New Balance: {self.balance}")

class CheckingAccount(BankAccount):
    def __init__(self, accountID, balance, overdraftProtection=True):
        super().__init__(accountID, "Checking", balance)   
        self.overdraftProtection = overdraftProtection
    


class SavingsAccount(BankAccount):
    def __init__(self, accountID, balance, interestRate, customerID):
        super().__init__(accountID, "Savings", balance)
        self.interestRate = interestRate
        self.customerID = customerID

class Services:
    def __init__(self, serviceID, serviceName, description):
        self.serviceID = serviceID
        self.serviceName = serviceName
        self.description = description

    def display_details(self):
        print(f"Service ID: {self.serviceID}")
        print(f"Service Name: {self.serviceName}")
        print(f"Description: {self.description}")
    
    def provide_service(self, customer):
        # Logic to provide the service
        # Example: Printing a generic service message for demonstration purposes
        print(f"Providing {self.serviceName} service to {customer.name}")

    def get_service_details(self):
        # Logic to retrieve service details
        # Example: Returning basic service information for demonstration purposes
        return {
            "Service ID": self.serviceID,
            "Service Name": self.serviceName,
            "Description": self.description
        }

class LoanServices(Services):
    def __init__(self, serviceID, serviceName, description, loanType, interestRate):
        super().__init__(serviceID, serviceName, description)
        self.loanType = loanType
        self.interestRate = interestRate

    def process_loan_application(self, customer, amount):
        # Logic to process a loan application for the customer
        pass


class InsuranceServices(Services):
    def __init__(self, serviceID, serviceName, description, coverageType, premium):
        super().__init__(serviceID, serviceName, description)
        self.coverageType = coverageType
        self.premium = premium

    def purchase_insurance(self, customer, coverage_details):
        # Logic to handle insurance purchase for the customer
        pass


class InvestmentServices(Services):
    def __init__(self, serviceID, serviceName, description, investmentType, riskLevel):
        super().__init__(serviceID, serviceName, description)
        self.investmentType = investmentType
        self.riskLevel = riskLevel

    def make_investment(self, customer, amount):
        # Logic to handle customer investments
        pass


# Initializing a Customer instance
customer = Customers(personID=1, person_type="Customer", name="John Doe", address="123 Main St", contact_info="123-456-7890", customerID=101, customer_type="Regular")

# Display customer details
customer.display_details()

#Initialize an employee instance
employee = Employees(personID=10, person_type="Employee", name="Mark Josh", address="333 North St", contact_info="423-466-1890", employeeID="EMP101", employeeType="Full-Time", jobTitle="Senior Financial Analyst", salary=50000)

# Display Employee details
employee.display_details()
employee_data = employee.get_employee_details()
file_name = "employee.json"
with open(file_name, "w") as file:
    json.dump(employee_data, file, indent=4)
print(f"Employee details saved to {file_name}")

# Create a SavingsAccount for the customer
savings_account = SavingsAccount(accountID=1001, balance=5000, customerID=101, interestRate=0.02)

# Function to deposit money while ensuring customerID matches
def deposit_amount(account, customer_id, amount):
    if account.customerID == customer_id:
        account.deposit(amount)
    else:
        print("Customer ID does not match the account's customer.")

# Deposit into the savings account
deposit_amount(savings_account, 101, 1000)


# Save customer data to JSON file
customer_data = {
    "name": customer.name,
    "address": customer.address,
    "contact_info": customer.contact_info,
    "customerID": customer.customerID
}

# Serialize data to JSON and write to a file
with open('customer_data.json', 'w') as json_file:
    json.dump(customer_data, json_file)
