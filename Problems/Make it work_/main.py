first, second = [int(input()) for _ in range(2)]

if first > second:
    print("The first one wins")
elif second > first:
    print("The second one wins")
else:
    print("Draw")
