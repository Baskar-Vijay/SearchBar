import subprocess

urlbasic="https://www.google.com/search?q="
input1 = str(input("Enter Your Input:")).split(" ")
count=0
for i in input1:
 if count != 0:
  urlbasic+="+"+i
 elif count == 0:
   urlbasic+=i
   count += 1
 else:
    print("unexpected behaviour")
# input[0]== i: then u can exclude the inclusion of count 
print(urlbasic)
try:
  subprocess.Popen(["firefox",urlbasic])
except Exception as e:
   print(e)
else:
    print("done")