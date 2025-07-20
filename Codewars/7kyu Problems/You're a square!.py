import math
def is_square(n):
    if n < 0:
        return False
    else:
        root = math.sqrt(n)
        return root * root == n