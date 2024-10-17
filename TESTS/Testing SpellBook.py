text_key_inputs = open("TESTS/Letters.txt", "r")
keys_inputs = text_key_inputs.read() 
keys = keys_inputs.split("\n")
text_key_inputs.close()


def Test_Key_Input(pressed_key:str, valid_keys:list = keys, ):
    
    match pressed_key:
        case pressed_key if pressed_key in valid_keys:
            print("You pressed", pressed_key)
        case _:
            print("Not a valid Key")

class Keyboard:
    def __init__(self):
        pass
    def key_amounts(self):
        self.Key_Amounts = {}

        self.Letter_Amounts_File = open('TESTS/Letter Amounts.txt' , "r")
        self.Letter_Amounts_File_Lines = self.Letter_Amounts_File.readlines()

        for line in self.Letter_Amounts_File_Lines:
            self.letter_count = line[0]
            self.letter_amount = line[2]
            self.Key_Amounts[self.letter_count] = self.letter_amount

        self.Letter_Amounts_File.close


keyboard = Keyboard()

keyboard.key_amounts()

print(keyboard.Key_Amounts)
