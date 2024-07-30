##Special characters
# import re
# a="let us see what is meta characteeeers"
# result=re.findall("\s",a) #it checks space
# print(result)
# ##############################

# import re
# a="let us see what is meta characteeeers"
# result=re.findall("\S",a) 
# print(result)

####################################
# it prints only digits
# import re
# a="let us see what is meta characters 12345"
# result=re.findall("\d",a) 
# print(result)

# ######################################
# #it prints except digits
# import re
# a="let us see what is meta characters 12345"
# result=re.findall("\D",a) 
# print(result)

###################################
#except space will come
# import re
# a="let us see what is meta characters 12345"
# result=re.findall("\w",a) 
# print(result)

##############################

#only space will come
# import re
# a="let us see what is meta characters 12345"
# result=re.findall("\W",a) 
# print(result)

###############################

# import re
# a="let us see what is meta characters 12345"
# result=re.findall("[123]",a) 
# print(result)

############################

# import re
# a="let us see what is meta characters 12345"
# result=re.findall("[^123]",a) 
# print(result)

#################################

# import re
# a="let us see what is meta characters 12345"
# result=re.findall("[0-4]",a) 
# print(result)

#####################################

# import re
# a="let us see what is meta characters 456"
# result=re.findall("[0-9][0-9][0-9]",a) 
# print(result)
# ########################################

# import re
# a="let us see what is meta characters 123456 b"
# result=re.findall("[a-c]",a) 
# print(result)

####################################
