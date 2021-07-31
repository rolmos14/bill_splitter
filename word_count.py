with open("file_name.txt", "r") as file:
    # Read the file and remove '\n' at the end of each line
    lines = list(map(str.strip, file.readlines()))
    summer_occurrences = len(list(filter(lambda word: word == "summer", lines)))
    print("Summer appears " + str(summer_occurrences) + " times.")
