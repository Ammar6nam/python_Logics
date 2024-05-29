   
users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]


def has_hits (string):
    factor1=1
    index1=0
    for index0 in users:
        if index0['name']== string:
            condition1=users[index1]['items']
            if len (condition1) >(0):
                index2=0
                for index3 in condition1:
                    if 'reads' in index3:
                        #print(index3)
                        if index3['reads']>1000:
                            x=0
                            checkConditios=0
                        else:
                            x=1
                        factor1*=x
                    else:
                        x=1
                    index2+=1                    
            else:
                pass
        else:
            pass
        index1+=1
    if factor1==0:
        return True
    else:
        return False

i=0
while(i<5):
     
     inputs=input(f'Enter name number{i+1}: ')
     print(f'{inputs} {has_hits(inputs)}')
     i+=1

# string=input('Enter the name: ')
# factor1=1
# index1=0
# for index0 in users:
#     if index0['name']== string:
#         condition1=users[index1]['items']
#         if len (condition1) >(0):
#             index2=0
#             for index3 in condition1:
#                 if 'reads' in index3:
#                     #print(index3)
#                     if index3['reads']>1000:
#                         x=0
#                         checkConditios=0
#                     else:
#                         x=1
#                     factor1*=x
#                 else:
#                     x=1
#                 index2+=1                    
#         else:
#             pass
#     else:
#         pass
#     index1+=1
# if factor1==0:
#     print('True')
# else:
#     print('False')

# #string=str(input('Enter the name: '))

#     #index2+=1
#     if index2==2:
#         break
# if factor1==0:
#     print('True')

# index0=0
# test2=input('Enter yor name: ')
# print(type(test2))
# for ii in users:
#     pointer=users[index0]
#     print(type(pointer["name"]))
#     if users[index0]['name'] == test2:
#         print(f"the name is {pointer['name']} item is {index0} ")
#     index0+=1


#     #index2+=1
#     if index2==2:
#         break
# if factor1==0:
#     print('True')

# index0=0
# test2=input('Enter yor name: ')
# print(type(test2))
# for ii in users:
#     pointer=users[index0]
#     print(type(pointer["name"]))
#     if users[index0]['name'] == test2:
#         print(f"the name is {pointer['name']} item is {index0} ")
#     index0+=1

# condition1=users[2]['items']
# range1=len(condition1)
# index3=0
# x2=1
# while index3<range1:
#     if condition1[index3]['reads'] > 1000:
#         x1=0
#         print(x1)
#     else:
#         x1=1
#         print(x1)
#     index3+=1
#     x2*=x1
# print(x2)


# def func1 (string):
#     index0=-1
# 

# condition1=users[2]['items']
# range1=len(condition1)
# index3=0
# x2=1
# while index3<range1:
#     if condition1[index3]['reads'] > 1000:
#         x1=0
#         print(x1)
#     else:
#         x1=1
#         print(x1)
#     index3+=1
#     x2*=x1
# print(x2)


# def func1 (string):
#     index0=-1
#     for index1 in users:
#         condition1=index1['items']
#         range1=len(condition1)
#         index3=0
#         factor1=1
#         while index3<range1:
#             if condition1[index3]['reads'] > 1000:
#                 condition2= 0
#                 #print(condition2)
#             else:
#                 condition2= 1
#                # print(condition2)
#             factor1*=condition2
#             print(factor1)
#             index3+=1
#         #print(users[2]['items'][0])
#         if (users[index0]['name']) == string and factor1==0 :
#             return True
#         else:
#             check = None
#             if check==None:
#                 return False      
# i=0
# while i<2:
#     name=str(input(f'Enter the name {i+1} please: '))
#     print(name,func1(name))
#     i+=1


# if check== True:
            #     return True
            # else:
            #     print('False')
           # print(f"the name is {string1} item is {index0} ")


# condition1=users[2]['items']
# range1=len(condition1)
# index3=0
# while index3<range1:
#     if condition1[index3]['reads'] > 1000:
#         condition2= True
#     else:
#         condition2= False
#     index3+=1

# def has_hits (string):
#     index0 = 0
#     for index1 in users:
#         pointer=users[index0]
#         if str(pointer['name']) == string:
#             print (f"the name is {string} and the index is {index0}" )
#     index0+=1
# test=str(input('Enter the name please: '))
# has_hits(test)

# for i in users:
#     name=i['name']
#     isReadExist=any('reads'in item for item in )

# def has_hits (string):
# print(users[2]['items'][0]['reads'])
# def has_hits (string):
#     for index in users:
#         name=i['name']
#         reads=i['items'][0][reads]
#         if reads > 1000:
#             return True
#         else:
#             return False

# string=input('Enter the name: ')
# factor1=1
# factor2=1
# index0=0
# for index1 in users[0]:
#     #print(users[index0]['name'])
#     if index1['name']== string:
#         condition1=users[index0]['items']
#         print(condition1)
#         print('yes')
#         #print(condition1)
#         if 'reads'in condition1:
#             print('yes2')
#             if condition1['reads']>1000:
#                 checkCondition = 0
#                 print(checkCondition)
#             else:
#                 checkCondition = 1
#                 print(checkCondition)
#             factor1*=checkCondition
#             print(factor1)
#         else:
#             print ('False')
#     index0+=1
# if factor1==0:
#     print('True')
    #print(condition1)
    #print (condition1)
    #range1=len(condition1)
    #print(range1)
    #         for loop1 in condition1:
    #             if loop1 > 1000:
    #                 print('True')
    #                 #print(value1)
    # else:
    #     print('False')     
    
# if factor2 ==0 and factor1 == 0 :
#     print ('True')
# else:
#     print ('False')

# if factor1 == 0:
#     print ('True')
# else:
#     print ('False')

        # else:
        #     check = None
        #     if check==None:
        #         return False      
# i=0
# while i<2:
#     name=str(input(f'Enter the name {i+1} please: '))
#     print(name,func1(name))
#     i+=1


# index3=0
    # factor1=1
    # while index3<range1:
    #     if condition1[index3]['reads'] > 1000:
    #         condition2= 0
    #         #print(condition2)
    #     else:
    #         condition2= 1
    #         #print(condition2)
    #     factor1*=condition2
    #     #print(factor1)
    #     index3+=1
        #print(users[2]['items'][0])

#         string=input('Enter the name: ')
# factor1=1
# factor2=1
# index0=0
# for index1 in users:
#     #print(users[index0]['name'])
#     condition1=index1['items']
#     #print(condition1)
#     #print (condition1)
#     range1=len(condition1)
#     #print(range1)
#     for loop1 in condition1:
#         if 'reads'in loop1:
#             value1=loop1['reads']
#             print(value1)
#             if value1 > 1000:
#                 checkCondition = 0
#                 #print('True')
#             else:
#                 checkCondition = 1
#                 #print('False')
#         factor1*=checkCondition
#         #print(factor1)
#                 #print(loop1['reads'])
    
#         if (users[index0]['name']) == string:
#             checkCondition2 = 0
#             #print('True')
#         else:
#             checkCondition2=1
#             #print('False')
#         factor2*=checkCondition2