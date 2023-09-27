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
    mass_dict = {keys[i] : values[i] for i in range(len(keys))}
    return mass_dict    

def orderDict(unsorted_dict):
    # convert elements from strings to floats
    # order the elements by value
    mass_dict = {}
    for key,value in unsorted_dict.items():
        mass_dict[key] = float(value)
        
    sorted_values = sorted(mass_dict.values())
    sorted_dict = {}

    for i in sorted_values:
        for k in mass_dict.keys():
            if mass_dict[k] == i:
                sorted_dict[k] = mass_dict[k]
    return sorted_dict

def initDynProgTable(dyn_prog_table, target_mass, amino_masses):
    for i in range(len(amino_masses)):
        dyn_prog_table[i+1][amino_masses[i]].append([amino_masses[i]])


def solution(dyn_prog_table, target_mass, amino_masses):
    for amino_index in range(1, len(amino_masses)+1):
        for dyn_prog_sum in range(1, int(round(target_mass))+1):
            if amino_masses[amino_index-1] > dyn_prog_sum:
                # Copy sequences down from previous rows
                dyn_prog_table[amino_index][dyn_prog_sum] = dyn_prog_table[amino_index-1][dyn_prog_sum]
            elif amino_masses[amino_index-1] == dyn_prog_sum:
                dyn_prog_table[amino_index][dyn_prog_sum].append([amino_masses[amino_index-1]])
            else:
                # Concatenate amino_mass to end of previous amino sequence and store
                # prev seq dyn_prog_table[amino_index][dyn_prog_sum-amino_index]
                # concat onto end of each seq
                for amino_acid in range(0,amino_index):
                    if dyn_prog_table[amino_index][dyn_prog_sum - amino_masses[amino_acid]] is not None:
                        for prev_seq in dyn_prog_table[amino_index][dyn_prog_sum - amino_masses[amino_acid]]:
                            if prev_seq is not None:
                                if sum(prev_seq) + amino_masses[amino_acid] <= target_mass:
                                    new_seq = prev_seq.copy()
                                    new_seq.append(amino_masses[amino_acid])
                                    dyn_prog_table[amino_index][dyn_prog_sum].append(new_seq)
              
if __name__ == "__main__":
    arglen = len(sys.argv)
    if arglen != 3:
        print("Usage: python sum.py <target mass sum> <amino sequence length")
        quit(0)
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    target_mass = float(sys.argv[1])
    num_aminos = int(sys.argv[2])

    mass_dict = readMasses()
    mass_dict = orderDict(mass_dict)
    print(mass_dict)
    rounded_mass_dict = {}
    mass_keys = list(mass_dict.keys())
    mass_values = list(mass_dict.values())
    rounded_mass_dict = {mass_keys[i] : int(mass_values[i]) for i in range(len(mass_keys))}
    # TODO: Round to 0.1 instead!
    rounded_mass_list = rounded_mass_dict.values()
    answer = []
    true_masses = []

    # Create table to store partial sequences
    dyn_prog_table = [[[] for j in range(int(round(target_mass))+1)] for i in range(len(rounded_mass_list)+1)] # dimensions should be num_aminos+1 x target_mass
    # and each entry should be a list of amino sequences
    initDynProgTable(dyn_prog_table, target_mass, list(rounded_mass_list))
    solution(dyn_prog_table, target_mass, list(rounded_mass_list))
    unsorted_combinations = dyn_prog_table[len(rounded_mass_list)][int(round(target_mass))]
    sorted_sequences = []
    for seq in unsorted_combinations:
        seq.sort()
        if seq not in sorted_sequences and len(seq) == num_aminos:
            sorted_sequences.append(seq)
    print("\n"+str(len(sorted_sequences))+" sequences found!\n")
    combinations = sorted_sequences
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
                for amino in rounded_mass_dict:
                    if rounded_mass_dict[amino] == mass:
                        i=0
                        for aminos_list in amino_super:
                            aminos_list.append(amino)
                            true_mass_list[i]+=mass_dict[amino]
                            i+=1
                            
            for aminos_list in amino_super:
                answer.append(aminos_list)
            for true_mass in true_mass_list:
                true_masses.append(true_mass)

    answer_dict = {true_masses[i] : answer[i] for i in range(len(answer))}
    pprint.pprint(answer_dict)

           
