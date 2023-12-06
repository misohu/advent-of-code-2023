# input1 = {
#     'Time': [7, 15, 30],
#     'Distance': [9, 40, 200]
# }
# input1 = {
#     'Time': [58, 81, 96, 76],
#     'Distance': [434, 1041, 2219, 1218]
# }

# input1 = {
#     'Time': [71530],
#     'Distance': [940200]
# }

input1 = {
    'Time': [58819676],
    'Distance': [434104122191218]
}

res = 1 

for i in range(len(input1["Time"])):
    # find start
    start = 0 
    for wait in range(1, input1["Time"][i] + 1):
        distance = wait*(input1["Time"][i] - wait)
        if distance > input1["Distance"][i]:
            start = wait
            break

    # find stop
    stop = 0
    for wait in range(input1["Time"][i], 0, -1):
        distance = wait*(input1["Time"][i] - wait)
        if distance > input1["Distance"][i]:
            stop = wait
            break
    res *= (stop - start + 1)

print(res)