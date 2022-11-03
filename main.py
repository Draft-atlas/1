def read_data_file(file_name):
    file_lines = []
    file = open(file_name, 'r')
    for line in file:
        file_lines.append(line)
    return file_lines


def split_line(line):
    splited_line = line.split(';')
    return splited_line


if __name__ == '__main__':
    stroki_iz_faila = read_data_file('data.csv')
    for stroka in stroki_iz_faila:
        razbitaya_stroka = split_line(stroka)
        #print(razbitaya_stroka)
        print(f'Меня зовут {razbitaya_stroka[0]} {razbitaya_stroka[1]}'
              f',мой пол {razbitaya_stroka[2]},'
              f'год моего рождения {razbitaya_stroka[3]},'
              f'можете звонить по номеру {razbitaya_stroka[4]}')