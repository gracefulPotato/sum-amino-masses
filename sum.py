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

def orderDict(unsortedDict):
    # convert elements from strings to floats
    # order the elements by value
    massDict = {}
    for key,value in unsortedDict.items():
        massDict[key] = float(value)
        
    sorted_values = sorted(massDict.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in massDict.keys():
            if massDict[k] == i:
                sorted_dict[k] = massDict[k]
    return sorted_dict

def find_changes(n, coins):
    print(n)
    if n < -1:
        return []
    if n < 1:
         return [[]]
    all_changes = []

    for last_used_coin in coins:
        combos = find_changes(n - last_used_coin, coins)
        for combo in combos:
            combo.append(last_used_coin)
            all_changes.append(combo)

    return all_changes

if __name__ == "__main__":
    arglen = len(sys.argv)
    if arglen != 2:
        print("Usage: python sum.py <target mass sum>")
        quit(0)
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    target_mass = float(sys.argv[1])

    massDict = readMasses()
    massDict = orderDict(massDict)
    print(massDict)
    massList = massDict.values()
    roundedMassList = []
    for m in massList:
        roundedMassList.append(int(m))
    combinations = find_changes(target_mass,roundedMassList)
    print(combinations)

           
