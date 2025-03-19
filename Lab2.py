# While Loop
i = 0                          
while ( i < 5 ) :              
    print ( i )                 
    i = i + 1                   
print () 

# For loop 
# 1. List
color_list = [ "red", "yellow", "blue", "red", "white" ]   
for i in color_list :                            
    print( i )
print ()

# 2. Tuple
fruit_tuple = ( "apple", "mango", "banana", "kiwi", "tomato" )   
for i in fruit_tuple :               
    print( i )
print ()

# 3. String
name_string = "ibrahim"   
for i in name_string :        
    print( i )
print ()

# For loop using range() function with Numbers
# 1. range 
for i in range ( 5 ) :                         
    print ( i )
print ()

# 2. range ( 2 parameters i.e intialization , condition )
for i in range ( 2, 5 ) :                      
    print ( i )
print ()

# 2. continue
for value in [ "I" , "Am" , "ibrahim" , "butt" ] :
    if ( value == "ibrahim" ) :
        continue
    print( value )
    
# Funtions basic structure
def myName () :                               
    print ( "I am ibrahim butt" )


myName()                                        
print ()

# Function with parameters
# 1. str as parameter
def fullName ( first_name, last_name ) :       
    print ( f"Your full name is {first_name} {last_name}." )


fullName ( "Ali" , "Akbar" )
fullName ( "Ahsan" , "Alahi" )
fullName ( "Ibrahim" , "Butt")
print ()

# 2. int as parameter
def sum ( num1, num2 ):
    print ( num1 + num2 )


sum ( 10 , 20 )
sum ( 5 , -10 )
print ()

# 3. list as parameter
def listSum( full_list ) :
    sum = 0 
    for index in range ( len ( full_list ) ) :
        sum += full_list[ index ]
    print ( "Sum =", sum )


listSum ( [ 10, 20, 30, 40 ] )
listSum ( [ -1, 1, 0, 3, 4 ] )
listSum ( [ 1 + 2j, 2 + 5j ] )
print ()

# default parameter
def countryName ( country = "Pakistan" ) :
    print ( "Your country is", country )


countryName ( "India" )
countryName ( "Australlia" )
countryName ()
print ()

# return statement in Functions
def findValue ( full_list, value ) :
    for i in range ( len ( full_list ) ) :
        if ( full_list[i] == value ) :
            return i
    return -1


numbers_list = [ 5, 10, 15, 0, 12 , "1" ]
index = findValue ( numbers_list, 1 )
if ( index == -1 ) :
    print ( "Not Found" )
else :
    print ( "Found at index", index )
print ()

# Keyword Arguments
def num3Value ( num1, num2, num3 ) :           
    print ( "Num3 =", num3 )

    
num3Value ( num3 = -1, num2 = 5, num1 = 100 )
num3Value ( num3 = 1000, num2 = 75, num1 = 2 )
print ()

# variable number of parameters
def product ( *numbers ) :
    prod = 1
    for num in numbers :
        prod = prod * num 
    print ( "Product =", prod )

        
product ( 10, 5 )
product ( 1, 2, 12 )
product ( 5, 4, 0)
product ( 10, "* ")
print ()

# Classes basic structure
class Test :
    x = 5
    
obj1 = Test() 
print ( obj1.x )

# __init__ function in classes ( Constructor )
class Person :
    def __init__ ( this, name, age ) :                 
        this.name = name
        this.age = age
        

per1 = Person ( "Ahmed", 19 )                         
per2 = Person ( "ibrahim", 21 )                          
print ( per1.name, per1.age )
print ( per2.name, per2.age )

# methods in classes
class Person :
    def __init__ ( this, name, age ) :                 
        this.name = name
        this.age = age
        
    def personName ( this ) :
        print ( "Person name is", this.name )

per1 = Person ( "ibrahim", 21 )                          
per1.personName ()