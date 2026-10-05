''' random.seed() usage
import random
#x=random.randint(1,10)
#y=random.randint(1,10)
#z=random.randint(1,10)
#print(x)
#print(y)
##print(z)
#random.seed(7) '''

''' f strings usage
order_number = 1234
order_id = f"ORD{order_number:03d}"
print(order_id)'''

''' random.choice() usage '''
"""import random
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
random.seed(3)
print(random.choice(weekdays))
print(random.choice(weekdays))
print(random.choice(weekdays))"""

''' print using for loop '''
"""
for n in range(1,7):
    print(f"SEAT{n:02d}") """

''' datetime module usage  '''
"""import datetime
import random
random.seed(5)
start_date = datetime.date(2024,1,1)
days_to_add = random.randint(0,364)
print(start_date + datetime.timedelta(days=days_to_add)) """

'''csv writer usage'''

import csv
import random
random.seed(9)
with open("scores1.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["player_id","score"])
for n in range(1,6):
    writer.writerow([f"P{n:02d}",random.randint(0,100)])
    
