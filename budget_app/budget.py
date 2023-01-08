class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    
    recipt = self.name.center(30, "*")

    for record in self.ledger:
      recipt += "\n" + record['description'][:23].ljust(23, " ") + str(format(record['amount'], '.2f')).rjust(7, " ")

    recipt += "\nTotal: " + str(format(self.get_balance(),'.2f'))
    
    return recipt

  def create_spend_chart(categories):
    return True

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description=""):

    if not self.check_funds(amount):
      return False

    amount = amount * -1
    self.ledger.append({"amount": amount, "description": description})

    return True

  def transfer(self, amount, new_category):
    if not self.check_funds(amount):
      return False

    self.ledger.append({"amount": (amount * -1), "description": "Transfer to " + new_category.name})

    new_category.ledger.append({"amount": amount, "description": "Transfer from " + self.name})
    
    return True
    


  def get_balance(self):
    total = 0.0
    for category in self.ledger:
      total += category['amount']
    return total

  def check_funds(self, amount):
    total = self.get_balance()
    if total < amount:
      return False
    return True
    
def create_spend_chart(categories):

  graphic = "Percentage spent by category\n"
  total_withdraw = calc_withdraws(categories)
  max_len = 0
  for x in range(100, -1, -10):
    graphic += str(x).rjust(3," ") + "|"
    for categorie in categories:
      max_len = len(categorie.name) if len(categorie.name) > max_len else max_len
      spent = percentage_spent(total_withdraw, categorie) 
      if x - spent <= 0:
        graphic += " o " 
      else:
        graphic += "   "
    graphic += " \n"  
  graphic += "    -" + "---"* len(categories) + "\n"
  for x in range(max_len):
    graphic += "    "
    for categorie in categories:
      try:
        graphic += categorie.name[x].center(3, " ")
      except:
        graphic += "   "
    graphic += " \n"
  graphic = graphic[:-1]
  return graphic
  
def calc_withdraws(categories):
  total_withdraw = 0.00
  for categorie in categories:
    withdraw = 0.00
    for record in categorie.ledger:
      if record["amount"] < 0:
        withdraw += record["amount"]
        
    categorie.withdraw = withdraw
    total_withdraw += withdraw

  return total_withdraw

def percentage_spent(total_withdraw, categorie):
  return (categorie.withdraw * 100) / total_withdraw //10 * 10