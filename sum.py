# main.py
import sys
import csv

def readMasses():
    # read from masses.csv
    with open('masses.csv', newline='') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
       rows = []
       for row in spamreader:
           rows.append(row)
    keys = rows[0][0].split(',')
    values = rows[1][0].split(',')
    massDict = {keys[i] : values[i] for i in range(len(keys))}
    return massDict    

if __name__ == "__main__":
    arglen = len(sys.argv)
    if arglen != 2:
        print("Usage: python sum.py <target mass sum>")
        quit(0)
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    massDict = readMasses()
    print(massDict)


           
