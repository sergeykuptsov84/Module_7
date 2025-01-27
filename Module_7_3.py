import os
import string

class WordsFinder:

    def __init__(self,my_dir, *name_txt):
        self.my_dir = my_dir
        self.name_txt = name_txt

    def file_write(self, file_name, *args):
        os.chdir(self.my_dir)
        strings = ''.join(args)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.writelines(strings)
        return  strings

    def get_all_words(self,file_name, *args):
        self.file_name = file_name
        os.path.basename(file_name)
        with open(file_name, 'r', encoding="utf-8") as file:
            file_words = (''.join([char.lower() for char in file if char not in string.punctuation])).split()

        name_ = str(self.file_name)
        all_words = {name_: file_words}
        return all_words

    def find(self, word):
        self.word = word
        for name, words in self.get_all_words(self.file_name).items():
            value_word = (words.index(word.lower()))
            one_word_dict = {name: value_word}
            return one_word_dict

    def count(self,word):
        self.word = word
        for name, words in self.get_all_words(self.file_name).items():
            count_word = (words.count(word.lower()))
            count_word_dict = {name: count_word}
            return count_word_dict


test_file = ["It is a text for task Найти везде,\n"
             "Используйте его для самопроверки.\n"
             "Успехов в решении задачи.\n"
             "text text text\n"
            ]

finder2 = WordsFinder("C:\PythonProject", *test_file )
finder2.file_write('test_file.txt', *test_file) # Запись файла
print(finder2.get_all_words('test_file.txt')) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте