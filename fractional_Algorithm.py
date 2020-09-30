import operator
#Receiving input from the user
numberOfObjects= int(input("Enter the number of objects:"))
profitList = list(map(int,input("Enter your profit values:").split()))
weightList = list(map(int,input("Enter your weight values:").split()))
maximumNumberOfObjectsInBag= int(input("Enter the maximum capacity bag:"))
print('Calculate the ratio(profit/weight) for each item')
#create list and append those value and add ratio of profit and weight

generalList=[]
for i in range(numberOfObjects):
    generalList.append([profitList[i]
    ,weightList[i],profitList[i]*1.0/weightList[i]])

    print("If", weightList[i],"=>",profitList[i],"Then",profitList[i]*1.0/weightList[i])
#sort the items based on this ratio
generalList=sorted(generalList,reverse=True,key= operator.itemgetter(2))
print('Sort the item based on ratio of (profit/weight)')
print(generalList)
#take item with highest ratio and add them until we can't add the next item as whole
max_profit=0
fractional_object=0
for i in range(numberOfObjects):
    if maximumNumberOfObjectsInBag>0 and generalList[i][1]<maximumNumberOfObjectsInBag:
        maximumNumberOfObjectsInBag-=generalList[i][1]
        max_profit+=generalList[i][0]
    else:
        fractional_object=i
#at the end add the next item as much (fraction) as we can
if maximumNumberOfObjectsInBag>0:
    max_profit+=maximumNumberOfObjectsInBag*(generalList[fractional_object][0]/
    (generalList[fractional_object][1]))
print("Maximum profit:")
print(max_profit)
