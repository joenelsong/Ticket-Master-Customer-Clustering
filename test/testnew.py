import numpy as np
import pandas
import csv

'''
path = ""
adwords_data_path = path+"approved_adwords_v3.csv"
ga_data_path = path+"approved_ga_data_v2.csv" 

ad = pandas.read_csv(adwords_data_path, engine='python', encoding='latin-1') 
ga = pandas.read_csv(ga_data_path, engine='python', encoding='latin-1') 
'''
##
path = ""
ga_data_path = path+"approved_ga_data_v2.csv" 
ga = pandas.read_csv(ga_data_path, engine='python', encoding='latin-1') 
# deleted rows from ga


ga.drop(['attraction_id','visitstarttime','date','customer_id','clickinfo_slot','adnetworktype','referralpath','campaign_name','source','medium','device_browser','device_browserversion','device_devicecategory','device_operatingsystem','device_operatingsystemversion','device_mobiledevicebranding','device_flashversion','device_javaenabled','device_language','device_screencolors','device_screenresolution','hits_minute','hits_time','hits_type','hits_page_hostname'], axis=1, inplace=True)


#more deleting from ga
ga.drop(['event_id','visitnumber','visitid', 'campaign_id', 'adgroup_id', 'keyword', 'geonetwork_continent', 'geonetwork_subcontinent', 'geonetwork_metro', 'hits_hitnumber', 'hits_hour', 'hits_isentrance', 'hits_isexit', 'hits_isinteraction'], axis=1, inplace=True)

ga = ga[ ~(ga.totals_timeonsite == 0) | ~(ga.totals_pageviews == 0)] # Remove some bad rows
ga.fillna(value=0, inplace=True)
ga.drop('totals_bounces', axis=1, inplace=True) # Drop bounces

data1 = ga.drop(['totals_visits'], axis=1)
data1 = ga.groupby(ga['fullvisitorid']).sum().reset_index()

data2 = data1.drop(['totals_hits','totals_pageviews','totals_timeonsite', axis=1)
data2 = data2.drop('geonetwork_region', axis=1)
data1 = ga.groupby(ga['fullvisitorid']).first().reset_index()

ga2 = ga.drop(['totals_bounces','totals_visits','totals_hits','totals_pageviews','totals_timeonsite'], axis=1)
geo1 = ga2.groupby(ga2['fullvisitorid']).first().reset_index()

#pd.merge(df_a, df_b, on='subject_id', how='inner')
newd = pandas.merge(data1, geo1, how='inner', on='fullvisitorid')
newd2 = newd[ (newd['totals_timeonsite']!=0) ]
newd3 = newd2[ (newd['totals_pageviews']!=0) ]


# Remove Outliers

#newd3.to_csv('preprocessed_cluster_data.csv')



