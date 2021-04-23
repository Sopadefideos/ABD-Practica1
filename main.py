from NuestroASF import ASFile
from NuestroRegistro import registro

finish = False
file_read = False
asf = ASFile()

while finish == False:
    print('*************** MENU ***************')
    print('1---> Read file.')
    print('2---> First register.')
    print('3---> Next register.')
    print('4---> Add register.')
    print('5---> Search register.')
    print('6---> List register.')
    print('9---> Finish program.')

    option = input('')
    if option == '1':
        file = asf.open('data/insertar.csv')
        file_read = True
    elif option == '2':
        if (file_read == True):
            row, position = asf.first(file, 0)
            asf.pretty_print_row(row, position)
        else:
            print('Please read the file first')
    elif option == '3':
        if (file_read == True):
            if (asf.end(file, position+1) == False):
                row, position = asf.next(file, position)
                asf.pretty_print_row(row, position)
            else:
                print('There are not more registers in that file')
        else:
            print('Please read the file first')
    elif option == '4':
        if (file_read == True):
            reg = registro()
            reg.nuevoRegistro('Anotacion 45', 45, 45, 45.0, 45.0, 45)
            asf.add(reg, file)
    elif option == '5':
        if (file_read == True):
            position = input('Put the number of the register you want to search: ')
            row, position = asf.search(position, file)
            asf.pretty_print_row(row, position)
    elif option == '6':
        if (file_read == True):
            print(file)
    elif option == '9':
        finish = True