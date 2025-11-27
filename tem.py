import sys
if len(sys.argv)==1:
  temp=sys.argv[0]
else:
  temp=33
if(temp<=15):
  temp1="Cold"
elif(15<=temp>=30):
  temp1="Normal"
else:
  temp1="Hot"
print("Temperature:",temp)
print("Status:",temp1)
