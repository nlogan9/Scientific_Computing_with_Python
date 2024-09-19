class Category:

    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        budget_ledger_str = ''
        category_index = (30 - len(self.category)) // 2
        for i in range(category_index):
            budget_ledger_str += '*'
        for i in range(30 - category_index):
            if i < len(self.category):
                budget_ledger_str += self.category[i]
            else:
                budget_ledger_str += '*'
        budget_ledger_str += "\n"
        for i in self.ledger:
            for j in range(23):
                if j < len(i['description']):
                    budget_ledger_str += i['description'][j]
                else:
                    budget_ledger_str += ' '
            amount_list = str(i['amount']).split('.')
            spaces = 4 - len(amount_list[0])
            for j in range(spaces):
                budget_ledger_str += ' '
            budget_ledger_str += amount_list[0] + '.'

            if len(amount_list) == 1:
                budget_ledger_str += '00'
            elif len(amount_list[1]) == 1:
                budget_ledger_str += amount_list[1] + '0'
            else:
                budget_ledger_str += amount_list[1][0] + amount_list[1][1]
            budget_ledger_str += '\n' 
        budget_ledger_str += 'Total: ' + str(self.get_balance())



        return budget_ledger_str

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            description1 = f'Transfer to {category.category}'
            print(description1)
            description2 = f'Transfer from {self.category}'
            self.withdraw(amount, description1)
            category.deposit(amount, description2)
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

 
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(65, 'groceries')
#food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
#food.transfer(50, clothing)
auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(15)
clothing.deposit(1000, 'deposit')
clothing.withdraw(25)
print(food)
print(clothing)


def create_spend_chart(categories):
    spending = []
    total = 0
    max_length = 0
    for category in categories:
        spent = 0
        if len(category.category) > max_length:
            max_length = len(category.category)
        for i in category.ledger:
            if i['amount'] < 0:
                spent += -1 * i['amount']
        spending.append(spent)
        total += spent
    
    #print(spending, total, max_length)

    chart = 'Percentage spent by category\n'
    for i in range(100, -10, -10):
        spaces = 3 - len(str(i))
        for j in range(spaces):
            chart += ' '
        chart += str(i) + '| '
        for cat in spending:
            if cat / total * 100 >= i:
                chart += 'o  '
            else:
                chart += '   '
        chart += '\n'
    chart += '    '
    for i in range(len(categories) * 3 + 1):
        chart += '-'
    for i in range(max_length):
        chart += '\n    '
        for category in categories:
            if i < len(category.category):
                chart += ' ' + category.category[i] + ' '
            else:
                chart += '   '
        chart += ' '
    return chart

print(create_spend_chart([food, clothing, auto]))
