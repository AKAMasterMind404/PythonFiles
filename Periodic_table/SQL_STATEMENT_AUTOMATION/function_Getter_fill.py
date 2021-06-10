import mysql.connector
import requests as r


def massRefiner(val):
    if type(val) == list: return str(val[0])

    decimal = val.index('.')
    bracket = val.index('(')

    return val[:decimal + 1] + val[decimal + 1:bracket][:3]


def radiusRectifier(string):
    string = string.strip()
    if not string: return 0
    if '(' not in string:
        return float(string)

    return float(string[:string.index('(')].strip())


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="periodic_table"
)

mycursor = mydb.cursor()
data = eval(r.get('https://neelpatel05.pythonanywhere.com/').text)


def automateFunctiom():
    for i in data:
        r = i['atomicNumber']
        n = i['name']
        m = massRefiner(i['atomicMass'])
        rad = str(i['atomicRadius']) if i['atomicRadius'] else 'Unknown'
        # print(r)
        print(f'displayInfo({r},"{n}","{m}","{rad}");')
        print('#############')


if __name__ == '__main__':
    sampleQuery = "SELECT " + \
                  "t1.Atomic_Number," + \
                  "t1.Name," + \
                  "t1.atomic_mass," + \
                  "t1.atomic_radius," + \
                  "t2.symbol " + \
                  "FROM \n" + \
                  "(SELECT * FROM  main_table WHERE atomic_number < 56) as t1\n" + \
                  "JOIN  group_block  t2\n" + \
                  "ON \n" + \
                  "t1.atomic_number = t2.atomic_number \n" + \
                  "ORDER BY \n" + \
                  "t2.symbol DESC;"

    mycursor.execute(sampleQuery)

    result = mycursor.fetchall()

    [print(i) for i in result]
    mydb.commit()
