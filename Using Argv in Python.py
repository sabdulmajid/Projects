# Using Argv in Python.py
import sys

if len(sys.argv) != 2:
    print("missing a command-line argument")
    sys.exit(1)

print(f"hello, {sys.argv[1]}")
sys.exit(0)