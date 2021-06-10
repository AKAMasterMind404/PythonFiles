def balanceUpdater(statement):
    amount=int(statement[2::])
    if statement[0].lower()=='w':
        return amount*-1
    elif statement[0].lower()=='d':
        return amount
    else:
        return None

balance=0
while True:
    ask=input('If you want to update passbook enter \'Y\'')
    if ask.lower()=='y':
        j=input('Enter Transaction Type,Amount:')
        add=balanceUpdater(j)
        if add!=None:
            balance+=add
        else:
            print('Invalid Input!')
    else:
        break
print('Your Balance is:',balance)