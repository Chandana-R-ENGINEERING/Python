# Random Password Generator

import random
import string

pass_len=8
charvalues=string.ascii_letters + string.digits + string.punctuation

#List Comprehension [function for i in range]

password="".join([random.choice(charvalues) for i in range(pass_len)])
# password= ""

# for i in range(pass_len):
#     password+=random.choice(charvalues)
    
print("Your random password is :" ,password)