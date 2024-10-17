file1=open("D:\Alg\Lab-2 Two pointer\Task-1\input1.txt","r")
file2=open("D:\Alg\Lab-2 Two pointer\Task-1\output1.txt","w")
length=file1.readline().strip("\n").split(" ")
arr=file1.readline().strip("\n").split(" ")

index2,index1=(int(length[0])-1),0
bul=False
for i in range (int(length[0])):
    if (int(arr[index1]))+int(arr[index2])==int(length[1]):
        bul=True
        break
    elif str(int(length[1])-(int(arr[index2]))) in arr:
        index1+=1
    else:
        index2-=1
index1+=1
index2+=1

if bul:
    file2.writelines(str(index1))
    file2.writelines(" ")
    file2.writelines(str(index2))
else:
    file2.writelines("IMPOSSIBLE")

file1.close()
file2.close()