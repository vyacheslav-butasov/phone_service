import csv
import psycopg2

files = ['DEF-9xx-29.10.2019.csv']
def load(files):
    conn = psycopg2.connect("dbname=phone_service user=slava password=qwr69zxp")
    cur = conn.cursor()
    cur.execute("TRUNCATE caller_id_phone_number")
    for file in files:
        with open('files/' + file, 'r') as f:
            print(file)
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                try:
                    cur.execute(
                        "INSERT INTO caller_id_phone_number (code, start_number, end_number, company, region ) \
                        VALUES ( %s, %s, %s, %s, %s)",
                        row[:3] + row[4:6]) # without capacity column
                except TypeError:
                    print(row[:3] , '|', row[4:6])
    conn.commit() 


load(files)
#cur.execute('SELECT * FROM caller_id_phone_number')
#one = cur.fetchone()
#print(one)
##>>> 3959300518
##3959300518
##>>> 395730000
##395730000
