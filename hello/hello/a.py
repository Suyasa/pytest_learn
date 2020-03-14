def main():
    a, b = map(int, input().split())
    print('Odd' if (a * b) % 2 else 'Even')


def wrong():
    a, b = map(int, input().split())
    print('Even' if (a * b) % 2 else 'Odd')


if __name__ == '__main__':
    main()
