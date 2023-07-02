import json


def create_dict_from_log(path):
    file = open(path, encoding='utf-8')
    lines = file.readlines()[1:] #Без заголовка
    dict = {}

    for row in lines:
        dict_i = {}
        dict_i = json.loads(row)
        try:
            #В файле есть совпадения по user_id, чтобы не потерять данные будем менять на ходу тип данных на массив
            if dict_i['user_id'] in dict and dict.get(dict_i['user_id']) is not None:
                l = dict[dict_i['user_id']]
                dict[dict_i['user_id']] = []
                dict[dict_i['user_id']].append(l)
                dict[dict_i['user_id']].append(dict_i['category'])
            else:
                dict[dict_i['user_id']] = dict_i['category']
        except:
            pass
    return dict
