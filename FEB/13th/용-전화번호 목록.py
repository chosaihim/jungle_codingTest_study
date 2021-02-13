# https://programmers.co.kr/learn/courses/30/lessons/42577

phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    for i in phone_book:
        i2 = list(i)

        for j in phone_book:
            if len(i) > len(j): continue
            if i == j: continue
            j2 = list(j)

            # 만약 접두어가 아니면 skip한다. 
            skip = False
            for k in range(len(i2)):
                if i2[k] != j2[k]:
                    skip = True
            
            if skip == False:
                return False
    
    return True

print(solution(phone_book))