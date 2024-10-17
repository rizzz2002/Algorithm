file1=open("D:\Alg\Lab-2 Two pointer\Task-2\input2.txt","r")
file2=open("D:\Alg\Lab-2 Two pointer\Task-2\output2.txt","w")
length=file1.readline().strip("\n")
arr=file1.readline().strip("\n").split(" ")
length2=file1.readline().strip("\n")
arr2=file1.readline().strip("\n").split(" ")

finalLength=int(length)+int(length2)
finalLst=[]

index1,index2=0,0

for i in range (finalLength-2):
    if index1+1==len(arr):
        
        finalLst.append(arr2[index2])
        index2+=1
    elif index2+1==len(arr2):
        finalLst.append(arr[index1])
        index1+=1
    elif int(arr[index1])>int(arr2[index2]):
        finalLst.append(arr2[index2])
        index2+=1
    elif int(arr[index1])<int(arr2[index2]):
        finalLst.append(arr[index1])
        index1+=1
    else:
        i+=1
        finalLst.append(arr[index1])
        finalLst.append(arr2[index2])
        index1+=1
        index2+=1

for y in range (finalLength-2):
    file2.writelines(finalLst[y])
    file2.writelines(" ")

file1.close()
file2.close()