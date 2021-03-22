from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Eletric"],
        ["Charmander", "Fire"],
        ["Psyduc", "Water"],
        ["Meowth", "Normal"]
    ]
)
print(table)

table2 = PrettyTable()
table2.add_column("Pokemon Name", ["Pikachu", "Charmander", "Psyduc", "Meowth"])
table2.add_column("Type", ["Eletric", "Fire", "Water", "Normal"])
table2.align = "l"
print(table2)