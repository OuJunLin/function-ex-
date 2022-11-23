year, month = map(int, input().split())

def checkYear(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False



def yearToDates(year):
    sum1 = 0
    for i in range(1, year):
        if checkYear(i):
            sum1 += 366
        else:
            sum1 += 365
    
    return sum1



def monthToDates(year, month):
    sum2 = 0
    month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,\
        9:30, 10:31, 11:30, 12:31}
    for i in range(1, month):
        if checkYear(year) and i==2:
            sum2 += month_dict[i]+1
        else:
            sum2 += month_dict[i]
    
    return sum2+1



def dateToWeek(year, month):
    dates = yearToDates(year)+monthToDates(year, month)
    return dates%7



print("SU", "MO", "TU", "WE", "TH", "FR", "SA", sep="\t")
weekspace = dateToWeek(year, month)
week = 0
for i in range(weekspace):
    print(" ", end="\t")
    week += 1

month_dict = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31,\
    9:30, 10:31, 11:30, 12:31}
for i in range(1, month_dict[month]+1):
    if week+1 == 7:
        print(i)
        week = 0
    else:
        print(i, end="\t")
        week += 1