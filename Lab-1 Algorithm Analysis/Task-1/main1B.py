file1=open("D:\Alg\Lab-1 Algorithm Analysis\Task-1\input1B.txt","r")
length=file1.readline()

num1lst=[]
opLst=[]
num2lst=[]
result=[]

for i in range (int(length)):
  val=file1.readline().strip("\n").split(" ")
  num1lst.append(val[1])
  opLst.append(val[2])
  num2lst.append(val[3])
  if val[2]=="+":
    result.append(int(val[1])+int(val[3]))
  elif val[2]=="-":
    result.append(int(val[1])-int(val[3]))
  elif val[2]=="*":
    result.append(int(val[1])*int(val[3]))
  else:
    result.append(int(val[1])/int(val[3]))
file1.close()

file2=open("D:\Alg\Lab-1 Algorithm Analysis\Task-1\output1B.txt","w")
for y in range (int(length)):
    final="The result of "+num1lst[y]+" "+opLst[y]+" "+num2lst[y]+" is "+str(result[y])
    if y==(int(length)-1):
      file2.writelines(final)
    else:
      file2.writelines(final+"\n")
      final=""
file2.close()