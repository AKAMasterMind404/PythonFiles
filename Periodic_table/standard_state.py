from Periodic_table import main as m


def radiusRectifier(string):
    string = string.strip()
    if not string: return 0
    if '(' not in string:
        return float(string.strip())

    return float(string[:string.index('(')].strip())


for i in m.data:
    atomic_number = int(i['atomicNumber'])
    s_State = i['standardState'] if i['standardState'] else 'Lab'
    mPoint = i['meltingPoint'] if i['meltingPoint'] else '0'
    bPoint = i['boilingPoint'] if i['boilingPoint'] else '0'
    i_rad = radiusRectifier(i['ionRadius']) if radiusRectifier(i['ionRadius']) else 0

    # print(f"{atomic_number},'{gBlock}','{symbol}','{radius}', '{yDis}'")
    query = f"INSERT INTO standard_state values({atomic_number},'{s_State}','{mPoint}','{bPoint}', '{i_rad}');"
    print(query)
    # print(f"{atomic_number},'{s_State}','{mPoint}','{bPoint}', '{i_rad}'")
    m.mycursor.execute(query)

    m.mydb.commit()
