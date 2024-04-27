#The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
if __name__ == '__main__':
    n = int(input())
for i in range(n):
    print(i**2)

#Code includes printing 123....n
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end='')

#Leap year
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))