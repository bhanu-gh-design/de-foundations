#This code generates customers.csv(Columns: `customer_id,name,state,created_at`) and accounts.csv(Columns: `account_id,customer_id,account_type,opened_at,status`) files with data. It generates 50 customers and 100 accounts with random data
import random
import csv
import datetime
random.seed(42)
acct_types = ["CHECKING","SAVINGS"]
statuses =["ACTIVE","CLOSED"]
states =["TX","GA","MI","CA","CO"]
with open("customers.csv","w",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(['customer_id','name','state','created_at'])
    for n in range(1,51):
        cid = f"C{n:04d}"
        cname = f"Customer_{cid}"
        cre_dt = datetime.date(2024,1,1)+datetime.timedelta(days=random.randint(0,900))
        writer.writerow([cid,cname,random.choice(states),cre_dt])
with open("accounts.csv","w",newline="") as f2:
    writer=csv.writer(f2)
    writer.writerow(['account_id','customer_id', 'account_type', 'opened_at', 'status'])
    for n in range(1,101):
        aid=f"A{n:04d}"
        open_dt = datetime.date(2024,1,1)+datetime.timedelta(days=random.randint(0,900))
        writer.writerow([aid,f"C{random.randint(1,50):04d}",random.choice(acct_types),open_dt,random.choice(statuses)])