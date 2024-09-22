class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest

    def value_after(self, n):
        return self.principal * (1 + self.interest / 100) ** n

    def __str__(self):
        return f"Principal - ${self.principal:.2f}, Interest rate - {self.interest:.2f}%"

# Test usage:
investment = Investment(1000, 5.12)
print(investment)
print(f"Value after 5 years: ${investment.value_after(5):.2f}")
