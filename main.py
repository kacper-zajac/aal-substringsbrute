import sys


file = open("data.txt", "r")
data_line = file.readline()

while data_line != "":
    data_line = data_line.strip("\n")
    data = data_line.strip(" ")

    number = int(data[0])   #ile bledow moze byc w podciagu
    string1 = data[1]       #pierwszy ciag
    string2 = data[2]       #drugi ciag

    length1 = len(string1)
    length2 = len(string2)

    iterator1 = 0
    iterator2 = 0
    iterator_mistakes = 0
    while iterator1 < length1:
