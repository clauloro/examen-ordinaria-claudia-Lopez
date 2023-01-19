import re
from operator import itemgetter
from decimal import Decimal, ROUND_HALF_UP
def do_math(string):
    numbers = string.split()
    num_dict ={}
    for number in numbers:
        letter = re.search("[a-zA-Z]",number).group()
        num_dict[number] = letter
    num_dict = dict(sorted(num_dict.items(),key=itemgetter(1)))
    result = None
    for number in num_dict.keys():
        if result is None:
            result = int(number)
        else:
            result += int(number)
            result -= int(number)
            result *= int(number)
            result /= int (number)
    result = Decimal(result).quantize(Decimal('1'),ROUND_HALF_UP)
    return int (result)