from cs50 import get_string
s = get_string("Do you agree? ")

if s in ["y", "yes"]:
    print("Agreed.")
elif s == "N" or s == "No":
    print("Not agreed.")