# ********************
# AQUÍ TIENE SU VUELTA
# ********************


def run(to_give_back: float, available_currencies: list) -> dict or None:
    if to_give_back == 0:
        return {}

    available_currencies.sort(reverse=True)

    money_back = {}

    for currency in available_currencies:
        if to_give_back >= currency:
            count = to_give_back // currency
            money_back[currency] = count
            to_give_back -= currency * count

    if to_give_back != 0:
        return None

    return money_back


if __name__ == '__main__':
    run(20, [5, 2, 1])
