def is_leap(year):
    leap = False
    
    if (not (year % 4)):
        leap = True

        if (not (year % 100)):
            leap = False

            if(not (year % 400)):
                leap = True
    
    return leap

year = int(input())
print(is_leap(year))