import json, os
from datetime import datetime
FILE_NAME = "expenses.json"
class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()
    def load_expenses(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as f:
                return json.load(f)
        return []
    def save_expenses(self):
        with open(FILE_NAME, 'w') as f:
            json.dump(self.expenses, f, indent=4)
    def add_expense(self, amount, category, note):
        expense = {"id": len(self.expenses)+1, "amount": amount, "category": category, "note": note, "date": datetime.now().strftime("%Y-%m-%d %H:%M")}
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Added: Rs.{amount} for {category}")
    def view_expenses(self):
        if not self.expenses: print("No expenses!"); return
        total=0
        for exp in self.expenses:
            print(f"{exp['id']}. Rs.{exp['amount']} | {exp['category']} | {exp['note']}")
            total+=exp['amount']
        print(f"Total: Rs.{total}")
def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1.Add 2.View 3.Exit")
        c=input("Choose: ")
        if c=='1':
            amt=float(input("Amount Rs: "))
            cat=input("Category: ")
            note=input("Note: ")
            tracker.add_expense(amt,cat,note)
        elif c=='2': tracker.view_expenses()
        elif c=='3': break
if __name__ == "__main__": main()
