import statistics


def average(arr):
    return format(statistics.mean(set(arr)), ".3f")


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    input()
