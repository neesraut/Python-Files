
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
##to make the data list as desired - lets say we need only those list that have ram and shyam in name and need to store in another list

##define/initialize the list outside of loop
'''required_list = []
for each in test_dict:
    if each['name'] in ['Ram','Shyam']:
        required_list.append(each)
print("the required list is {required_list}".format(required_list=required_list))
'''

##FUnction In Python 
##no arguments
'''
def appendList():
    list1=[1,2,3]
    list2=[4,5,6]
    list3 = []
    list3.append(list1)
    list3.append(list2)
    print("The appended List is {list3}".format(list3=list3))

appendList()  #calling function
'''
##function with Arguments
'''
def appendList(list1,list2):
    list3 =[]
    list3.append(list1)
    list3.append(list2)
    print("The appened list is{list3}".format(list3=list3))

list1=[1,2,3]
list2=[4,5,6]
appendList(list1,list2)
'''

##function with return type
'''list3 = []
def returnAppendedList(list1,list2):
    list3.append(list1)
    list3.append(list2)
    return list3

print("The appended list is {appendedList}".format(appendedList = returnAppendedList([1,2,4],[5,9,10])))
'''

##CLASS AND OBJECTS- OOP CONCEPTS

class UserData:
    def __init__(self,name,age,country): 
        ##constructor, when the class is called or the object is made this is initialized first
        ##in order to set the variable, to make the data that is mostly used in class
        ##self is the default parameter, can be any
        self.name = name
        self.age = age
        self.country = country
    
    def printUserDetails(self):
        print("The user name is {name}, age is {age}, country is {country}".format(name=self.name,age=self.age,country=self.country))

### userData1 = UserData("ram",'5','china')
### userData1.printUserDetails()

##Another class using other class objects
class UserSalaray:
    def __init__(self,userDataAsObject):
        self.name = userDataAsObject.name
        self.age = int(userDataAsObject.age)

        self.country = userDataAsObject.country
        if self.age <=24:
            self.salary = "10000"
        else:
            self.salary="20000"
        
    def showUserDetails(self):
        print("The user name is {name} with age {age} who lives in {country} has a salary amount of {salary}".format(name=self.name,age=self.age,country=self.country,salary=self.salary))


##make the object of the class that you want to use the attributes
userData1 = UserData("ram",'5','china')
userSalary1 = UserSalaray(userData1)
userSalary1.showUserDetails()



