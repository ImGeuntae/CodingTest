print(sum([(ord(b)-96)*(31**a)for a,b in zip(range(int(input())),input())])%1234567891)