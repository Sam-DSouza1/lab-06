def encode(password):
    out = ""
    for s in password:
        s = str(int(s) + 3)
        out += s[-1]
    return out


def decode(encoded_password):
    arr = []
    decoded_password = ""
    for i in password:
        arr.append(int(i))
    for j in arr:
        j -= 3
        decoded_password += str(j)
    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")



def main():
    while(True):
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")
        if option == "1":
            password = input("Please input your password to encode")
            print(encode(password))
            print("Your password has been encoded and stored")
        elif option == "2":
            password = input("Please input your password to decode")
        elif option == "3":
            break


main()
