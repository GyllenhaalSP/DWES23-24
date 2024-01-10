# ****************************
# CONVIRTIENDO HTML A MARKDOWN
# ****************************


def run(html: str) -> str:
    words = html[html.find('>') + 1:html.rfind('<')]
    hash_qty = int(html[2])
    return '#' * hash_qty + ' ' + words


if __name__ == '__main__':
    run('<h1>Core</h1>')
