# ****************
# TODO SON CARITAS
# ****************


def run(emoji_text: str) -> str:
    emoji_text_lower = emoji_text.lower()

    match emoji_text_lower:
        case 'happy':
            return '😀'
        case 'sad':
            return '😔'
        case 'angry':
            return '😡'
        case 'pensive':
            return '🤔'
        case 'surprised':
            return '😮'


if __name__ == '__main__':
    run('happy')
