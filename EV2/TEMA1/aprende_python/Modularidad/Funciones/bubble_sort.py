# **********************
# ORDENANDO CON BURBUJAS
# **********************


def bubble(items: list) -> list:
    ordered_list = items[:]
    lst_len = len(ordered_list)
    for i in range(lst_len):
        for j in range(0, lst_len - i - 1):
            if ordered_list[j] > ordered_list[j + 1]:
                ordered_list[j], ordered_list[j + 1] = ordered_list[j + 1], ordered_list[j]

    return ordered_list

