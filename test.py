import heapq
h = []
data = [(0,1),(2,4),(1,2),(5,3),(4,0)]
for d in data:
    heapq.heappush(h,d)

print(h)
for i in range(len(data)):
    print(heapq.heappop(h),h)
