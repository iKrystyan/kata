def solution(number):
    if number < 0:
        return 0
    
    multiples = []
    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            multiples.append(num)

    return sum(multiples)

print(solution(10))