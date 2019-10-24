import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

'''
def writeto():

    headings = ['bitter', 'sour', 'salty', 'sweet', 'umami', 'happiness', 'sadness', 'surprise', 'fear', 'anger',
                'disgust', 'content']

    with open('graph.csv', 'w') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(headings)
'''

def writeto():
    with open('graph.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([])


def appendto(values):
    with open('graph.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(values)


def showgraph():
    cols = ['bitter', 'sour', 'salty', 'sweet', 'umami', 'happiness', 'sadness', 'surprise', 'fear', 'anger',
            'disgust']

    df = pd.read_csv('graph.csv', names=cols, header=None)
    df['frame'] = np.arange(len(df))

    df.plot(x='frame',
            y=['happiness', 'sadness', 'surprise', 'fear', 'anger', 'disgust'])
    plt.ylabel("percentage")
    plt.title("Emotion")
    plt.axhline(y=60, linestyle='dashed', color='k', linewidth=0.7)
    plt.ylim(0, 100)

    df.plot(x='frame',
            y=['bitter', 'sour', 'salty', 'sweet', 'umami'])
    plt.axhline(y=55, linestyle='dashed', color='k', linewidth=0.7)
    plt.ylabel("percentage")
    plt.title("Taste")
    plt.ylim(0, 100)

    plt.show()

