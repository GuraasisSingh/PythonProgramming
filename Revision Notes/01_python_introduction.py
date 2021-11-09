# -*- coding: utf-8 -*-
"""01 Python Introduction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RQSGzvMyY_CE5Icf25roUXLoLz0Zq42g

#Introduction to Python

Python is one of the most popular programming languages in the world right now. This is because of how easy it is to code in this language. Most syntax is very close to the English language that you and I speak. In addition, you can do a lot of things in Python from simple dice program to full featured websites, robotics and even artificial intelligence!!!

**Advantages and disadvantages of Python**

One of the major reasons for the vast popularity of python is because of its huge number of advantages and very little disadvantages.

Advantages:
* Very easy to learn
* very simple syntax requirement
* large number of libraries 
* large community support
* Dynamic
* Object-oriented
* can integrate with c, C++ and java

Disadvantages:
* slow execution
* uses a lot of memory

**Did you know?**

The Python language was not named after the popular snake species but instead on Monty Python, a British comedy series, which the creator of Python was a huge fan of.

## Print function

Print is one of the most simplest functions in Python. Its allows the developer to display any data on the screen. To do that, you have to write the keyword print followed by the data you wish to show inside the parenthesis

example:
```
print(data)
```

If the data is of type string (letters or words), then we should write the string inside single or double quotes (' ' or " ")

**example:**
"""

print("I am Batman!!!")        #here the sentence is a string, therefore written in quotes

"""


If the data to be printed is a number, we can directly write it without quotes.

**example:**

"""

print(100)                     #here the data is a number, hence can be written directly without quotes

"""You can also print multiple items in a single print command by separating them with commas

For example:
"""

print("i have",100,'apples')
print('there are',50, 'states in the usa')

"""if you notice, in the above example, print shows 2 default behavior
* automatically adds a space between the items in the print function
* prints each print output on a new line

Both the default behaviours can be changed using the keywords sep and end respectively. The default values for sep=" " (space) and end="\n"(new line), but these can be changed

For example,
"""

print("i have",100,'apples',sep="*", end="@@@@")
print('there are',50,'states in the usa', sep="\t", end="!!!")         #\t denotes one tab space

"""##Variables

Just like how we store our stuff in different boxes/jars and later access them when we need it, in python too we have boxes to store different values such as strings, numbers and other data. These boxes are called variables. 

Variables can store any data we want and we can access them when we want to. We can even change the data inside the variables if required.

To store a value inside a variable we need to write the name of the variable and equate it to the value


```
variable_name = value
```

We can even use variables in our code instead of using the values directly.

**Example**
"""

name='Batman'
print(name)        #instead of writing Batman inside the print function, we are writing the variable inside which batman is stored

age=10
print(age)         #here we use the age variable inside print, instead of writing the number directly

"""**Rules for Python variables:**

* A variable name must start with a letter or the underscore character
*    A variable name cannot start with a number
* A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
* Variable names are case-sensitive (age, Age and AGE are three different variables)

**Type casting**

Though python dynamically assigns a data type to a variable, Sometimes we might need to specify a data type or convert certain data types to a different data type, like string to integer or vice versa. 

There are 3 major variable types that you need to know
* int(): this can only contain integer values
* float(): used to store decimal numbers
* str(): used to store strings (text)

for example:
"""

x=str(10)
print(type(x))     #to check the datatype of any item we can use the type method

x=int(10)
print(type(x)) 

x=float(10)
print(type(x))

"""##Input

We might want to take certain data directly from the user and use it in our code. For that we have the input method.



```
variable=input('question that you want to prompt to the user')
```

Example

"""

name=input('Please enter your name ')

print(name)

"""note that input is always stored as string. As such, if we are inputing numbers with the intent of using it in arithmatic operations, then we should 1st convert them to int or float

For example, 

lets print the age of the user after 5 yrs
"""

age=int(input('What is your age?'))
print(age+5)

"""##Try it yourself:

**Do the following tasks:**
* store the following sentence in a variable: 'I am going to be the best coder'
* print the variable
* print the number 565

**Solution**
"""

sentence='I am going to be the best coder'

print(sentence)
print(565)