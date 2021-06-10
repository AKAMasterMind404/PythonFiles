import csv

with open('finalbatch.csv','r') as sheet:
    sheet=csv.DictReader(sheet)
    fieldnames=sheet.fieldnames
print(fieldnames)

with open('finalbatch.csv','r') as contactsheet:
    contactsheet=csv.DictReader(contactsheet)

    with open('refinedFinal.csv','a') as read:
        read = csv.DictWriter(read, fieldnames=fieldnames)
        c=0
        for i in contactsheet:
            if i["Name"]!="":
                name=i['Name']
                phone=str(i['Phone 1 - Value'])
                if len(phone)!=10:
                    print(phone)
                    c+=1
                #read.writerow({'Name':name,'Phone 1 - Value':phone})
        print(c)