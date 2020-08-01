import plotly
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.subplots import make_subplots
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="airportservices-hyd"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM parkingstands")
records = mycursor.fetchall()
len1 = len(records)

mycursor.execute("SELECT * FROM trolley")
records1 = mycursor.fetchall()
len2 = len(records1)

mycursor.execute("SELECT * FROM informationdesk")
records2 = mycursor.fetchall()
len3 = len(records2)

mycursor.execute("SELECT * FROM currencyexchange")
records3 = mycursor.fetchall()
len4 = len(records3)

mycursor.execute("SELECT * FROM boardinggates")
records4 = mycursor.fetchall()
len5 =  len(records4)

mycursor.execute("SELECT * FROM arrivalbaggagebelt")
records5 = mycursor.fetchall()
len6 =  len(records5)

fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]], subplot_titles=['Pie Chart', 'Bar Chart'])
trace1=go.Bar(
    x=[' Parking Stands','Trolley','InformationDesk','Currency Exchange','BoardingGates','ArrivalBaggageBelt'],
    y=[len1,len2,len3,len4,len5,len6],
    name="",
    marker = {'color' : ['cyan','darkviolet','red','green','blue','orange'] }
    )

trace2=go.Pie(values=[len1,len2,len3,len4,len5,len6],
labels=[' Parking Stands','Trolley','InformationDesk','Currency Exchange','BoardingGates','ArrivalBaggageBelt'],
name="")
fig.add_trace(trace1,row=1, col=1)
fig.add_trace(trace2,row=1, col=2)

fig.update_layout(title='Service Consumption', xaxis={'title':'Service name'},
    yaxis={'title':'Units of Comsumption'})
plotly.offline.plot(fig, filename='C:/Users/Lekhasree Uddanti/Desktop/project/figure1.html',validate=False)
