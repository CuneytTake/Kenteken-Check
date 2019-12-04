import urllib.request
import json
import tkinter as tk
from tkinter import ttk, filedialog
import tempfile
from PIL import ImageGrab
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


df1 = pd.read_csv("gebreken.csv",usecols=['Kenteken','Gebrek identificatie'],nrows=10000)
print (df1)
# Counts number of unique values in column 'Gebrek identificatie' and prints the 5 with the most results as data frame
top5 = df1['Gebrek identificatie'].value_counts().nlargest(5)

# Assigns top 5 to a variable and casts them to StringVar
topresult1= top5.index[0]
topresult2= top5.index[1]
topresult3= top5.index[2]
topresult4= top5.index[3]
topresult5= top5.index[4]

# Listing top 5 results and their counts
topresults = [topresult1, topresult2, topresult3, topresult4, topresult5]
topresultcount = [top5[0], top5[1], top5[2], top5[3], top5[4]]
print ('topresults =',topresults)
print ('topresultcount =',topresultcount)
# Arranging top results in numpy grid
xpos = np.arange(len(topresults))
print ('topresults xpos =',xpos)

def beschrijfgebrek():
    global topresultoutput
    topresultoutput = ""
    for x in topresults:
        gebrekenlegenda = 'https://opendata.rdw.nl/resource/hx2c-gt7k.json?gebrek_identificatie=' + x
        response = urllib.request.urlopen(gebrekenlegenda)
        gebrekenlegendaResult = json.loads(response.read())
        for v in gebrekenlegendaResult:
            for key, value in v.items():
                if key == 'gebrek_omschrijving':
                    topresultoutput += x + ' - ' + value + "\n"

beschrijfgebrek()


# 2D Bar Chart declarations
plt.bar(xpos,topresultcount, label="Gebreken")
plt.xticks(xpos, topresults)
plt.ylabel("Aantal gebreken in 10000 keuringen")
plt.xlabel("Gebrek identificaties" + '\n\n' + topresultoutput)
plt.title('Top 5 Gebreken APK')
plt.subplots_adjust(bottom=0.33)
plt.legend()
plt.show()

print (xpos)
print (topresultoutput)

