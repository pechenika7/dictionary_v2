dict_file = open('dict.txt',  'r', encoding='utf8')

eng_rus = list()
while True:
    item = dict_file.readline()
    if item == '' or item == '\n':
        break
    temp_list = item.split(';')
    eng_rus.append({temp_list[0]: temp_list[1].strip()})
count_words = len(eng_rus)
dict_file.close

print(eng_rus)

print(eng_rus[0][words_on_page*(current-1)+i], '-', eng_rus[1][words_on_page*(current-1)+i])