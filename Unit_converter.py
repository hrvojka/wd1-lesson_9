print("Hy, the purpose of this program is to convert km to miles..")

while True:
    km = input("Enter km: ")
    km = float(km.replace(",","."))
    miles = km * 0.62137119224
    print(f"Miles: {miles}")
    question = input("Continue (y/n): ").lower()
    if question == "n":
        print("Goodbye..")
        break
    else:
        while question != "y" and question != "n":
            question = input("Enter y for yes and n for no: ").lower()
        if question == "n":
            print("Goodbye..")
            break

