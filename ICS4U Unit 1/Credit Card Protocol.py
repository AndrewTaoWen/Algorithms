balance = int(input('Enter you balance: '))

payment = max(0.021 * balance, min(10, balance))

print('The payment cost is:', int(payment))