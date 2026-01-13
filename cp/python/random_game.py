import sys

input = sys.stdin.readline
def flush_print(s):
    print(s)
    sys.stdout.flush()

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    def solver(n):
        if n % 2 == 0:
            flush_print("\t/2")
            return n // 2
        else:
            if (n - 1) % 4 == 0 or n == 1:
                flush_print("\t-1")
                return n - 1
            else:
                flush_print("\t+1")
                return n + 1

    def can_win(n):
        # Rick wins if number of 1's in binary is odd
        return bin(n).count('1') % 2 == 1

    if not can_win(n):
        flush_print("Lose")
        response = int(sys.stdin.readline().strip())
        if response == "WA":
            exit()
        else:
            continue
    else:
        flush_print("Win")

    while True:
        n = solver(n)
        if n == 0:
            result = sys.stdin.readline()
            if result != "GG":
                exit()
            break

        response = sys.stdin.readline().strip()
        if response == "GG":
            break
        elif response == "WA":
            exit()
        elif response == "+1":
            n += 1
        elif response == "-1":
            n -= 1
        elif response == "/2":
            n //= 2
