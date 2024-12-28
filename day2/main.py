import numpy as np

# f = np.genfromtxt("input.txt")

with open("input.txt") as f:
    input = f.read()

data = [[int(e) for e in l.split(' ')] for l in input.split('\n')]

safe = [True for i in range(len(data))]

for k in range(len(data)):
    report = data[k]
    if report[0] == report[-1]: 
        safe[k] = False
        continue
    is_increasing = report[-1] > report[0]
    fault = 0
    for j in range(len(report)-1):
        diff = report[j+1] - report[j]
        if (is_increasing != (report[j+1] > report[j])) or (diff == 0 or abs(diff) > 3):
            # print(k)
            # print(report)
            # print(is_increasing)
            # print(report[j+1] > report[j])
            # print(diff)
            safe[k] = False
            break

print(sum(safe))

data = [[int(e) for e in l.split(' ')] for l in input.split('\n')]

safe1 = [True for i in range(len(data))]

for k in range(len(data)):
    report = data[k]
    if report[0] == report[-1]: 
        safe1[k] = False
        continue
    fault = 0
    while fault < 2:
        is_increasing = report[-1] > report[0]
        safe1[k] = True
        for j in range(len(report)-1):
            diff = report[j+1] - report[j]
            if (is_increasing != (report[j+1] > report[j])) or (diff == 0 or abs(diff) > 3):
                fault += 1
                safe1[k] = False
                if fault < 2: 
                    report.pop(j)
                break
        if safe1[k] == True: break

data = [[int(e) for e in l.split(' ')] for l in input.split('\n')]

safe2 = [True for i in range(len(data))]

for k in range(len(data)):
    report = data[k]
    if report[0] == report[-1]: 
        safe2[k] = False
        continue
    fault = 0
    while fault < 2:
        is_increasing = report[-1] > report[0]
        safe2[k] = True
        for j in range(len(report)-1):
            diff = report[j+1] - report[j]
            if (is_increasing != (report[j+1] > report[j])) or (diff == 0 or abs(diff) > 3):
                fault += 1
                safe2[k] = False
                if fault < 2: 
                    report.pop(j+1)
                break
        if safe2[k] == True: break

print(sum(np.array(safe1) + np.array(safe2)))