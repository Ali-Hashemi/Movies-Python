from Config import *
import csv
from Classes.ClassUtility import *

# with open("eggs.csv", "w", newline='') as csv_file:
#     spamwriter = csv.writer(csv_file, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam ' * 2, 'Lovely Spam', 'Wonderful Spam'])
#

with open('eggs.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Print.print_white(row['first_name'], row['last_name'])
