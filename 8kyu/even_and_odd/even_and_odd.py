def even_and_odd(n): 
    # your code here
    num = str(n)
    NE = "".join(c for c in num if int(c) % 2 == 0)
    NO = "".join(c for c in num if int(c) % 2 != 0)
    
    NE = int(NE) if len(NE) != 0 else 0
    NO = int(NO) if len(NO) != 0 else 0

    return (NE, NO)
    
print(even_and_odd(2468))