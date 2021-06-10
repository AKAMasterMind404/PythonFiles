from Periodic_table.SQL_STATEMENT_AUTOMATION import data as d
import random as r


def valModifier(val):
    if type(val) == str:
        return f' "{val}" '
    else:
        return val


def randomAttributes():
    seed1 = r.randrange(0, len(d.t_contents.items()))
    selected1 = list(d.t_contents.items())[seed1]
    t1 = selected1[0]
    t1Table = selected1[1][0]

    comp = d.comparision[r.randrange(0, len(d.comparision))]
    litVal = d.literal[r.randrange(0, len(d.literal))]

    orderSeed = r.randrange(0, len(d.order))

    seed2 = r.randrange(0, len(d.t_contents.items()))
    selected2 = list(d.t_contents.items())[seed2]
    t2 = selected2[0]
    t2Table = selected2[1][0]

    return t1, comp, litVal, orderSeed, t2, t1Table, t2Table


def childGenerator(table: d.Table, t2):
    st = ""
    for i in table.children:
        st += f" t1.{i},\n"

    st = st.strip()
    st += f"\n t2.{t2}"
    return st


t1, comp, litVal, orderSeed, t2, ob1, ob2 = randomAttributes()
# 'DENSITY', '<=', 50, 0, 'DENSITY', d.bonding_type, d.bonding_type
print(f"PASSED:{t1, comp, litVal, orderSeed, t2,} table:{ob1.name} table:{ob2.name}")
try:
    query = "SELECT \n" \
        f" {childGenerator(ob1, d.t_contents.get(t2)[1])} \n" \
        f"FROM \n" \
        f"(SELECT * FROM {ob1.name}WHERE {d.t_contents.get(t1)[1]} {comp} {valModifier(litVal)}) as t1\n" \
        f"JOIN {ob2.name} t2\n" \
        f"ON\n" \
        f"t1.atomic_number = t2.atomic_number\n" \
        f"ORDER BY \n" \
        f"t2.{d.t_contents.get(t2)[1]} {d.c_rep[orderSeed]};"
    print(query)
except:
    print("Ambiguous Query!")
