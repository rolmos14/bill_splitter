# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# Initialize dictionary with Key : None
group_kids = dict.fromkeys(groups)

num_of_groups = int(input())
for group_idx in range(num_of_groups):
    group_kids[groups[group_idx]] = int(input())

print(group_kids)
