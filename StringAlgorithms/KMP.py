
def computeLPS(text):
    length = len(text)
    LPS = [0]*length
    slow = 0
    fast = 1

    while fast<length:
        if text[fast]==text[slow]:
            slow+=1
            LPS[fast] = slow
            fast+=1
        elif text[fast]!=text[slow] and slow>0:
            slow-=1
        else:
            LPS[fast] = 0
            fast+=1

    return LPS

def KMP(text,pattern):
    LPS = computeLPS(pattern)
    limit = len(pattern)
    j = 0

    for i in range(len(text)):        
        if text[i] == pattern[j]:
            j+=1
            if j == limit:
                j=0
                print("pattern found at index " + str(i-limit+1))
        elif text[i] != pattern[j]:
            j = LPS[j]




KMP("acfacabacabacacdkacabacacd","acabacacd")
