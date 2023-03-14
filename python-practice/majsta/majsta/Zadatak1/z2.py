file1 = open('Zadatak1/worklog.txt', 'r')
count = 0

while True:
    count += 1

    line = file1.readline()

    if not line:
        break
    print("Line{}: {}".format(count, line.strip()))
file1.close()