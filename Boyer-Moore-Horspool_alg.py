class BMH:
    """Алгоритм Бойера — Мура — Хорспула — алгоритм поиска подстроки в строке.
    Алгоритм использует только сдвиги плохих символов, при этом за такой символ 
    берётся символ из исходного текста, который соответствует последнему 
    символу шаблона, независимо от того, где случилось несовпадение.
    """

    def __init__(self) -> None:
        pass


    def _get_table_of_offsets(self, substring: str) -> dict:
        """получите таблицу смешений, благодаря которой
        будем смещать подстроку в строке и поиска совпадений.

        Args:
            substring (str): искомая подстрока.

        Returns:
            dict: таблица смешений.
        """
        table_of_offsets = {}
        for indx, char in enumerate(substring[::-1]):
            if indx == 0:
                continue
            if char in table_of_offsets:
                continue
            table_of_offsets.setdefault(char, indx)
        table_of_offsets.setdefault(substring[-1], len(substring))
        table_of_offsets.setdefault('*', len(substring))
            
        return table_of_offsets


    def find_substring(self, string: str, substring: str) -> bool:
        """выполняем поиск подстроки в строке.

        Args:
            string (str): строка, в которой будет произведен поиск.
            substring (str): искомая подстрока

        Returns:
            bool: истина - если подстрока есть в строке, иначе ложь.
        """
        len_string = len(string)
        len_substring = len(substring) 
        if len_substring > len_string:
            print(f'[==INFO==] Подстрока не найдена.')
            return False
        table_of_offsets = self._get_table_of_offsets(substring)
        ptr_char_check_string = len_substring - 1
        while ptr_char_check_string < len_string:
            ptr_k = 0 
            ptr_j = 0
            break_flag = False
            for ptr_j in range(len_substring-1, -1, -1):
                if string[ptr_char_check_string-ptr_k] != substring[ptr_j]:
                    if ptr_j == ptr_char_check_string:
                        offset = table_of_offsets[
                            string[ptr_char_check_string]
                        ] if table_of_offsets.get(
                            string[ptr_char_check_string], False
                        ) else table_of_offsets['*']
                    else:
                        offset = table_of_offsets[substring[ptr_j]]
                    
                    ptr_char_check_string += offset
                    break_flag = True
                    break
                
                ptr_k += 1

            if not break_flag:
                print(f'[==INFO==] Подстрока найдена по индексу {ptr_char_check_string - ptr_k + 1}.')
                return True
        else:
            print(f'[==INFO==] Подстрока не найдена.')
            return False
        

if __name__ == '__main__':
    string = 'большие метеоданные'
    substring = 'данные'
    bmh = BMH()
    bmh.find_substring(string, substring)
