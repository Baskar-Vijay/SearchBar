import subprocess

urlbasic="https://www.google.com/search?q="
input1 = str(input("Enter Your Input:")).split()
urlbasic="https://www.google.com/search?q="+"+".join(input1)
try:
  subprocess.Popen(["cmd.exe","/c", "start", "", "chrome", urlbasic])
except Exception as e:
   print(e)
else:
    print("done")