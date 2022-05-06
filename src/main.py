if __name__ == '__main__':
    import csv

    with open("data/1_1.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(row)
            # print(', '.join(row))
