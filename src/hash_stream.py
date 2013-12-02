import hashlib, sys, base64
import main

if __name__ == "__main__":
    for line in sys.stdin.readlines():
        print(main.encode(line.strip()))