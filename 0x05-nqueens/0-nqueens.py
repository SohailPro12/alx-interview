#!/usr/bin/python3
"""
N Queens problem
"""


if __name__ == "__main__":
    import sys
    n = sys.argv[1]
    if len(sys.argv) != 2:
        print("Usage: python n_queens.py N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
