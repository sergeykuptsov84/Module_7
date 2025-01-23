def  custom_write(file_name, *args):
    strings = ''.join(args)
    file = open(file_name, 'w', encoding='utf-8')
    file.writelines(strings)
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    byte_number = [0,]
    while file.readline():
        byte_number.append(file.tell())
    file.close()
    file = open(file_name, 'r', encoding='utf-8')
    line_index = []
    string_items = []
    for i, j in enumerate(file.readlines()):
        line_index.append((i + 1))
        string_items.append(j)
    file.close()
    string_items = [line.rstrip() for line in string_items]
    keys_ = list(zip(line_index, byte_number))
    strings_positions = dict(zip(keys_, string_items))
    return strings_positions


info = [
    'Text for tell.\n',
    'Используйте кодировку utf-8.\n',
    'Because there are 2 languages!\n',
    'Спасибо!\n',
    ]

result = custom_write('text_7_2.txt', *info)
for elem in result.items():
    print(elem)

