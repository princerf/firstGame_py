import pickle

points = []

def print_table():
    global points
    points.sort()
    if len(points) == 0:
        print '\nThe table of points is empty\n'
    else:
        print '\n'+'-'*5 + '   Table of points   ' + '-'*5
        for i in points:
            print i
        print '\n'

def savePoint(myList):
    with open('file' , 'w+') as data_w:
        pickle.dump(myList , data_w)

def loadPoint():
    with open('file' , 'r+') as data_r:
        load_point = pickle.load(data_r)
        return load_point

def clear_list():
    global points
    points = []
    with open('file' , 'w') as clHist:
        pickle.dump(points , clHist)

points = loadPoint()
