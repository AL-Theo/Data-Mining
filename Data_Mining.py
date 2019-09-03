mainFile = open('project25_data.csv')
#Functions
def getData(fileObject, columnNumber):
    lists = []
    for line in fileObject:
        line = line.replace('\n', '')
        row = line.split(',')
        data = (row[columnNumber],row[0])
        lists.append(data)
    return lists[1:]
 
def monthlyAverage(data):
    currMonth= ""
    months = 0
    avg = 0
    total = 0
    result = []
    for line in data[::-1]:
        if currMonth == "":
            currMonth= line[1][0:7]
        #print(currMonth, total, avg)
        if(months < 8):
            if currMonth == line[1][0:7]:
                avg += float(line[0])
                total+= 1
            else:
                #new month
                result.append((avg/total, currMonth))
                total=0
                months +=1
                currMonth= line[1][0:7]
                avg= float(line[0])
        else:
            break
    result = result[::-1]
    print("Last 8 monthly averages")
    for monthlyData in result :
        print("month = "+ monthlyData[1] + " data= "+ str(monthlyData[0]))
    return result
    
#Main Code
column = int(input('Enter column number: '))
data = getData(mainFile, column)
data = monthlyAverage(data)

print("\n\nLowest 6 values:")
#get lowest
low= sorted(data)[0:6]
for l in low:
    print("date = "+ l[1] + " data= "+ str(l[0]))

print("\n\nHighest 6 values:")
#get highest
high= sorted(data)[::-1][0:6]
for h in high:
    print("date = "+ h[1] + " data= "+ str(h[0]))





            

    
          






