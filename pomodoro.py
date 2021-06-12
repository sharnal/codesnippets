#!/usr/bin/env python


# pomodoro calculator
# When studying courses on udemy or elsewhere, I'd like to know how many pomodoros ( chunks of 20 minutes ) is
# it equal to? Of course, it may take much longer than just the lenght of the videos as you may spend time in labs,
# or setup time, etc. One day I'd like to make a chrome extension out of it that can parse the times and tell you
# how many pomodoros its equal to, maybe even track it for you. For now, I'd just like to do it manually.

total_minutes = 0

while True:
    duration = input("Enter a time\n")
    print(duration)

    if len(duration) == 0:
        break

    exploded = duration.strip().split(":")
    print(exploded)
    total_minutes = total_minutes + int(exploded[0]) * 60 + int(exploded[1])
    print("Total duration(running) {}".format(total_minutes))
    continue

print("Total duration in minutes: {}".format(total_minutes))
print("Total hours:minutes: {0:02}:{1:02}".format(total_minutes//60, total_minutes%60))
print("Number of pomodoros: {}".format(total_minutes/20))
