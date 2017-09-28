import pandas as pd

class DataGetter():
    def __init__(self):
        self.test = pd.read_excel('test.xlsx')
        self.NAME = []
        self.NUMBER = []

    def get_name(self):
        for x in self.test['类型']:
            self.NAME.append(x)
        return self.NAME

    def get_number(self):
        for x in self.test['具体数目']:
            self.NUMBER.append(x)
        return self.NUMBER