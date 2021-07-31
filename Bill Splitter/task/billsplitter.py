friends = dict()

try:
    num_of_friends = int(input("Enter the number of friends joining (including you):"))
except ValueError:
    print("\nNo one is joining for the party")
else:
    if num_of_friends <= 0:
        print("\nNo one is joining for the party")
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for _ in range(num_of_friends):
            friend = input()
            friends.update({friend: 0})
        bill = int(input("\nEnter the total bill value:"))
        bill_split = round(bill / num_of_friends, 2)
        for name in friends:
            friends[name] = bill_split
        print(f"\n{friends}")
