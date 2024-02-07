class BMH:

    def __init__(self) -> None:
        pass


    def get_table_of_offsets(self, substring):
        table_of_offsets = {}
        for indx, char in enumerate(substring[::-1]):
            if indx == 0:
                continue
            if char in table_of_offsets:
                continue
            table_of_offsets.setdefault(char, indx)
        table_of_offsets.setdefault(substring[-1], len(substring))
        table_of_offsets.setdefault('*', len(substring))
            
        print(table_of_offsets)
        return table_of_offsets


    def find_substring(self, string, substring):
        if len(substring) > len(string):
            return False
        table_of_offsets = self.get_table_of_offsets(substring)
        offset = len(substring)
        for indx, char in enumerate(string):
            if substring[offset] != string[offset]:
                try:
                    offset += table_of_offsets[char]
                except KeyError:
                    offset += table_of_offsets['*']
            else:
                offset -=1


if __name__ == '__main__':
    string =    'большие метеоданные'
    substring =       'данные'
    bmh = BMH()
    bmh.get_table_of_offsets(substring=substring)
