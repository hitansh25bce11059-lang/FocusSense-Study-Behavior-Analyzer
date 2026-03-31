studyTimes = []
distTimes = []

def takeData():
    while True:
        print("\nAdd a study session")
        s = input("Study hours: ")
        d = input("Distraction hours: ")

        try:
            s = float(s)
            d = float(d)
        except:
            print("Enter valid numbers")
            continue

        studyTimes.append(s)
        distTimes.append(d)

        more = input("Add another session? (y/n): ").lower()
        if more != "y":
            break


def calcTotal(arr):
    total = 0
    for i in arr:
        total += i
    return total


def productivity():
    totalStudy = calcTotal(studyTimes)
    totalDist = calcTotal(distTimes)

    if totalStudy + totalDist == 0:
        return 0

    return (totalStudy / (totalStudy + totalDist)) * 100


def worstSession():
    worst = -1
    index = -1

    for i in range(len(studyTimes)):
        total = studyTimes[i] + distTimes[i]
        if total == 0:
            continue

        p = (studyTimes[i] / total) * 100

        if worst == -1 or p < worst:
            worst = p
            index = i

    return index, worst


def giveAdvice(p):
    if p >= 80:
        return "You are in a strong focus zone. Maintain this."
    elif p >= 60:
        return "Decent focus but distractions are creeping in."
    elif p >= 40:
        return "Your attention is unstable. You need structure."
    else:
        return "Heavy distraction pattern detected. Immediate correction needed."


def main():
    print("=== FocusSense ===")

    takeData()

    if len(studyTimes) == 0:
        print("No data entered")
        return

    p = productivity()
    idx, worst = worstSession()

    print("\n--- Analysis ---")
    print(f"Total sessions: {len(studyTimes)}")
    print(f"Overall Productivity: {round(p,2)}%")

    print("\nInsight:")
    print(giveAdvice(p))

    if idx != -1:
        print(f"\nLowest focus session: Session {idx+1} ({round(worst,2)}%)")

    if p < 50:
        print("Suggestion: Try fixed study blocks like 25 mins focus / 5 mins break")

    print("\nDone.")


if __name__ == "__main__":
    main()
