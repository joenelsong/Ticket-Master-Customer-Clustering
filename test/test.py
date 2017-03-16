import numpy as np
import pandas
'''
pur.count() # counts for all rows

#df = df[df.line_race != 0]

'''
path = ""
purchase_data_path = path+"approved_data_purchase-v5.csv"
adwords_data_path = path+"approved_adwords_v3.csv"
ga_data_path = path+"approved_ga_data_v2.csv" 


pur = pandas.read_csv(purchase_data_path, engine='python', encoding='latin-1') 
ad = pandas.read_csv(adwords_data_path, engine='python', encoding='latin-1') 
ga = pandas.read_csv(ga_data_path, engine='python', encoding='latin-1') 





## Purchase Processing
''' Variables of Interest:


'''
#npur_header = np.array([])
#npur = pur.values



# Delete Major Category = MISC
misc_removed = len(npur)*[0]
for i in range (len(npur) ):
    if (npur[i][7] != 'MISC'):
        misc_removed[i] = 1
    

for i in range(npur):
    if (


#column_counts



new_series = len(a1)*[0]
for i in range ( len(a1) ):
    id = a1.index[i]
    for r in range( len(ga) ):
        if (ga['fullvisitorid'][r] == id):
            new_series[i] = ga['geonetwork_region'][r]



