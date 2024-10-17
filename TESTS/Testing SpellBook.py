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

