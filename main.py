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
    print("10---> Reorganize file.")
    print("11---> Close file.")
    print("12---> Drop by other file.")
    print("13---> Finish program.")

    option = input("")
    # READ FILE
    if option == "1":
        asf.open("data/insertar.csv")
        file_read = True

    # FIRST REGISTER
    elif option == "2":
        if file_read == True:
            row, position = asf.first()
            asf.pretty_print_row(row, position)
        else:
            print("Please read the file first")

    # NEXT REGISTER
    elif option == "3":
        if file_read == True:
            if asf.end(position + 1) == False:
                row, position = asf.next(position)
                asf.pretty_print_row(row, position)
            else:
                print("There are not more registers in that file")
        else:
            print("Please read the file first")

    # ADD REGISTER
    elif option == "4":
        if file_read == True:
            reg = registro()
            reg.nuevoRegistro("Anotacion 45", 45, 45, 45.0, 45.0, 45)
            asf.add(reg)
        else:
            print("Please read the file first")

    # SEARCH REGISTER
    elif option == "5":
        if file_read == True:
            position = input("Put the number of the register you want to search: ")
            row, position = asf.search(position)
            asf.pretty_print_row(row, position)
        else:
            print("Please read the file first")

    # MODIFY REGISTER
    elif option == "6":
        if file_read == True:
            reg = registro()
            reg.nuevoRegistro("Anotacion 45", 45, 45, 45.0, 45.0, 45)
            asf.modify(reg, position)
        else:
            print("Please read the file first")

    # DELETE REGISTER
    elif option == "7":
        if file_read == True:
            asf.delete(position)
        else:
            print("Please read the file first")

    # LIST REGISTERS
    elif option == "8":
        if file_read == True:
            asf.list()
        else:
            print("Please read the file first")

    # LIST RAW REGISTERS
    elif option == "9":
        if file_read == True:
            asf.list_raw()
        else:
            print("Please read the file first")

    # REORGANIZE FILE
    elif option == "10":
        path_option = input("Do yo want to insert a path? y/n: ")
        if path_option == "y":
            asf.reorganize(True)
        elif path_option == "n":
            asf.reorganize(False)

    # CLOSE FILE
    elif option == "11":
        if file_read == True:
            asf.close()
            file_read == False
        else:
            print("Please read the file first")

    # DROP BY FILE
    elif option == "12":
        if file_read == True:
            path = input("Insert the path of the file: ")
            asf.delete_by_file(path)
        else:
            print("Please read the file first")

    # EXIT MENU
    elif option == "13":
        finish = True
