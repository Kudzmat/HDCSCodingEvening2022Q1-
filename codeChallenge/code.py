def findDisarium(start: int, fin: int):

    disariums = []
    for num in range(start, fin):  # range of the initial numbers
        num2 = str(num)  # we want to the string variant of each number
        i = 0
        x = 1
        total = 0
        while i < len(num2):  # basically each digit in the number
            total += int(num2[i]) ** x
            i += 1
            x += 1
        if total == num:
            disariums.append(num)
        else:
            continue

    # printing solution
    print(*disariums, sep="| ")


case_1 = [1, 600]
case_2 = [50, 2000]
case_3 = [150, 3000000]
case_4 = [-6, 200]

findDisarium(case_1[0], case_1[1])  # works well
findDisarium(case_2[0], case_2[1])  # works well
"""
findDisarium(case_3[0], case_3[1]) takes long to execute, function needs improvement
"""

