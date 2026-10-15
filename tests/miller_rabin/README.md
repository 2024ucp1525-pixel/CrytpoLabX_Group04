# 512-bit Probable Prime Generation Using Miller-Rabin

## Objective
Generate a 512-bit probable prime using the Miller-Rabin
primality test and verify the result independently.

## Algorithm
1. Generate a random 512-bit integer.
2. Set its most significant bit to ensure a 512-bit length.
3. Set its least significant bit to ensure the candidate is odd.
4. Reject candidates divisible by small primes.
5. Apply the Miller-Rabin test using 40 random bases.
6. Repeat until a candidate passes all rounds.
7. Verify the bit length and check primality independently.

## Requirements
- Python 3
- SymPy for independent primality verification

Install SymPy if necessary:

    python3 -m pip install sympy

## Execution

    python3 attacks/miller_rabin/miller_rabin_512_prime.py

## Experimental Results

Run the program and record the actual results below.

| Parameter | Value |
|---|---|
| Assigned bit length | 512 |
| Generated prime candidate | Record program output |
| Actual bit length | Record program output |
| Number of candidates tested | Record program output |
| Miller-Rabin rounds for final candidate | 40 |
| Total execution time | Record program output |
| Miller-Rabin verification | Record program output |
| Independent SymPy verification | Record program output |

## Verification
The generated candidate must have exactly 512 bits, pass all
40 Miller-Rabin rounds, and pass the independent SymPy check.
