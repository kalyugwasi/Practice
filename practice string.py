import sys
input = sys.stdin.readline

def is_kth_deletable(arr, k, bad_val):
    l = 0
    r = len(arr) - 1
    while l < r:
        if arr[l] == arr[r]:
            l += 1
            r -= 1
        else:
            if arr[l] == bad_val:
                l += 1
            elif arr[r] == bad_val:
                r -= 1
            else:
                return False
    return True

def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))

        l = 0
        r = n - 1
        while l < r and a[l] == a[r]:
            l += 1
            r -= 1
        
        if l >= r:
            print("YES")
            continue

        # Try removing a[l] or a[r] completely to make it a palindrome
        if is_kth_deletable(a[l:r+1], k, a[l]) or is_kth_deletable(a[l:r+1], k, a[r]):
            print("YES")
        else:
            print("NO")

solve()
