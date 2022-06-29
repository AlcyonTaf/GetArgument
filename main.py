# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sys.argv)
    f = open("output.txt", "w")
    f.write(str(sys.argv))
    f.close()


