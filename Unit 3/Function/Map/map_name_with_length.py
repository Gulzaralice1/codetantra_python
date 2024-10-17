# using map function find the length of number
name = ["alice","gulzar","raja"]  #, [5 , 6  4]
def find_lengh(name): #name is parameter
    return len(name)

mapped_object = map(find_lengh,name)  #Here name pass one by one just like -----> 
# 1st name is "alice"  function find its length,    
# 2nd name is "gulzar" function find its length,
# all length store in box at the end we are printing length of name 
print(list(mapped_object))  # [5, 6, 4]
print(type(map))  # class 
print(type(mapped_object))  # map