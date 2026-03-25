#COUNT DOWN TIMER  *with 1-second gap)
import time
count=int(input("enter the counter num:"))
print("\n countdown start now:")
for i in range(count,0,-1):
    print(i)
    time.sleep(1)
print("\n  WOHOOO! Happy New Year")   
