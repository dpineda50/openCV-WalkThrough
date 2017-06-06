import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-i", required = True,
                help = "The input must be a number from 1-10 inclusive.")
args = vars(ap.parse_args())

print("your input " + str(args["i"]))

x = args["i"]
if x <= 0:
    print("This is unacceptable input")
elif x <= 5:
    print("This is in the lower half")
elif x <= 11:
    print("This is in the upper half")
else:
    print("OUT OF BOUNDS")

