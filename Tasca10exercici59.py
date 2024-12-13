def primers(max):
    print(1)
    for i in range(2, max+1):
        primer = True
        for j in range(2,i):
            if(i%j==0):
                primer = False
        if primer:
            print(i)

primers(100)