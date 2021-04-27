from NuestroASF import ASFile
from NuestroRegistro import registro

finish = False
file_read = False
asf = ASFile()

while finish == False:
    print("*************** MENU ***************")
    print("1---> Read file.")
    print("2---> First register.")
    print("3---> Next register.")
    print("4---> Add register.")
    print("5---> Search register.")
    print("6---> Modify register.")
    print("7---> Delete register.")
    print("8---> List register.")
    print("9---> List raw register.")
    print("10---> Finish program.")

    option = input("")
    if option == "1":
        asf.open("data/insertar.csv")
        file_read = True
    elif option == "2":
        if file_read == True:
            row, position = asf.first()
            asf.pretty_print_row(row, position)
        else:
            print("Please read the file first")
    elif option == "3":
        if file_read == True:
            if asf.end(position + 1) == False:
                row, position = asf.next(position)
                asf.pretty_print_row(row, position)
            else:
                print("There are not more registers in that file")
        else:
            print("Please read the file first")
    elif option == "4":
        if file_read == True:
            reg = registro()
            reg.nuevoRegistro("Anotacion 45", 45, 45, 45.0, 45.0, 45)
            asf.add(reg)
        else:
            print("Please read the file first")
    elif option == "5":
        if file_read == True:
            position = input("Put the number of the register you want to search: ")
            row, position = asf.search(position)
            asf.pretty_print_row(row, position)
        else:
            print("Please read the file first")
    elif option == "6":
        if file_read == True:
            reg = registro()
            reg.nuevoRegistro("Anotacion 45", 45, 45, 45.0, 45.0, 45)
            asf.modify(reg, position)
        else:
            print("Please read the file first")
    elif option == "7":
        if file_read == True:
            asf.delete(position)
        else:
            print("Please read the file first")
    elif option == "8":
        if file_read == True:
            asf.list()
        else:
            print("Please read the file first")
    elif option == "9":
        if file_read == True:
            asf.list_row()
        else:
            print("Please read the file first")
    elif option == "10":
        finish = True
