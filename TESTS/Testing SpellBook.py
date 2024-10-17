Key_Updater = {}

Letter_Positions_File = open('TESTS/Letter Positions.txt' , "r")
Letter_Positions_File_Lines = Letter_Positions_File.readlines()

for line in Letter_Positions_File_Lines:
    letter = line[0]
    if letter == "p":
        position_x = int(line[4:8])
        position_y = int(line[10:13])
    else: 
        position_x = int(line[4:7])
        position_y = int(line[9:12])

    Key_Updater[letter] = (position_x, position_y)

print(Key_Updater)

Letter_Positions_File.close()
