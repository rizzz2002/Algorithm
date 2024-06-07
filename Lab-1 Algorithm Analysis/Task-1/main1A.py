file1=open("D:\Alg\Lab-1 Algorithm Analysis\Task-1\input1A.txt","r")
length=file1.readline()
numlst=[]
resultLst=[]
for i in range (int(length)):
    num=file1.readline().strip("\n")
    if int(num)%2==0:
        numlst.append(num)
        resultLst.append("Even")
    else:
        numlst.append(num)
        resultLst.append("Odd")
file1.close()

file2=open("D:\Alg\Lab-1 Algorithm Analysis\Task-1\output1A.txt","w")
for y in range (int(length)):
    final=numlst[y]+" is an "+resultLst[y]+" number"
    if y==(int(length)-1):
      file2.writelines(final)
    else:
      file2.writelines(final+"\n")
      final=""
file2.close()