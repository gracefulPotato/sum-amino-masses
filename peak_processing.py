import sys
import csv
import sum

if __name__ == "__main__":
    # Check args
    arglen = len(sys.argv)
    if arglen != 3:
        print("Usage: python sum.py <name of csv input file> <target peak>")
        quit(0)
    input_filename = sys.argv[1]
    target_peak = sys.argv[2]
    print(f"Input filename: {input_filename}")
    print(f"Target peak: {target_peak}")

    with open(input_filename, newline='') as csvfile:
       spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
       peak_masses = []
       i=0
       for row in spamreader:
           if i>2:
               peak_masses.append(float(row[0]))
           i+=1
    peak_masses = peak_masses
    print(peak_masses)

    massDict = sum.readMasses()
    massDict = sum.orderDict(massDict)
    print(massDict)

    sequences = {}

    # first effort
    for i in range(len(peak_masses)):
        bigger_mass = peak_masses[len(peak_masses)-i-1]
        for key in massDict.keys():
            amino_mass = massDict[key]
            difference = round(bigger_mass - amino_mass, 3)
            #print(difference)
            if difference in peak_masses:
                #print("HIT!")
                #print(difference)
                sequences[(bigger_mass,difference)] = [key]
    print("\n------------------------------------------")
    print("Amino acid fragment sequences identified:")
    print(sequences)
    

    # identify which peaks are important
       # first, because you can subtract the masses off from the total of the sequence
       # to find the order
          # the highest mass fragment should be on the end of the amino acid (all aminos together)
          # the order they come off is the sequence

       # the third option: look for other key facts

       # option: use part 1 (sum.py) to find possible subsequences for each of the peaks

       # option 3: the fragmentation rules (page 12 of latest de novo pdf)

       # -17 rule

       # filter out low abundances

       # y = abundance = peak height = intensity




       # strategy 1: start with the sequence given by sum.py, then look for permutations and
       # subsequences in the CSV
            # one easy thing is to look for two peaks whose difference between their masses equals
            # an individual amino acid mass.

