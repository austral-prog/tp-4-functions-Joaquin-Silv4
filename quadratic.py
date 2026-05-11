# Replace the "ANSWER HERE" for your answer
import math


def roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return "( )"
    elif discriminant == 0:
        r = -b / (2 * a)
        return f"({r})"
    else:
        r1 = (-b + math.sqrt(discriminant)) / (2 * a)
        r2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"({r1}, {r2})"


def value_y(a, b, c, x):
    return a*x**2 + b*x + c


def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    if a == 0:
        return f"f(x) = {b} * X + {c}"
    if b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    return f"f(x) = {a} * X^2 + {b} * X + {c}"

def derivation(a, b, c):
    deriv_a = 2 * a
    if deriv_a == 0 and b == 0:
        return "f'(x) = 0"
    if deriv_a == 0:
        return f"f'(x) = {b}"
    if b == 0:
        return f"f'(x) = {deriv_a} * X"
    return f"f'(x) = {deriv_a} * X + {b}"
