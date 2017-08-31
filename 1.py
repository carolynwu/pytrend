# use Google Trend API to find the historical search frequency 
# Use python to process the return data from Google Trend API. 
# Use CSV lib to output the result and show in MS EXCEL
# by xujia wu
# 8/31/2017


from pytrends import request
import csv

# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = request.TrendReq()

# Create payload and capture API tokens.
pytrend.build_payload(kw_list=['Houston', 'Dallas'],timeframe='2017-07-30 2017-08-30')

interest_over_time_df = pytrend.interest_over_time()
interest_over_time_e=interest_over_time_df['Houston']
interest_over_time_f=interest_over_time_df['Dallas']

interest_over_time_c=interest_over_time_df['Houston'].keys()
interest_over_time_g=interest_over_time_df['Dallas'].keys()

# new_list to store the time and searching frequency and ',' used to separated the statistics in cvs file
new_list=[]
for index in range (len(interest_over_time_c)):
	new_list.append(str(interest_over_time_c[index])+','+str(interest_over_time_e[interest_over_time_c[index]])+','+str(interest_over_time_f[interest_over_time_g[index]]))

new_list.insert(0,',Houston,Dallas')

for i in range(len(new_list)):
	new_list[i]=str(new_list[i])+str("\n")	
new_list1=[]
new_list2=[]
for index in range (len(interest_over_time_c)):
	new_list1.append(interest_over_time_e[interest_over_time_c[index]])
for index in range (len(interest_over_time_c)):
	new_list2.append(interest_over_time_f[interest_over_time_g[index]])
r=0
for i in new_list1:
	r+=i
result1 =r/len(new_list1)
result1=round(result1,2)
#print(result1)

r=0
for i in new_list2:
	r+=i
result2=r/len(new_list2)
result2=round(result2,2)
new_list.insert(32,','+str(result1)+','+str(result2))


f=open('persons.csv','w')
data=new_list
f.writelines(data)