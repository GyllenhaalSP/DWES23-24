# *****************
# FICHO CUANDO TOCA
# *****************
from datetime import datetime, timedelta


def run(time: str, offset: int) -> str:
    time = datetime.strptime(time, '%H:%M')
    time = time + timedelta(minutes=offset)
    time = time.strftime('%H:%M') if time.hour >= 10 else time.strftime('%H:%M').removeprefix('0')
    return time


if __name__ == '__main__':
    run('17:15', 240)