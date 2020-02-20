#understanding how if...else statments work in python
#say we have two variables with the same value and we wanted to do something
#only under the condition that both of those values are same
a = 'raj'
b = 'raj'

#we check if the values of a and b are the same with the '==' sign
#if they are the same then the block of code underneath gets executed and the
#else part isn't executed
if(a == b):
    print('hello world')
else:
    print('something else')

#(o/p) → hello world-------------------------------------------------------------------------------------------------------

#now say that we had 2 numbers of which number_1 is smaller than number_2
#and we wanted to add them only if number_2 was smaller
number_1 = 2
number_2 = 4

# then you could do something like this
if(number_2 < number_1):
    final_number = number_1 + number_2
    print(final_number)
else:
    print('not adding the numbers')

#(o/p) → not adding the numbers----------------------------------------------------------------------------------------------

#lets understand how to use if statements with boolean values
#say c is true and d is false
c = True
d = False

#the if section would get executed and the else section wouldn't
#this is because we are always checking if the condition in the parenthesis is true or not
#if so, we execute that block otherwise we move to the else part
if(c):
    print('hello world')
else:
    print('no hello world displayed')
    
#(o/p) → hello world ----------------------------------------------------------------------------------------------------------

#this is interesting... 'not c' would translate to '!c' in many other programming languages
#NOTE: in python '&&' → 'and', '||' → 'or' and '!' → 'not'
#therefore, the else part of the condition will get executed as the if condition is now false
if(not c):
    print('will execute if c is false')
else:
    print('will execute if c is true')
    
#(o/p) → will execute if c is true --------------------------------------------------------------------------------------------
