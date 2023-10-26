def encode(password):
    out = ""
    for s in password:
        s = str(int(s) + 3)
        out += s[-1]
    return out


def main():
    password = input("Please input your 8-digit passcode")
    print(encode(password))


main()
