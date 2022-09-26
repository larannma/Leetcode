n = int(input())
map_input = {}
map_names = ()

for i in range(n):
    map_input[i] = list(input().split(","))

for i, a in map_input:
    map_names[i] = set(map_input[i][0])


print(map)