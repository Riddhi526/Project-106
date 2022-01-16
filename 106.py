import csv
import numpy as np
import plotly.express as px

def plotFigure(data_source):
    with open(data_source) as file_name:
        data = csv.DictReader(file_name)
        fig = px.scatter(data, x = "Days Present", y = "Marks In Percentage")
        fig.show()

def getDataSource(data_path):
    Days_present = []
    Marks_In_Percentage = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Days_present.append(float(row["Days Present"]))
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))

    return {"x" : Days_present, "y": Marks_In_Percentage}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Days present and marks in percentage is :-  \n--->",correlation[0,1])

def setup():
    data_source = "student.csv"


    datasource = getDataSource(data_source)
    findCorrelation(datasource)
    plotFigure(data_source)
    
setup()



