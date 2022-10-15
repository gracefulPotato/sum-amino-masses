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
    massKeys = list(massDict.keys())
    massValues = list(massDict.values())
    roundedMassDict = {massKeys[i] : int(massValues[i]) for i in range(len(massKeys))}
    roundedMassList = roundedMassDict.values()
    combinations = find_changes(target_mass,roundedMassList)
    answer = []
    true_masses = []
    for c in combinations:
        if len(c) == num_aminos:
            amino_super = [[]]
            true_mass_list = [0]
            for mass in c:
                if mass == 113 or mass == 128:
                    old_length = len(amino_super)
                    for i in range(old_length):
                        new_amino_list = []
                        new_mass = 0
                        
                        for a in amino_super[i]:
                            new_amino_list.append(a)
                        new_mass += true_mass_list[i]
                        amino_super.append(new_amino_list)
                        true_mass_list.append(new_mass)
                    if mass == 113:
                        for i in range(len(amino_super)):
                            if i<len(amino_super)/2:
                                amino_super[i].append('Ile')
                            else:
                                amino_super[i].append('Leu')
                            true_mass_list[i]+=113.0841
                        continue
                    elif mass == 128:
                        for i in range(len(amino_super)):
                            if i<len(amino_super)/2:
                                amino_super[i].append('Gln')
                                true_mass_list[i]+=128.0586
                            else:
                                amino_super[i].append('Lys')
                                true_mass_list[i]+=128.09496
                        continue
                for amino in roundedMassDict:
                    if roundedMassDict[amino] == mass:
                        i=0
                        for aminos_list in amino_super:
                            aminos_list.append(amino)
                            true_mass_list[i]+=massDict[amino]
                            i+=1
                            
            for aminos_list in amino_super:
                answer.append(aminos_list)
            for true_mass in true_mass_list:
                true_masses.append(true_mass)

    answer_dict = {true_masses[i] : answer[i] for i in range(len(answer))}
    pprint.pprint(answer_dict)

           
