import pandas as pd

df = pd.read_excel('D:/python course/Financial Sample.xlsx')
#print(df)
#print(df.to_string()) 
#print(df.head(10)) 
#print(df.tail(10)) 

new_df = df.info()

#print(new_df)
b=df.sample(4)
#print(b)
c=df.describe()
#print(c)
d=df.sort_values(by='Month Number', ascending=True)
#print(d.head(50))

#s=df[(df.Month Number > 1) & (df.Discount Band < 5)]
s=df.groupby('Country')[["Sale Price"]].mean()
#print(s)

r = df.filter(["Country", "COGS", "Month Number", "Discounts"])
s = r[r["Month Number"] > 1]
print(s.head(10))
#############################################

print(r.head(50))
y=r.isna().any()
print(y)
########################################
u=r.fillna(r.COGS.mean())
ut=r.fillna(r.COGS.median())
print(u.head(10))
print(ut.head(10))
####################################
t=r[r.COGS>10000]
print(t.head(10))

#####################################
h=r.COGS.quantile(1.0)
print(h)

###################################
