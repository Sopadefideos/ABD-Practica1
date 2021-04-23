from NuestroASF import ASFile
from NuestroRegistro import registro

asf = ASFile()
file = asf.open("data/insertar.csv")
value, pos = asf.first(file, 0)
asf.pretty_print_row(value, pos)

while asf.end(file, pos) == False:
    value, pos = asf.next(file, pos)
    asf.pretty_print_row(value, pos)