# importing packages 
import pandas as pd 

# create data 
df = pd.DataFrame([ 
				[180000, 110, 18.9, 1400], 
				[360000, 905, 23.4, 1800], 
				[230000, 230, 14.0, 1300], 
				[60000, 450, 13.5, 1500]], 
	
				columns=['Col A', 'Col B', 
							'Col C', 'Col D']) 

# view data 
print(df)

##########################################################
import matplotlib.pyplot as plt  #pip install matplotlib

df.plot(kind = 'bar')
plt.show()


##############################################
# copy the data 
df_max_scaled = df.copy() 

# apply normalization techniques 
for column in df_max_scaled.columns: 
	df_max_scaled[column] = df_max_scaled[column] / df_max_scaled[column].abs().max() 
	
# view normalized data 
print(df_max_scaled) 


####################################################
import matplotlib.pyplot as plt 
df_max_scaled.plot(kind = 'bar')
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

# Assuming you have a DataFrame called df_max_scaled
# containing your data
df_max_scaled.plot(kind='bar')
plt.show()

#######################################################
# copy the data 
df_min_max_scaled = df.copy() 

# apply normalization techniques 
for column in df_min_max_scaled.columns: 
	df_min_max_scaled[column] = (df_min_max_scaled[column] - df_min_max_scaled[column].min()) / (df_min_max_scaled[column].max() - df_min_max_scaled[column].min())	 

# view normalized data 
print(df_min_max_scaled)

###################################################################
import matplotlib.pyplot as plt 
df_min_max_scaled.plot(kind = 'bar')
plt.show()

#########################################################################
# copy the data 
df_z_scaled = df.copy() 

# apply normalization techniques 
for column in df_z_scaled.columns: 
	df_z_scaled[column] = (df_z_scaled[column] -
						df_z_scaled[column].mean()) / df_z_scaled[column].std()	 

# view normalized data 
print(df_z_scaled)

##########################################################################
import matplotlib.pyplot as plt 
df_z_scaled.plot(kind='bar')
plt.show()

###########################################################################


