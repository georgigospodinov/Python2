import csv

input_file = "Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv"
inf = csv.reader(open(input_file, 'r'))
outf = open("reformatted.csv", 'w')
precision = 1000

def wr(row):
    """
        Takes a list of strings and writes them to a file in csv format.
        The strings are separated by commas and a new line is put at the end.

        :param row: The row to write to file as a list of strings
    """
    length = len(row)
    for i in range(length-1):
        outf.write(row[i])
        outf.write(',')
    outf.write(row[length-1])
    outf.write('\n')

def get_range(string):  # Expected format '$_._'
    """
        Takes a string of expected format '$<float>'
        and converts into a range of format '$_000-_000'.
        So, $1234.56 becomes $1000-2000.

        :param string: The string to parse and convert
        :return: The range the number belongs to ('$<start>-<end>')
        :rtype: string
    """
    value = int(float(string[1:]))  # Drop dollar sign, parse float, then int
    start = round(value/precision)*precision  # Replace the last two digits with 0s
    end = start + precision
    return '$'+str(start)+'-'+str(end)

def reformat_row(row):
    """
        Takes a list of strings,
        formats the money amounts from the last three variables into ranges,
        and returns a new list with these values.

        :param row: The row to reformat as a list of strings
        :return: A list of reformatted strings
        :rtype: List of strings.
    """
    length = len(row)
    formatted = []
    for i in range(length):
        v = row[i]
        if i == 9 or i == 10 or i == 11:
            v = get_range(v)
        # Put quotes to avoid splitting a string because of commas in it.
        formatted.append("\""+v+"\"")
    return formatted

def format_file():
    """
        Reformats the input file,
        saving to the output file.
    """
    wr(inf.__next__())  # Copy the header
    for r in inf:  # Reformat the contents.
        wr(reformat_row(r))

    outf.close()
