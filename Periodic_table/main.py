import mysql.connector
import requests as r


def massRefiner(val):
    if type(val) == list: return str(val[0])

    decimal = val.index('.')
    bracket = val.index('(')

    return val[:decimal + 1] + val[decimal + 1:bracket][:3]


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="periodic_table"
)

mycursor = mydb.cursor()
data = eval(r.get('https://neelpatel05.pythonanywhere.com/').text)

if __name__ == '__main__':
    for i in data:
        atomic_number = int(i['atomicNumber'])
        name = i['name']
        mass = massRefiner(i['atomicMass'])
        radius = i['atomicRadius'] if i['atomicRadius'] else 'Unknown'

        # print(f"{atomic_number},'{gBlock}','{symbol}','{radius}', '{yDis}'")
        query = f"INSERT INTO main_table values({atomic_number},'{name}','{mass}','{radius}');"

        mycursor.execute(query)

        mydb.commit()
