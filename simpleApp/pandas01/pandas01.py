#-* coding:utf8 -*-
import pandas as pd


data = pd.read_csv('Accidents0514.csv',error_bad_lines=False)

# print 'Total rows:{0}'.format(len(data))
#
# print list(data)

#发生在周一的车祸
accidents_sunday=data[data.Day_of_Week==1]
print ('Accidents which happened on a Sunday:{0}'.format(len(accidents_sunday)))

#发生在周一的车祸，10辆以上的

accidents_sunday_twenty_cars=data[(data.Day_of_Week==1)&(data.Number_of_Vehicles>10)]
print ('Accidents which happened on a Sunday involving > 20 cars:{0}'.format(len(accidents_sunday_twenty_cars)))

#发生在周一的车祸，10辆以上的,并且是雨天

accidents_sunday_twenty_cars_rain = data[(data.Day_of_Week==1)&(data.Number_of_Vehicles>10)&(data.Weather_Conditions==2)]
print ('Accidents which happened on a Sunday involving > 20 cars in the rain:{0}'.format(len(accidents_sunday_twenty_cars_rain)))

# Accidents in London on a Sunday
london_data = data[data['Police_Force'] == 1 & (data.Day_of_Week == 1)]
print("Accidents in London from 1979-2004 on a Sunday: {0}".format(
    len(london_data)))

#2005年发生的事故在london
london_data_2005 = london_data[(pd.to_datetime(london_data['Date'],coerce=True)>pd.to_datetime(
    '2005-01-01',coerce=True))&(pd.to_datetime(london_data['Date'],coerce=True)<pd.to_datetime(
    '2005-12-31',coerce=True))]
print ('Accidents in London in the year 2005 on sunday:{0}'.format(len(london_data_2005)))

london_data_2005.rename(
    columns={'\xef\xbb\xbfAccident_Index': 'Accident_Index'}, inplace=True)


# Save to Excel
writer = pd.ExcelWriter(
    'london_data_2005.xlsx', engine='xlsxwriter')
london_data_2005.to_excel(writer, 'Sheet1')
writer.save()