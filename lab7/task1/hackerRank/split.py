def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    print(line)


line = input()
split_and_join(line)