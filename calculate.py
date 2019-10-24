import csv
from statistics import mean
# AU01 is data [1][5]
import graph


def calculate(row, name):
    """
    Calculates a normalised value for each taste/emotion using a combination of Action Units.

    :type row: int
    :param row: row number passed in from the vis.py file so only the row needed at the time is processed

    :type name: String
    :param name: filename given by the user from the start screen, used to open the correct csv file

    :return: values in an array which are then displayed in the GUI using progress bars
    """
    values = []

    with open('../GUI/files/'+str(name)+'.csv', 'r') as f:
        data = [row for row in csv.reader(f)]

    # calculate bitter float
    bitter = mean([float(data[row][7]), float(data[row][8]),  float(data[row][11]),
           float(data[row][12])])
    bitter = round((bitter / 5) * 250)

    values.append(bitter)

    # calculate sour float
    sour = mean([float(data[row][7]), float(data[row][8]), float(data[row][11]),
         float(data[row][12]), float(data[row][13]),  float(data[row][18]),
         float(data[row][19]), float(data[row][20])])
    sour = round((sour / 5) * 250)

    values.append(sour)

    # calculate salty
    salty = mean([float(data[row][7]), float(data[row][11]), float(data[row][12]), float(data[row][15]),
          float(data[row][19])])
    salty = round((salty / 5) * 250)

    values.append(salty)

    # calculate sweet
    sweet = mean([float(data[row][13]), float(data[row][14]), float(data[row][20])])
    sweet = round((sweet / 5) * 200)

    values.append(sweet)

    # calculate umami
    umami = mean([float(data[row][7]), float(data[row][13]), float(data[row][12])])
    umami = round((umami / 5) * 200)

    values.append(umami)

    # ------------------------------------------------------------------------------------------------------------- #

    # calculate happy
    happy = mean([float(data[row][9]), float(data[row][13])])
    happy = round((happy / 5) * 150)

    values.append(happy)

    # calculate sad
    sad = mean([float(data[row][5]), float(data[row][7]), float(data[row][15])])
    sad = round((sad / 5) * 200)

    values.append(sad)

    # calculate surprise
    surprise = mean([float(data[row][5]), float(data[row][6]), float(data[row][8]), float(data[row][20])])
    surprise = round((surprise / 5) * 200)

    values.append(surprise)

    # calculate fear
    fear = mean([float(data[row][5]), float(data[row][6]), float(data[row][7]), float(data[row][8]),
         float(data[row][20])])
    fear = round((fear / 5) * 200)

    values.append(fear)

    # calculate anger
    anger = mean([float(data[row][7]), float(data[row][8]), float(data[row][10]), float(data[row][18])])
    anger = round((anger / 5) * 200)

    values.append(anger)

    # calculate disgust
    disgust = mean([float(data[row][11]), float(data[row][16]), float(data[row][19])])
    disgust = round((disgust / 5) * 200)

    values.append(disgust)

    graph.appendto(values)

    row += 1

    return values


