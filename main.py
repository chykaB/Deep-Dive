"""
PERSONAL EARNINGS CALCULATOR
Concepts
- Variables
- Inputs
- Operators(+,-,/)
- Assignment
- Data types
- Formating

WHAT IT WILL DO (Pseudocode)
1. Ask for personal info
2. Ask for salary and months worked
3. Calculate total earnings
4. Calculate bonus
5. Calcualte net income
6. Average weekly income
7. Balance
8. Print summary
"""

"""
UPDATED ALGORITHM
1. While user wants to enter an employee:
2. Get inputs (name, salary, etc)
3. Compute net income
4. Use if-elif-else to clasify income level
5. Use a loop to deduct 3 expenses from net income
6. Show remaining balance and weekly distribution
7. Ask to stop or continue

UPDATED PSEUDOCODE
WHILE user wants to enter emplyee:
    Get employee details
    Caculate earnings and net income

    IF net income > 1,000,000:
        print "Higher earner"
    ELSE IF net income > 500, 000:
        print "Average earner"
    ELSE:
        print "Low earner"
    
    FOR 3 expense items:
        Ask for name and amount
        Subtract from the net income
    
    Show remianing balance
    Show weekly breakdown
    Ask if another employee should be entered
"""
NUMBER_OF_WEEKS = 4


class InvalidSalaryData(Exception):
    def __init__(self, salary, months, bonus):
        message = (
            f"Invalid salary data: salary={salary}, months={months}, bonus={bonus}"
        )
        if salary < 0:
            message += " Salary must be non-negative"
        if months <= 0:
            message += " Months must be greater than zero."
        if bonus <= 0:
            message += " Bonus percent must be non-negative"

        super().__init__(message)


class Employee:
    def __init__(self):
        self.details = {}
        self.salary_details = ()
        self.earnings = ()
        self.earner_type = ""
        self.expenses = []
        self.expense_names = set()
        self.weekly_income = 0
        self.balance = 0

    def collect_details(self):
        try:
            self.details["name"] = input("Enter employee's name: ")
            self.details["age"] = input("Enter age: ")
            self.details["job"] = input("Enter job title: ")
        except Exception as e:
            print(f"Error collecting personal details: {e}")

    def collect_salary_info(self):
        try:
            salary = float(input("Enter your monthly salary: "))
            months = int(input("How many months have you worked: "))
            bonus_percent = float(input("Enter your performance bonus (%): "))

            if salary < 0 or months <= 0 or bonus_percent <= 0:
                raise InvalidSalaryData(salary, months, bonus_percent)

            self.salary_details = (salary, months, bonus_percent)
        except ValueError:
            print("Invalid Input! Please enter numeric values.")
            self.collect_salary_info()
        except InvalidSalaryData as e:
            print(f"{e}")
            self.collect_salary_info()
        except Exception as e:
            print(f"Unexpected error during salary input: {e}")
            self.collect_salary_info()

    def calculate_earnings(self):
        try:
            salary, months, bonus_percent = self.salary_details
            total_earnings = salary * months
            bonus_amount = (bonus_percent / 100) * total_earnings
            net_income = total_earnings + bonus_amount
            self.earnings = (total_earnings, bonus_amount, net_income)
        except Exception as e:
            print(f"Error calculatinf earngins: {e}")

    def classify_earner(self):
        try:
            net_income = self.earnings[2]
            if net_income > 1_000_000:
                self.earner_type = "High earner"
            elif net_income > 500_000:
                self.earner_type = "Average earner"
            else:
                self.earner_type = "Low earner"
        except Exception as e:
            print(f"Error collecting expenses: {e}")
            self.classify_earner()

    def collect_expenses(self):
        try:
            self.expenses.clear()
            self.expense_names.clear()

            for i in range(3):
                name = input(f"  Expense #{i + 1} name: ")
                amount = float(input(f" Amount for {name}: "))
                self.expenses.append({"name": name, "amount": amount})
                self.expense_names.add(name)
        except ValueError:
            print(f"Please enter valid numbers for expense amounts.")
            self.collect_expenses()
        except Exception as e:
            print(f" Error colllecting expense: {e}")
            self.collect_expenses()

    def deduct_expenses(self):
        try:
            net_income = self.earnings[2]
            for expense in self.expenses:
                net_income -= expense["amount"]
            self.earnings = (self.earnings[0], self.earnings[1], net_income)
        except Exception as e:
            print(f"Error deducting expenses: {e}")

    def compute_weekly_distribution(self):
        try:
            months = self.salary_details[1]
            net_income = self.earnings[2]
            total_weeks = months * NUMBER_OF_WEEKS

            self.weekly_income = net_income // total_weeks if total_weeks else 0
            self.balance = net_income % total_weeks if total_weeks else net_income
        except Exception as e:
            print(f"Error computing weekly distribution: {e}")

    def print_summary(self):
        try:
            print("\n--- Earnings Summary ---")
            print(f"Name: {self.details['name']}")
            print(f"Age: {self.details['age']}")
            print(f"Job: {self.details['job']}")
            print(f"Monthly Salary: {self.salary_details[0]}")
            print(f"Months worked: {self.salary_details[1]}")
            print(f"Total earnings (Before bonus): {self.earnings[0]}")
            print(f"Bonus Percentage: {self.salary_details[2]}")
            print(f"Bonus Amount: {self.earnings[1]}")
            print(f"Earner Type: {self.earner_type}")
            print(f"Aproximate weekly income: {self.weekly_income}")
            print(f"Balance: {self.balance}")
            print(f"Expenses: {[ expense['name'] for expense in self.expenses ]}")
        except Exception as e:
            print(f"Error printing summary: {e}")


def main():
    add_more = "yes"
    employees = []

    while add_more.lower() == "yes":
        emp = Employee()
        emp.collect_details()
        emp.collect_salary_info()
        emp.calculate_earnings()
        emp.classify_earner()
        emp.collect_expenses()
        emp.deduct_expenses()
        emp.compute_weekly_distribution()
        emp.print_summary()

        employees.append(emp)

        try:
            add_more = input("\n Do you want to add another employee? (yes/no): ")
        except Exception as e:
            print(f"Error reading inout: {e}")
            break

    print("\n All employee data entered. Session completed")

if __name__ == "__main__":
    main()
