import csv

FILE1 = "Location14.22.19.026369.csv"
FILE2 = "Location17.00.11.773067.csv"
FILE3 = "Location17.28.42.949897.csv"
FILE4 = "Location17.55.18.263808.csv"
FILE = "Location-filter.csv"

previous = {
    "A": -1,
    "B": -1,
    "C": -1
}
sum = {
    "A": 0,
    "B": 0,
    "C": 0
}
count = {
    "A": 0,
    "B": 0,
    "C": 0
}
max = 0

# writeFile = open("LocationDensity.csv", "w")
# wr = csv.writer(writeFile)

with open(FILE) as f:
    reader = csv.reader(f)

    for line in reader:
        nowNumber = float(line[0][6:])

        if previous[ line[1] ] != -1:
            interval = nowNumber - previous[ line[1] ]
            if interval < 0: interval = interval + 60

            sum[ line[1] ] += interval
            count[ line[1] ] += 1

            print(line[1], line[0], "%.2f"%interval)
            # wr.writerow([line[1], line[0], "%.2f"%interval])

            if interval > max:
                if interval < 40:
                    max = interval
        previous[ line[1] ] = nowNumber
    
    print(count["A"] + count["B"] + count["C"])
    print(count["A"])
    print(count["B"])
    print(count["C"])

print("--------")
print(sum["A"] / count["A"])
print(sum["B"] / count["B"])
print(sum["C"] / count["C"])
print(max)