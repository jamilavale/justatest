'''
Multiline Strings::
   This is an example of a multiline comment - it could be 3 single quotes or 3 double quotes
'''

"""
This is also a 
multiline comment
"""



#This is an example of setting a string to use Title Case
example = 'this is a string'
print(example.title())

'''
This is how you can create a string from a list - 
for example, a filename with underscores between the arguments
'''
print('_'.join(['LG','09122019','logcat']))


'''
This is how you split a string into a list - using an underscore as a delimiter
'''
print('LG_09982019_logcat'.split('_'))