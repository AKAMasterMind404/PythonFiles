from Periodic_table import main as m

for i in m.data:
    atomic_number = int(i['atomicNumber'])
    name = i['name']
    mass = m.massRefiner(i['atomicMass'])
    radius = i['atomicRadius'] if i['atomicRadius'] else 'Unknown'
    values = (atomic_number, name, mass, radius)
    # print(values)
    # sql1 = "INSERT INTO main_table (Atomic_number, Name, atomic_mass, Atomic_Radius) VALUES (%d, %s, %s, %s);"
    query = f"INSERT INTO main_table values({atomic_number},'{name}','{mass}','{radius}');"

    m.mycursor.execute(query)

    m.mydb.commit()