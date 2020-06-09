N=int(input())
lst=list(map(int,input().split()))
count_e = 0
count_o = 0
for i in range(len(lst)):
    if lst[i]%2==0:
        count_e+=1
    else:
        count_o+=1
if count_e>count_o:
    print("READY FOR BATTLE")
else:
    print("NOT READY")