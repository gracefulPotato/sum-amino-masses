1. open terminal
2. run git clone sum-amino-masses
3. run cd sum-amino-masses
4. run script with: python sum.py <desired mass total>


Part 2 setup:
Open spectra in FlexAnalysis
Make sure mass list is set up with a low threshold
Select File > Export > Mass list to Excel
Open downloaded file in Excel and Save As a csv file
Run the script specifying that filename and the target peak as follows:
    python peak_processing.py <name of csv input file> <target peak>