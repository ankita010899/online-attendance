#import csv
from extract import send_details


def find_missing():
    numbers = []
    d = send_details()

    for data in d:
        for word1 in data:
            for word in word1.split():
                numbers.append(str((''.join(filter(str.isdigit, word)))))

    while '' in numbers:
        numbers.remove('')

    numbers = [int(i) for i in numbers]
    numbers = sorted(set(numbers))
    print("Numbers = ", numbers)

    full_list = [x for x in range(numbers[0], numbers[-1] + 1)]

    missing = (list(set(numbers) ^ set(full_list)))

    print("Missing = ", missing)
    return missing

'''def print_absent():
    #print("\nMissing numbers generated!!!")
    result = find_missing(numbers)
    print("Absent = ", result)
    return result
#print("DONE!")'''
'''

#CSV CODE


csvfile=open('test1.csv','w', newline='')

obj=csv.writer(csvfile)

csvfile.close()

'''


'''

#TESTING

str1="01_kjhgv"
print(''.join(filter(str.isdigit, str1)))
'''