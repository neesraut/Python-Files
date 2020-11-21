
##list and dict combo - msot used in real world
test_dict =[
            {
                'name':'Ram',
                'classs':'5',
                'country' : 'Nepal'
            },

            {
                'name':'Hari',
                'classs':'6',
                'country' : 'Australia'

            },
            {
                'name':'Shyam',
                'classs':'8',
                'country' : 'China'
            }
]
#print(test_dict)
##print all the elements in list
#for each in test_dict:
   # print("Each element is{each}".format(each=each))

##to print each elements in dictinory items within List
for each in test_dict:
   print("Each Dict Item")    
   print("Name is:{name}, class is :{classs}, country is: {country}\n".format(name=each['name'],classs=each['classs'],country=each['country']))
