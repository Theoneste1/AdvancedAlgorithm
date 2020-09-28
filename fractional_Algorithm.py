import operator
#Receiving input from the user
n= int(input("Enter the number of objects:"))
profit = list(map(int,input("Enter your profit values:").split()))
weight = list(map(int,input("Enter your weight values:").split()))
m= int(input("Enter the maximum capacity bag:"))
print('Calculate the ratio(profit/weight) for each item')
#create list and append those value and add ratio of profit and weight

l=[]
for i in range(n):
    l.append([profit[i],weight[i],profit[i]*1.0/weight[i]])
    
    print(profit[i]*1.0/weight[i])
#sort the items based on this ratio
l=sorted(l,reverse=True,key= operator.itemgetter(2))
print('Sort the item based on ratio of (profit/weight)')
print(l)
#take item with highest ratio and add them until we can't add the next item as whole
max_profit=0
fractional_object=0
for i in range(n):
    if m>0 and l[i][1]<m:
        m-=l[i][1]
        max_profit+=l[i][0]
    else:
        fractional_object=i
#at the end add the next item as much (fraction) as we can
if m>0:
    max_profit+=m*(l[fractional_object][0]/(l[fractional_object][1]))
print("Maximum profit:")
print(max_profit)
