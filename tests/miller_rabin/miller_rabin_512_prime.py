#!/usr/bin/env python3
"""
Generate a 512-bit probable prime using Miller-Rabin.
Optional independent verification uses SymPy's isprime().
"""

import secrets
import time


def miller_rabin(n, bases):
    """Return (is_probable_prime, number_of_MR_rounds_performed)."""
    if n < 2:
        return False, 0
    if n in (2, 3):
        return True, 0
    if n % 2 == 0:
        return False, 0

    # Write n - 1 = 2^s * d, where d is odd.
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    rounds_done = 0
    for a in bases:
        # Bases must be in [2, n - 2].
        a = 2 + (a % (n - 3))
        x = pow(a, d, n)  # efficient modular exponentiation
        rounds_done += 1

        if x == 1 or x == n - 1:
            continue

        passed_round = False
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                passed_round = True
                break
            if x == 1:
                break

        if not passed_round:
            return False, rounds_done

    return True, rounds_done


def has_small_prime_factor(n):
    """Quickly reject candidates divisible by small primes."""
    for p in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n != p and n % p == 0:
            return True
    return False


def generate_probable_prime(bits=512, rounds=40):
    if bits < 2:
        raise ValueError("bits must be at least 2")

    candidates_tested = 0
    total_mr_rounds = 0
    start = time.perf_counter()

    while True:
        # Set the top bit to ensure exactly 'bits' bits; set low bit to ensure odd.
        candidate = secrets.randbits(bits)
        candidate |= (1 << (bits - 1))
        candidate |= 1
        candidates_tested += 1

        if has_small_prime_factor(candidate):
            continue

        bases = [secrets.randbelow(candidate - 3) + 2 for _ in range(rounds)]
        probable_prime, rounds_done = miller_rabin(candidate, bases)
        total_mr_rounds += rounds_done

        if probable_prime:
            elapsed = time.perf_counter() - start
            return candidate, bases, candidates_tested, total_mr_rounds, elapsed


def main():
    assigned_bits = 512
    rounds = 40

    prime, bases, candidate_count, total_rounds, elapsed = generate_probable_prime(
        assigned_bits, rounds
    )

    print("MILLER-RABIN 512-BIT PROBABLE PRIME GENERATOR")
    print("-" * 50)
    print("Assigned bit length:", assigned_bits)
    print("Generated probable prime candidate:", prime)
    print("Actual bit length:", prime.bit_length())
    print("Number of candidates tested:", candidate_count)
    print("Miller-Rabin rounds for final candidate:", rounds)
    print("Total Miller-Rabin rounds executed:", total_rounds)
    print("Total execution time (seconds):", f"{elapsed:.6f}")
    print("Final candidate is odd:", prime % 2 == 1)
    print("Final candidate passes Miller-Rabin:",
          miller_rabin(prime, bases)[0])
    print("Bases used for the final candidate:")
    print(bases)

    # Independent verification, if SymPy is installed.
    try:
        from sympy import isprime
        print("Independent verification (sympy.isprime):", isprime(prime))
    except ImportError:
        print("SymPy is not installed; install it with: python3 -m pip install sympy")
        print("Then rerun to perform independent verification.")


if __name__ == "__main__":
    main()
