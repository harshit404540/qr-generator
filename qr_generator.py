import qrcode as qr

def qr_code_creator():
    try:
        user = input("Enter QR data: ")
        qr_code_filename = input("Enter QR Filename: ")
        path = input("Enter Path (Ex - C/User/qr or just press Enter to save in current working directory...): ")
        qr_code = qr.make(user)
        qr_code.save(path + "/" + qr_code_filename + ".png")
        print("\nQR created Successfully...")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    while True:
        ch = int(input("Enter 1 to create QR or 2 for Exiting: "))
        if ch == 1:
            qr_code_creator()
        elif ch == 2:
            print("Good Bye...")
            break
        else:
            print("Wrong Input...")