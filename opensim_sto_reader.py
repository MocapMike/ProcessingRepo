import os
import csv

def readMotionFile(filename):
    """ Reads OpenSim .sto files.

    Parameters
    ----------

    filename: absolute path to the .sto file

    Returns
    -------

    header: the header of the .sto
    labels: the labels of the columns
    data: an array of the data

    """

    if not os.path.exists(filename):
        print('File does not exist')
        return

    file_id = open(filename, 'r')

    # read header
    next_line = file_id.readline()
    header = [next_line]
    nc = 0
    nr = 0
    while not 'endheader' in next_line:
        if 'datacolumns' in next_line:
            nc = int(next_line[next_line.index(' ') + 1:len(next_line)])
        elif 'datarows' in next_line:
            nr = int(next_line[next_line.index(' ') + 1:len(next_line)])
        elif 'nColumns' in next_line:
            nc = int(next_line[next_line.index('=') + 1:len(next_line)])
        elif 'nRows' in next_line:
            nr = int(next_line[next_line.index('=') + 1:len(next_line)])

        next_line = file_id.readline()
        header.append(next_line)

    # process column labels
    next_line = file_id.readline()
    if next_line.isspace() == True:
        next_line = file_id.readline()

    labels = next_line.split()

    # get data
    data = []
    for i in range(1, nr + 1):
        d = [float(x) for x in file_id.readline().split()]
        data.append(d)

    file_id.close()

    return header, labels, data


def writeToCSV(filename, labels, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(labels)
        writer.writerows(data)



# Test the function
header, labels, data = readMotionFile(r'/Users/mdn/Documents/DATA/V3D_Opensim_Comparison/TAG_800_A1/AddbiomechanicOutput/SO/RealFinalTestSO_L1_StaticOptimization_force.sto')
print(header)
print(labels)
print(data)

csv_filename = "/Users/mdn/Documents/DATA/V3D_Opensim_Comparison/TAG_800_A1/AddbiomechanicOutput/SO/RealFinalTestSO_L1_StaticOptimization_force.csv"  # replace with your desired CSV filename
writeToCSV(csv_filename, labels, data)