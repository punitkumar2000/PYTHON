Client_List = {1: "Harry", 2: "Rohan", 3: "Hammad"}
Log_List = {1: "Exercise", 2: "Diet"}

def getdate():
    import datetime
    return datetime.datetime.now()

try:
    print("Select Client Name:")
    for key, value in Client_List.items():
        print("Press", key, "for", value, "\n", end="")
    client_name = int(input("Enter Here:"))

    print("Selected Client : ", Client_List[client_name], "\n", end="")

    print("Press 1 for Log-")
    print("Press 2 for Retrieve-")
    op = int(input("Enter Here:"))

    if op == 1:
        for key, value in Log_List.items():
            print("Press", key, "to log", value, "\n", end="")
        log_name = int(input("Enter here:"))

        print("Selected Job : ", Log_List[log_name])
        f = open(Client_List[client_name] + "_" + Log_List[log_name] + ".txt", "a")
        k = 'y'
        while(k != "n"):
            print("Enter", Log_List[log_name], "\n", end="")
            mytext = input()
            f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
            k = input("ADD MORE ? y/n:")
            continue
        f.close()

    elif op == 2:
        for key, value in Log_List.items():
            print("Press", key, "to Retrieve", value,"\n", end="")
        log_name = int(input("Enter Here:"))

        print(Client_List[client_name], "-", Log_List[log_name], "Report : ", "\n", end="")
        f = open(Client_List[client_name] + "_" + Log_List[log_name] + ".txt", "rt")
        contents = f.readlines()
        for line in contents:
            print(line, end="")
        f.close()

    else:
        print("Invalid Input !!!")

except Exception as e:
    print("Wrong Input !!!")