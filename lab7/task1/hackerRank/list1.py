n = int(input())
my_list = []
for i in range(n):
    command = input().split()
    
    match command[0]:
        case "insert":
            ind = int(command[1])
            elem = int(command[2])
            my_list.insert(ind, elem)
        case "print":
            print(my_list)
        case "remove":
            elem = int(command[1])
            my_list.remove(elem)
        case "append":
            elem = int(command[1])
            my_list.append(elem)
        case "sort":
            my_list.sort()
        case "pop":
            my_list.pop()
        case "reverse":
            my_list.reverse()

