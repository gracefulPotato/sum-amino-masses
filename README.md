1. open terminal
2. run git clone sum-amino-masses
3. run cd sum-amino-masses
4. run script with: python sum.py <desired mass total>


Part 2 setup:
1. Open spectra in FlexAnalysis
2. Make sure mass list is set up with a low threshold
3. Select File > Export > Mass list to Excel
4. Open downloaded file in Excel and Save As a csv file
5. Run the script specifying that filename and the target peak as follows:
    python peak_processing.py <name of csv input file> <target peak>
