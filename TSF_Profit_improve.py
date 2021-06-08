import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("E:\MUSAB II\Internships\SPARKS Foundation\SampleSuperstore.csv")
Superstore = data.drop(['Country'],axis=1)

#CREATING THE CENTRAL DATAFRAME
cent1 = Superstore.loc[(Superstore['Category']=='Furniture') & (Superstore['Region']=='Central')]
central1 = cent1.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
cent2 = Superstore.loc[(Superstore['Category']=='Office Supplies') & (Superstore['Region']=='Central')]
central2 = cent2.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
dato = [central1['Profit'],central2['Profit']]
headers = ['Furniture','Office Supplies']
Central = pd.concat(dato,axis=1,keys=headers)
central_furn_mean=Central['Furniture'].mean()
#print("The mean of Furniture Profit in the Central region is {}".format(central_furn_mean))
central_OS_mean=Central['Office Supplies'].mean()
#print("The mean of Office Supplies Profit in the Central region is {}".format(central_OS_mean))

#CREATING THE SOUTH DATAFRAME
sou1 = Superstore.loc[(Superstore['Category']=='Furniture') & (Superstore['Region']=='South')]
south1 = sou1.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
sou2 = Superstore.loc[(Superstore['Category']=='Office Supplies') & (Superstore['Region']=='South')]
south2 = sou2.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
datr = [south1['Profit'],south2['Profit']]
headers = ['Furniture','Office Supplies']
South = pd.concat(datr,axis=1,keys=headers)
south_furn_mean=South['Furniture'].mean()
#print("The mean of Furniture Profit in the Southern region is {}".format(south_furn_mean))
south_OS_mean=South['Office Supplies'].mean()
#print("The mean of Office Supplies Profit in the Southern region is {}".format(south_OS_mean))

#CREATING THE EAST DATAFRAME
eas1 = Superstore.loc[(Superstore['Category']=='Furniture') & (Superstore['Region']=='East')]
east1 = eas1.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
eas2 = Superstore.loc[(Superstore['Category']=='Office Supplies') & (Superstore['Region']=='East')]
east2 = eas2.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
datw = [east1['Profit'],east2['Profit']]
headers = ['Furniture','Office Supplies']
East = pd.concat(datw,axis=1,keys=headers)
east_furn_mean=East['Furniture'].mean()
#print("The mean of Furniture Profit in the Eastern region is {}".format(east_furn_mean))
east_OS_mean=East['Office Supplies'].mean()
#print("The mean of Office Supplies Profit in the Eastern region is {}".format(east_OS_mean))

#CREATING THE WEST DATASET
wes1 = Superstore.loc[(Superstore['Category']=='Furniture') & (Superstore['Region']=='West')]
west1 = wes1.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
wes2 = Superstore.loc[(Superstore['Category']=='Office Supplies') & (Superstore['Region']=='West')]
west2 = wes2.drop(['Ship Mode','Segment','City','State','Postal Code','Sub-Category','Sales','Quantity','Discount'],axis=1)
datx = [west1['Profit'],west2['Profit']]
headers = ['Furniture','Office Supplies']
West = pd.concat(datx,axis=1,keys=headers)
west_furn_mean=West['Furniture'].mean()
#print("The mean of Furniture Profit in the Eastern region is {}".format(west_furn_mean))
west_OS_mean=West['Office Supplies'].mean()
#print("The mean of Office Supplies Profit in the Eastern region is {}".format(west_OS_mean))

#The Final Statements
if central_furn_mean > central_OS_mean:
    print('Increase the Purchases of Furniture and decrease the Purchasing of Office Supplies in The Central')
else:
    print('Increase the Purchases of Office Supplies and decrease the Purchasing of Furniture in The Central')

if south_furn_mean > south_OS_mean:
    print('Increase the Purchases of Furniture and decrease the Purchasing of Office Supplies in The South')
else:
    print('Increase the Purchases of Office Supplies and decrease the Purchasing of Furniture in the South')

if east_furn_mean > east_OS_mean:
    print('Increase the Purchases of Furniture and decrease the Purchasing of Office Supplies in the East')
else:
    print('Increase the Purchases of Office Supplies and decrease the Purchasing of Furniture in the East')

if west_furn_mean > west_OS_mean:
    print('Increase the Purchases of Furniture and decrease the Purchasing of Office Supplies in The West')
else:
    print('Increase the Purchases of Office Supplies and decrease the Purchasing of Furniture in The West')
