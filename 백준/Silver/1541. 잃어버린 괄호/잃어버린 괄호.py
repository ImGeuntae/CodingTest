a,*b = (sum(map(int,x.split('+'))) for x in input().split('-'))
print(a-sum(b))