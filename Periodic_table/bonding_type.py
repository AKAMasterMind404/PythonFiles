from Periodic_table import main as m

for i in m.data:
    atomic_number = int(i['atomicNumber'])
    bType = i['bondingType'] if i['bondingType'] else 'Unknown'
    o_s = i['oxidationStates'] if i['oxidationStates'] else 'Unknown'
    en = i['electronegativity'] if i['electronegativity'] else 'Unknown'
    d = i['density'] if i['density'] else 'Unknown'
    io = i['ionizationEnergy'] if i['ionizationEnergy'] else 'Unknown'

    # print(f"{atomic_number}, '{bType}', '{o_s}', '{en}', '{d}', '{io}'")
    # print(values)
    # sql1 = "INSERT INTO main_table (Atomic_number, Name, atomic_mass, Atomic_Radius) VALUES (%d, %s, %s, %s);"
    query = f"INSERT INTO bonding_type values({atomic_number}, '{bType}', '{o_s}', '{en}', '{d}', '{io}');"

    m.mycursor.execute(query)
    m.mydb.commit()
