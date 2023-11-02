from shutil import copy2
def save_dict(eng_rus, path='dict.txt'):
    cw = len(eng_rus) #cw - count words
    f = open(path, 'w', encoding='utf8')
    for i in range(cw):
        print(eng_rus[i].keys())
        temp = eng_rus[i].keys()[0] + ';' + eng_rus[i][eng_rus[i].keys()[0]] + '\n'
        f.write(temp)
    f.close
    return cw


def back_up(current_user, user_dict, eng_rus):
    if user_dict[2][current_user] == 2:
        cw = save_dict(eng_rus, 'dict.bak')
        return cw
    else:
        print("Access denied- you don't have permission.")
        return -1


def restore(current_user, user_dict):
    if user_dict[2][current_user] == 2:
      print('Restore completed')
      copy2('dict.bak', 'dict.txt')
    else:
        print("Access denied- you don't have permission.")