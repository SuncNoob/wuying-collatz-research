#!/usr/bin/env python3
"""
Collatz conjecture finite verification for n = 1..10000.
Prints OK if all sequences reach 1.
"""

def collatz_steps(n: int) -> int:
    """Return the number of steps for n to reach 1 under the Collatz map."""
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def main():
    limit = 10000
    max_steps = 0
    max_n = 0
    for n in range(1, limit + 1):
        s = collatz_steps(n)
        if s > max_steps:
            max_steps = s
            max_n = n
    print(f"Verified n = 1..{limit}. Max steps = {max_steps} (at n = {max_n}).")
    print("OK")

if __name__ == "__main__":
    main()
