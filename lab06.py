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
    return decoded_password


def main():
    password = input("Please input your 8-digit passcode")
    print(encode(password))


main()
