def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    bucket1 ,bucket2 = [], []
    gyo, hab = 0, 0
    for i1 in range(len(str1)-1) :
        front,back = str1[i1],str1[i1+1]
        #? re.findall('[^a-zA-Z]+', str1[i:i+2]) 
        #? str.isalpha() 함수 활용해보기
        if (ord('a') <= ord(front) and ord(front) <= ord('z'))  \
            and (ord('a') <= ord(back) and ord(back) <= ord('z')):
            bucket1.append((front,back))
    for i2 in range(len(str2)-1) :
        front,back = str2[i2],str2[i2+1]
        if (ord('a') <= ord(front) and ord(front) <= ord('z'))  \
            and (ord('a') <= ord(back) and ord(back) <= ord('z')):
            bucket2.append((front,back))


    gyo, hab = 0, len(bucket1) + len(bucket2)
    for b in bucket1 :
        if b in bucket2 :
            gyo += 1
            bucket2.remove(b)
    if gyo == 0 and hab == 0:
        return 65536
    return  int((gyo / (hab - gyo)) * 65536)
