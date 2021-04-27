from NuestroRegistro import registro
import pandas as pd


class ASFile:
    def __init__(self):
        self.header_file = {
            "tam_head_file": 0,
            "num_registers:": 0,
            "tam_block": 0,
            "tam_head_block": 0,
            "tam_head_register": 0,
            "num_atributte_register": 0,
            "types_atributte": [],
            "tam_types_atributte": [],
        }
        self.block = {"block_header_id": 0, "registers": pd.DataFrame()}

    def open(self, path):
        df = pd.read_csv(path)
        self.block["registers"] = df
        self.block["registers"]["status"] = 0
        self.list()

    def first(self):
        file = self.block["registers"]
        first = file.loc[[0]]
        return first, 0

    def next(self, pos):
        pos += 1
        value = self.block["registers"].loc[[pos]]
        return value, pos

    def pretty_print_row(self, row, pos):
        print("********************* ROW " + str(pos) + " *********************")
        print(row)
        print("*************************************************" + "\n")

    def end(self, pos):
        if len(self.block["registers"].index) != pos:
            return False
        else:
            return True

    def add(self, register):
        self.block["registers"].loc[len(self.block["registers"].index)] = [
            register.anotacion,
            register.val1,
            register.val2,
            register.val3,
            register.val4,
        ]

    def search(self, pos):
        if len(self.block["registers"].index) > int(pos) and int(pos) >= 0:
            value = self.block["registers"].loc[[int(pos)]]
            return value, int(pos)

    def modify(self, register, pos):
        self.block["registers"].loc[pos] = [
            register.anotacion,
            register.val1,
            register.val2,
            register.val3,
            register.val4,
        ]

    def delete(self, pos):
        newfile = self.block["registers"].drop(labels=int(pos), axis=0)
        self.block["registers"] = newfile

    def list(self):
        simple_file = self.block["registers"].iloc[:, 0:5]
        print("**********************FILE***********************")
        print(simple_file)
        print("*************************************************" + "\n")

    def list_row(self):
        print("**********************FILE******************************")
        print(self.block["registers"])
        print("********************************************************" + "\n")
