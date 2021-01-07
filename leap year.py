
#leapyear uning nestedif
while True:
    year = int(input("Enter a year: "))
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
                break
            else:
                print("{0} is not a leap year".format(year))
                continue
        else:
            print("{0} is a leap year".format(year))
            break
    else:
        print("{0} is not a leap year".format(year))
        continue
    
### simplified leapyear

year=int(input("enter a year"))
if year%4==0 and year%100!=0 or year%400==0:   ##or 
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))                



