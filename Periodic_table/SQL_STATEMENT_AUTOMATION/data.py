class Table:
    def __init__(self, name, children):
        self.name = name
        self.children = children


main_table = Table(name=" main_table ",
                   children=["Atomic_Number", "Name", "atomic_mass", "atomic_radius"])

standard_state = Table(name=" standard_state ",
                       children=["atomic_number", "standard_state", "melting_point", "boiling_point", "ion_radius"])

group_block = Table(name=" group_block ",
                    children=["atomic_number", "group_block", "symbol", "atomic_radius", "year_discovered"])

bonding_type = Table(name=" bonding_type ",
                     children=["atomic_number", "bonding_type", "oxidation_states",
                               "electronegativity", "density", "ionization_energy"])

t_contents = {
    "ATOMIC NUMBER": [main_table, 'atomic_number'],
    "SYMBOL": [group_block, 'symbol'],
    "NAME": [main_table, 'name'],
    "MELTING POINT": [standard_state, 'melting_point'],
    "BOILING POINT": [standard_state, 'boiling_point'],
    "DENSITY": [bonding_type]
}

comparision = ['=', '>', '<', '>=', '<=', '!=']

literal = [50, "Hydrogen", 56, 12, 3341]  # say

order = ["ASCENDING", "DESCENDING"]
c_rep = ["ASC","DESC"]
