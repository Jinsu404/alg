def solution(keymap, targets):
    answer = []
    
    for w in targets:
        cnt = 0
        for c in w:
            l = 101
            for k in keymap:
                if c in k:
                    l = min(k.index(c)+1, l)
            if l == 101: 
                cnt = -1 
                break
            cnt+=l
        answer.append(cnt)
        
    return answer