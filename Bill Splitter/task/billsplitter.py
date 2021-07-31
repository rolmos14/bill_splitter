import random

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
        lucky_feature = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
        if lucky_feature == 'No':
            print("\nNo one is going to be lucky")
        else:
            names = list(friends.items())
            print(f"\n{random.choice(names)[0]} is the lucky one!")
