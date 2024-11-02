def initialize_key_amounts():
    Default_Key_Count_Remaining = {}

    Letter_Amounts_File = open('states/battle_data/Letter_Amount.txt' , "r")
    Letter_Amounts_File_Lines = Letter_Amounts_File.readlines()

    for line in Letter_Amounts_File_Lines:
        letter_count = line[0]
        letter_amount = line[2]
        Default_Key_Count_Remaining[letter_count] = int(letter_amount)
    print(Default_Key_Count_Remaining)
    Letter_Amounts_File.close()

initialize_key_amounts()