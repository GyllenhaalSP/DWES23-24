# *****************
# NÚMEROS PERFECTOS
# *****************


def is_perfect(n: int) -> bool:
    def is_perfect_number(num: int) -> bool:
        return sum([i for i in range(1, num) if num % i == 0]) == num
    return is_perfect_number(n)

