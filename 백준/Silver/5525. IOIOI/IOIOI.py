N,M,S = int(input()),int(input()),input()
x,y,z = (M-N*2),N*2+1,"IO"*N+"I"
print(sum((S[i:y+i]==z) for i in range(x)))