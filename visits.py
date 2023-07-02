import purchaselog


def add_funnel():
    pass


def convert_log_item(log_item):
    log_item = log_item.split(',')
    log_item[1] = log_item[1].strip()
    return log_item
    pass


def find_purchase_in_log(purchases, log_item):
    log_item = convert_log_item(log_item)
    if log_item [0] in purchases:
        return purchases[log_item[0]]
    else:
        return 0
    pass


def add_funnel(file, log_item, purchase):
    try:
        file.write(log_item.strip() + ',' + purchase + '\n')
    except:
        if purchase.__class__ == list:
            file.write(log_item.strip())
            for p in purchase:
                file.write(',' + p)
            file.write('\n')
        else:
            print(purchase.__class__)




def funnel(purchases_path, logs_path):
    visits = open(logs_path)
    purchases = purchaselog.create_dict_from_log(purchases_path)
    funnel = open("data/funnel.csv", "w")
    for row in visits:
        if (find_purchase_in_log(purchases, row) != 0):
            add_funnel(funnel, row, find_purchase_in_log(purchases, row))
    funnel.close()