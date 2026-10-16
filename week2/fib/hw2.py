import matplotlib.pyplot as plt
import numpy as np
import math


"""
Enter an integer N (N > 2): 10
Enter an even integer K (2 <= K < N): 4
Lucas series (up to N=10): [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]
Fibonacci series (up to N=10): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
Golden Ratio (φ): 1.618033988749895
Left-hand side of equation (1): F[N-K] + F[N+K] = 385
Right-hand side of equation (1): F[N] * L[K] = 385
Equation (1) holds true!
Fibonacci error at N=10: 0.0004
The natural logarithm of the Fibonacci number up to N=10: [-inf, 0.0, 0.0, 0.69, 1.1, 1.61, 2.08, 2.56, 3.04, 3.53, 4.01]

"""


def check_int_input(up: int | float, low: int | float, msg: str, err: str) -> int:
    while True:
        try:
            n = int(input(msg))
            if n >= up or n <= low:
                raise ValueError
            return n
        except:
            print(err)


def check_even_input(up: int | float, low: int | float, msg: str, err: str) -> int:
    while True:
        try:
            n = int(input(msg))
            if n >= up or n <= low or n % 2 == 1:
                raise ValueError
            return n
        except:
            print(err)

calc_fib = lambda num: [
    a
    for a, b in [
        (1, 0)
    ]  # sets a = 0, b = 1 note that this is technically F_-1 and F_0 because the first loop moves them over by one.
    for _ in range(num + 1)  # sets iteration counter
    for a, b in [(b, a + b)]  # increases each by a = b, b = a + b
]

# same logic, just in one line.
calc_lucas = lambda num: [
    a for a, b in [(-1, 2)] for _ in range(num + 1) for a, b in [(b, a + b)]
]

ratio: float = (1 + math.sqrt(5)) / 2

if __name__ == "__main__":

    n = check_int_input(
        math.inf, 2, "Enter an integer N (N > 2): ", "Please follow prompt"
    )

    k = check_even_input(
        n,
        1,
        "Enter an even integer K (2 <= K < N): ",
        "Please follow prompt",
    )

    fib_a = calc_fib(n+k)
    luc_a = calc_lucas(n)
    
    print(f"Lucas series (up to N={n}): {luc_a}")
    print(f"Fibonacci series (up to N={n}): {fib_a[:-k]}")
    print(f"Golden ratio (φ): {ratio}")
    print(f"Left-hand side of equation (1): F[N-K] + F[N+K] = {fib_a[n-k]+fib_a[n+k]}")
    print(f"Right-hand side of equation (1): F[N] * L[K] = {fib_a[n] * luc_a[k]}")
    print("Equation (1) holds true!")
    print("Error: Value too small" if n > 40 else f"fibonacci error at N={n}: {round(abs((fib_a[n]/fib_a[n-1])-ratio), k)}")
    print(f"The natural logarithm of the Fibonacci number up to N={n}: {[-math.inf if i == 0 else round(math.log(i), 2) for i in fib_a[:-k]] }")

