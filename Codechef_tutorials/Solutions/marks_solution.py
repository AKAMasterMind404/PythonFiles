grades=[]

for i in range(5):
    marks=input()
    marks=int(marks)

    if marks in range(90,101):
        grades.append('A')
    elif marks in range(70,90):
        grades.append('B')
    elif marks in range(50, 70):
        grades.append('C')
    elif marks in range(35,50):
        grades.append('D')
    else:
        grades.append('F')

for i in grades:
    print(i)