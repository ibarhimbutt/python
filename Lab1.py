# We use hash for comments in Python

# This is how we show an output string
print ( "Hello Guys, I'm Python developer" )

# This is how we show any number as an output
print ( 100 )

# Variable Declaration
a = 10
b = 3.35
c = 2e-2
d = 10E3
e = 1 + 2j
f = 5 + 3J
g = "okay."
h = "It's said "
i = '"Dream Big and Dare to Fail!"'
j = True


print ( a, b, c, d, e, f, g, "\n", h+i, j )

# Datatype Checking Function
print ( type ( a ) )
print ( type ( b ) )
print ( type ( c ) )
print ( type ( d ) )
print ( type ( e ) )
print ( type ( f ) )
print ( type ( g ) )
print ( type ( h ) )
print ( type ( i ) )
print ( type ( j ), "\n" )

# TypeCasting
w = complex ( 9, 4 ) 
x = str ( 100 )
y = int ( 100 )
z = float ( 100 )

print ( w )
print ( x )
print ( y )
print ( z )

print ( type ( w ) ) 
print ( type ( x ) )
print ( type ( y ) )
print ( type ( z ) )

# Two Statements in same line
print ( w ) ; print ( x )

# String indices and accessing
name = "Ibrahim butt"

print ( name )

# String indices
print ( name[0] )
print ( name[-12] )

# String slicing
print ( name[ 1 : 5 ] )
print ( name[ 6 : ] )
print ( name[ : 6 ] )

# List
listNumber = [ "List", 12, True ]

print ( listNumber )

# List indices
print ( listNumber[0] )

print ( type ( listNumber[0] ) )
print ( type ( listNumber[1] ) )
print ( type ( listNumber[-1] ) )

# List slicing
print ( listNumber[ 0: 1 ] )
print ( listNumber[ 0 : 2 ] )