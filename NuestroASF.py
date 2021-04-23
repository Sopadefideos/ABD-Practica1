from NuestroRegistro import registro
import pandas as pd 

class ASFile:
    def __init__(self):
        self.header_file = {
            'tam_head_file': 0,
            'num_registers:': 0,
            'tam_block': 0,
            'tam_head_block': 0,
            'tam_head_register': 0,
            'num_atributte_register': 0,
            'types_atributte': [],
            'tam_types_atributte': []
            }
        self.block = {
            'block_header_id': 0,
            'registers': []
        }

    def open(self, path): 
        df = pd.read_csv(path)
        print('**********************FILE***********************')
        print(df.to_string())
        print('*************************************************'+'\n')
        return df
    
    def first(self, file, pos):
        first = file.loc[[pos]]
        return first, pos

    def next(self, file, pos):
        pos += 1
        value = file.loc[[pos]]
        return value, pos

    def pretty_print_row(self, row, pos):
         print('********************* ROW '+str(pos)+' *********************')
         print(row)
         print('*************************************************'+'\n')
    
    def end(self, file, pos):
        if(len(file.index) != pos):
            return False
        else:
            return True