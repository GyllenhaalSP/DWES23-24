# *****************
# COMBINANDO TECLAS
# *****************


def run(key1: str, key2: str, key3: str) -> str:
    match (key1, key2, key3):
        case ('CTRL', 'ALT', 'T'):
            return 'Open terminal'
        case ('CTRL', 'ALT', 'L'):
            return 'Lock screen'
        case ('CTRL', 'ALT', 'D'):
            return 'Show desktop'
        case ('ALT', 'F2', ''):
            return 'Run console'
        case ('CTRL', 'Q', ''):
            return 'Close window'
        case ('CTRL', 'ALT', 'DEL'):
            return 'Log out'


if __name__ == '__main__':
    run('CTRL', 'ALT', 'T')
