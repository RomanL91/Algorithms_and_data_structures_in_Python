class KMP:
    """Алгоритм Кнута — Морриса — Пратта (КМП-алгоритм) — эффективный алгоритм, 
    осуществляющий поиск подстроки в строке, используя то, что при возникновении 
    несоответствия само слово содержит достаточно информации, 
    чтобы определить, где может начаться следующее совпадение, 
    минуя лишние проверки.
    """
    def __init__(self) -> None:
        pass


    def _get_list_for_shift_by_prefixes(self, substring):
        """вернет список смещения префиксов для алгоритма.

        Args:
            substring (str): искомая пордстрока.

        Returns:
            list: список индексов.
        """
        list_for_shift_by_prefixes = [0] * len(substring)
        prefix_ind = 0
        suffix_ind = 1

        while suffix_ind < len(substring):
            if substring[prefix_ind] == substring[suffix_ind]:
                list_for_shift_by_prefixes[suffix_ind] = prefix_ind + 1
                prefix_ind += 1
                suffix_ind += 1
            else:
                if prefix_ind == 0:
                    list_for_shift_by_prefixes[suffix_ind] = 0
                    suffix_ind += 1
                else:
                    prefix_ind = list_for_shift_by_prefixes[prefix_ind - 1]
        
        return list_for_shift_by_prefixes
    

    def find_substring(self, string, substring):
        """найдет подстроку в строке.

        Args:
            string (str): строка в которой будет происходить поиск
            substring (str): искомая подстрока.

        Returns:
            bool: истина - если подстрока есть в строке, иначе - ложь.
        """
        ptr_1 = 0
        ptr_2 = 0
        list_for_shift_by_prefixes = self._get_list_for_shift_by_prefixes(substring)

        while ptr_1 < len(string):
            if string[ptr_1] == substring[ptr_2]:
                ptr_1 += 1 
                ptr_2 += 1
                if ptr_2 == len(substring):
                    print(f'[==INFO==] подстрока {substring} найдена в {string}.')
                    return True
            else:
                if ptr_2 > 0:
                    ptr_2 = list_for_shift_by_prefixes[ptr_2 - 1]
                else:
                    ptr_1 += 1

        if ptr_1 == len(string) and ptr_2 != len(substring):
            print(f'[==INFO==] подстрока {substring} не найдена в {string}.')
            return False


if __name__ == '__main__':
    string = 'лилилось лилилась'
    substring = 'лилила'
    kmp = KMP()
    kmp.find_substring(string=string, substring=substring)
