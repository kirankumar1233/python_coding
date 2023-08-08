# dictionary
'''1. it is used to store the data in the form of key and values it is a data type in python 
2.it is mutable and key must be single element
3.keys and values seperates with : colon and key value pair separets with , comma
eg; page no= key and content in that page is value
syntax # madhu={}'''

capitals={"andhra":"amaravati","telengana":"hyd","maharastra":"mumbai"}
'''print(type(capitals))
print(capitals["andhra"])
print(capitals["telengana"])
print(capitals["maharastra"])
print(capitals.get('telengana')) #prints value of particular key
print(capitals.keys()) # prints total keys present in dictionary'''


'''print(capitals.values()) # prints total values in a dictionary 
print(capitals.items()) # output: dict_items([('andhra', 'amaravati'), ('telengana', 'hyd'), ('maharastra', 'mumbai')])
capitals.update({"karnataka":"bengaluru"}) #adds last
print(capitals)'''

'''capitals['andhra']="vishakapatnam" #changes the ptaticular key value
print(capitals)
capitals.pop("telengana") # delets particular pair
print(capitals)'''

#for i in capitals:
    #print(i) # prints only keys

'''for i,j in capitals.items():
    #print(i) #prints only keys
    print(j) # prints only values
    #print(i,j)#prints both keys and values'''
    