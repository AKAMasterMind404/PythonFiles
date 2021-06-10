from Periodic_table import main as m

for i in m.data:
    atomic_number = int(i['atomicNumber'])
    gBlock = i['groupBlock'] if i['groupBlock'] else 'Unknown'
    symbol = i['symbol'] if i['symbol'] else 'Unknown'
    radius = i['atomicRadius'] if i['atomicRadius'] else -1
    yDis = i['yearDiscovered']

    # print(f"{atomic_number},'{gBlock}','{symbol}','{radius}', '{yDis}'")
    query = f"INSERT INTO group_block values({atomic_number},'{gBlock}','{symbol}','{radius}', '{yDis}');"

    m.mycursor.execute(query)

    m.mydb.commit()
