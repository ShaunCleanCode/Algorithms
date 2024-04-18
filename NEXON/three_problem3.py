import os
def countMeetings(firstDay, lastDay):
    # Pair each investor with their available days and sort by the last day available
    investors = sorted(zip(firstDay, lastDay), key=lambda x: x[1])

    # Keep track of scheduled meeting days to avoid double-booking
    scheduled_days = set()
    meetings_count = 0

    for start, end in investors:
        # Try to schedule a meeting within the investor's available range
        for day in range(start, end + 1):
            if day not in scheduled_days:
                scheduled_days.add(day)
                meetings_count += 1
                break

    return meetings_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    firstDay_count = int(input().strip())

    firstDay = []

    for _ in range(firstDay_count):
        firstDay_item = int(input().strip())
        firstDay.append(firstDay_item)

    lastDay_count = int(input().strip())

    lastDay = []

    for _ in range(lastDay_count):
        lastDay_item = int(input().strip())
        lastDay.append(lastDay_item)

    result = countMeetings(firstDay, lastDay)

    fptr.write(str(result) + '\n')

    fptr.close()
