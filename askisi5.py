t = [0,3,2,5,0,3,5,1,4,6,2,4];

def dayofweek(d,m,y):
    if(m < 3):
        y = y - 1;
    return ( y + y/4 - y/100 + y/400 + t[m-1] + d) % 7;

d=int(input("Please enter the day"));
m=int(input("Please enter the month"));
y=int(input("Please enter the year"));
day = dayofweek(d , m, y);
if(day == 1):
    print("Monday");
if(day == 2):
    print("Tuesday");
if(day == 3):
    print("Wednesday");
if(day == 4):
    print("Thursday");
if(day == 5):
    print("Friday");
if(day == 6):
    print("Saturday");
if(day == 7):
    print("Sunday");
