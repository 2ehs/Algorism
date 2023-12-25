# 연습문제 1 

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n + fact(n- 1)

# print(fact(10))

# 연습문제 2

def max(n):
    if len(n) == 1:
        return n[0]
    else:
        if n[0] < n[1]:
            n.remove(n[0])
            return max(n)
        else:
            n.remove(n[1])
            return max(n)

print(max([10,4,2,3,6,99,12]))