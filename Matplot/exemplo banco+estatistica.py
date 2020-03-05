import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import psycopg2
import time

##%matplotlib inline
##sns.set()

conn_str = "host={} dbname={} user={} password={}".format('localhost','python','postgres','admin')
conn = psycopg2.connect(conn_str)
conn.set_isolation_level(0)

df = pd.read_sql('select *from empregado',con = conn)

##df.plot(kind = "scatter",
##                x = "lotacao", y = "salario",
##                title = "lotacao X salario")
##plt.show()

##plt.hist(df["salario"])
##plt.title("Histograma do salario")
##plt.xlabel("Valor")
##plt.ylabel("Frequencia")
##print(df)
##time.sleep(4)
##plt.show()
##


#print(np.max([1,2,3,4,5,6,7,8,9]))

cursor = conn.cursor()
cursor.execute("select * from departamento")
rows = cursor.fetchall()
print(rows)
