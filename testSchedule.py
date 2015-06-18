import sys

Week = {'Monday': 0, 'Tuesday': 1440, 'Wednesday': 2880, 'Thursday':4320, 'Friday':5760}

def transformTime(timeSlot):
    slotRange = []
    timeSlot = timeSlot.split()
    day_sum = Week[timeSlot.pop(0)]
    timeSlot = timeSlot[0].split("-")
    for i in range(len(timeSlot)):
         time = timeSlot[i].split(":")
         slotRange.append(day_sum + int(time[0])*60 + int(time[1]))
    slotRange[1] -= testLength
    return slotRange

text = sys.stdin.read().split('\n')
text.pop()
testLength = int(text[0].split()[0])
most = int(text[0].split()[1])
all_students = []

for i in range(1,len(text)):
    student = []
    schedule = text[i].split(",")
    for x in schedule:
        slot = transformTime(x)
        student.extend(range(slot[0],slot[1]+1))
    all_students.append(set(student))

test_time = 0
top_num = 0

while test_time < 7200:
    summed = 0
    for x in all_students:
        if test_time in x:
            summed +=1
    if summed > top_num:
        top_num = summed
        if summed == most:
            break
    test_time += 1

print top_num
