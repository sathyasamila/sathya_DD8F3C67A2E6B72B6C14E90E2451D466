# leap year

"""
year % 4==0 &
year % 100!==0
year % 100==0

"""
def isleapyear(year):
  if (year % 4==0 and year % 100!=10) or year % 400==0:
      return True 
  else:
      return False

year = int(input("Enter a year :"))

if isleapyear(year):
 print('{} is a leap yaer.'.format(year))
else:
    print('{} is not a leap yaer.'. format (year))
     
     
                 
