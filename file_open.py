#Opening file

filename=open('words.txt')
for line in filename:
    print(line.upper().rstrip())
filename.close()


second_file=open('mbox.txt')
sum=0
count=0
for line in second_file:
    if line.startswith("X-DSPAM-Confidence:"):
        sum=sum+float(line[-7:-1])
        count=count+1
print("Average spam confidence:",sum/count)
    