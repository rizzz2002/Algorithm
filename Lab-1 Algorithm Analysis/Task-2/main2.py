file1=open("D:\Alg\Lab-1 Algorithm Analysis\Task-2\input.txt","r")
length=file1.readline()
arr=file1.readline().strip("\n").split(" ")

def bubbleSort(arr):
    ck=check(arr)
    if ck:
      for i in range(len(arr)-1):
          for j in range(len(arr)-i-1):
              if arr[j] > arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def check(arr):
  for t in range (len(arr)-1):
    if arr[t]>arr[t+1]:
      return True
  return False

array=bubbleSort(arr)
file1.close()

file2=open("D:\Alg\Lab-1 Algorithm Analysis\Task-2\output.txt","w")
for q in range (int(length)):
  if q==(int(length)-1):
      file2.writelines(array[q])
  else:
    final=array[q]+" "
    file2.writelines(final)
    final=""
file2.close()