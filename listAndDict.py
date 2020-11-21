
##list and dict combo - msot used in real world
#for single line commenting use # and for bulk lines use '''
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
'''for each in test_dict:
   print("Each Dict Item")    
   print("Name is:{name}, class is :{classs}, country is: {country}\n".format(name=each['name'],classs=each['classs'],country=each['country']))
'''
#to print/access the items from dict within list that has particual data in it
'''for each in test_dict:
    if each['name']=='Ram':
        print(each)
'''

##to print the data where there is multiple conditions
'''for each in test_dict:
    if each['name'] in ['Ram','Hari']:
        print("The filtered elements are{each}".format(each=each))
'''
##to print the data where there is multiple conditions for different element
'''for each in test_dict:
    if each['name']=='Ram' and each['classs']=='5':
        print("Data with name ram and class 5 is {each}".format(each=each))
'''
