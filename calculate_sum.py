import time


def calculate_sum(a: int | float, b: int | float) -> str:
    """
    Function to calculate sum of 2 numbers.
    :param a: Number 1, Type - int/float
    :param b: Number 2, Type - int/float
    :return: String with the sum of the 2 numbers
    """
    delay()
    return f"Sum of the 2 Numbers is `{a + b}`"


def delay():
    """
    Function to introduce a 5-second delay
    :return:
    """
    print("5 Sec Delay....")
    time.sleep(5)
