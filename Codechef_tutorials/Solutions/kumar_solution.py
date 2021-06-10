number_of_names=input()
number_of_names=int(number_of_names)

answers=[]
#kumar
for i in range(number_of_names):
    fullname=input()
    surname=fullname.split()[1]
    if surname[-1:-6:-1][::-1]=='kumar':
        # print(surname[-1:-6:-1][::-1])
        answers.append('Namaste')
    else:
        # print(surname[-1:-6:-1][::-1])
        answers.append('Hello')

for i in answers:
    print(i)