# 연습문제 1-1
# def range_b(n):
#     b = 0
#     for i in range(1,n+1):
#         b += i * i
#     print(b) 
# range_b(10)

# 연습문제 1-2 
# O(n)

# 연습문제 1-3
# O(1)

# 연습문제 2-1
# def min_n(a):
#     min = a[0]
#     for i in range(0,len(a)):
#         if min > a[i]:
#             min = a[i]
#     print(min)
# min_n([9,5,4,21,32,43,24,32,3,543,56,4326,526,543,6543,6,54])

# 연습문제 3-1 

a = ["Tom","Jerry","Mike"]
Team = []

for i in range(0, len(a)):
    for z in range(1,len(a)-1):
        Team.append(a[i] + "-" + a[z])
print(Team)
