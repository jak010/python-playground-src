from __future__ import annotations

from typing import Optional, Tuple, Union


def divide(x: float, y: float) -> float | ZeroDivisionError:
    if y == 0:
        return ZeroDivisionError("Cannot divide by 0")
    return x / y


result = divide(1, 0)

if isinstance(result, ZeroDivisionError):
    raise result

print(f"Dividend is: {result}")
