def solution(answers):
    
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = {}
    temp = []

    number = 0
    for x in answers :
        if number % 4 == 0 : 
            a.extend(a)
        if number % 7 == 0 : 
            b.extend(b)
        if number % 10 == 0 : 
            c.extend(c)
            
        if x == a[number] :
            temp.append(1)
        if x == b[number] :
            temp.append(2)
        if x == c[number] :
            temp.append(3)
        number = number + 1 
    
    for i in temp:
        try: count[i] += 1
        except: count[i]=1
    
    if 


    print(count)

    answer = list(count.keys())

    print(answer)

    return answer

solution([1, 3, 2, 4, 2])   