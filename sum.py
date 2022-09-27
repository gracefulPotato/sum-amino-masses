# main.py
import sys
import csv
import pprint

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
    #print(n)
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
    if arglen != 3:
        print("Usage: python sum.py <target mass sum> <amino sequence length")
        quit(0)
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    target_mass = float(sys.argv[1])
    num_aminos = int(sys.argv[2])

    massDict = readMasses()
    massDict = orderDict(massDict)
    print(massDict)
    roundedMassDict = {}
    #massList = massDict.values()
    #roundedMassList = []
    #for m in massList:
        #roundedMassDict[] =
        #roundedMassList.append(int(m))
    massKeys = list(massDict.keys())
    massValues = list(massDict.values())
    roundedMassDict = {massKeys[i] : int(massValues[i]) for i in range(len(massKeys))}
    roundedMassList = roundedMassDict.values()
    combinations = find_changes(target_mass,roundedMassList)
    answer = []
    for c in combinations:
        mass_sum = 0
        #answer.append(c)
        if len(c) == num_aminos:
            amino_super = [[]]
            aminos = []
            aminos2 = []
            doppelganger = 0#False
            for mass in c:
                if mass == 113 or mass == 128:
                    doppelganger += 1#True
                    old_length = len(amino_super)
                    for i in range(old_length):
                        new_amino_list = []
                        for a in amino_super[i]:
                            new_amino_list.append(a)
                        amino_super.append(new_amino_list)
                    #for a in amino_super[0]:
                    #    amino_super[len(amino_super)].append(a)
                    if mass == 113:
                        for i in range(len(amino_super)):
                            if i<len(amino_super)/2:
                                amino_super[i].append('Ile')
                            else:
                                amino_super[i].append('Leu')
                        continue
                    elif mass == 128:
                        for i in range(len(amino_super)):
                            if i<len(amino_super)/2:
                                amino_super[i].append('Gln')
                            else:
                                amino_super[i].append('Lys')
                        continue
                for amino in roundedMassDict:
                    if roundedMassDict[amino] == mass:
                        for aminos_list in amino_super:
                            aminos_list.append(amino)
                            
                        #aminos.append(amino)
                        #if doppelganger:
                         #   aminos2.append(amino)
            for aminos_list in amino_super:
                answer.append(aminos_list)
                #answer.append(mass_sum)
            #if doppelganger:
                #answer.append(aminos2)
    pprint.pprint(answer)

           
