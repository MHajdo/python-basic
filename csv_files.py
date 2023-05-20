with open("resources/people.csv") as people_file:
    people_data = people_file.read().splitlines()

    for row in people_data:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}")
