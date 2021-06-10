number_of_courses=int(input())

good_courses=0
l=[]

for course in range(number_of_courses):
	subjects, failed = map(int, input().split())
	marks=list(map(float, input().split()))
	average=sum(marks)/len(marks)

	res=''

	if average>55 and subjects - failed > failed:
		good_courses+=1
		res='Good'
	else:
		res='Not Good'

	l.append(res)

for i in l:
	print(i)

print('Car') if number_of_courses-good_courses<good_courses else print('Cycle')