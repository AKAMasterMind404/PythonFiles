import csv

dic1={}
dic2={}
with open('Round_1.csv','r') as r1:
    r1=csv.DictReader(r1)
    for i in r1:
        time=float(i["Best Time(Mins)"])
        name=i["Team Name"]
        rank=int(i["Rank"])
        college=i["Organisation"]
        if time>2.5:
            dic1[name]=(rank,college)

with open('Round_2.csv', 'r') as r2:
    r2 = csv.DictReader(r2)
    for i in r2:
        time = float(i["Best Time(Mins)"])
        name = i["Team Name"]
        rank = int(i["Rank"])
        college=i["Organisation"]
        if time > 2.15:
            dic2[name]=(rank,college)

print(dic1)
print(dic2)


champions={}

for i in dic1:
    if i in dic2:
        print(i,dic1.get(i))
        champions[dic1.get(i)[0]+dic2.get(i)[0]]=i,dic1.get(i)[1]

champions1={i:champions.get(i)[0] for i in champions}
ranks=sorted([i for i in champions])

finals={}
for i in ranks:
    finals[i]=champions.get(i)

# with open('finalrankings.csv','a') as finalsheet:
#     finalsheet=csv.DictWriter(finalsheet,fieldnames=["Rank","Name","College"])
#     finalsheet.writeheader()
#     r=1
#     for i in finals:
#         finalsheet.writerow({"Rank":r,"Name":finals.get(i)[0],"College":finals.get(i)[1]})
#         r+=1