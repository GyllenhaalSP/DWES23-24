# **************************
# AQUÍ TIENE SU VUELTA (MAX)
# **************************


def run(to_give_back: float, available_currencies: dict) -> dict or None:
    if to_give_back == 0:
        return {}

    sorted_currencies = sorted(available_currencies.keys(), reverse=True)

    money_back = {}
    for currency in sorted_currencies:
        max_currency_use = min(to_give_back // currency, available_currencies[currency])

        if max_currency_use > 0:
            money_back[currency] = max_currency_use
            to_give_back -= currency * max_currency_use

        if to_give_back <= 0:
            break

    if to_give_back > 0:
        return None

    return money_back


if __name__ == '__main__':
    run(20, {5: 3, 2: 7, 1: 3})