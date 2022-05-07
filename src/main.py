color_code_dict = {'2': 'B',
                   '3': 'G',
                   '4': 'Y',
                   '5': 'R',
                   '7': '',
                   '6': '',
                   '1': ''}
if __name__ == '__main__':
    import csv
    loc = 45
    time = 0.010
    timeBetweenBlocks = 0

    output = ""
    with open("../data/4_1.csv") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # skip first row

        next(reader)  # skip next row
        prev = 0
        timeAfterTimeout = 0
        for row in reader:
            # if timer times out
            if timeBetweenBlocks == 0:
                timeBetweenBlocks = time * loc
                output += color_code_dict[row[1][0]]
                prev = row[1]
            # if we encounter a new color
            elif prev != row[1]:
                # if we encounter it moments after we added one
                if timeAfterTimeout < 0.020:
                    output = output[:-1]  # remove last char
                    # reset timer
                    timeAfterTimeout = 0
                # if we just encountered a new one
                output += color_code_dict[row[1][0]]
                timeBetweenBlocks = time * loc
                # update the prev
                prev = row[1]

            timeBetweenBlocks -= 0.010
            timeAfterTimeout += 0.010
            # print(', '.join(row))

    print(output)
