fr = open("texts", "rt")

for i in fr:
    if "a61" in i:
        print("a61")
    if "a62" in i:
        print("a62")
    elif "a63" in i:
        print("a63")