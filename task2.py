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


def author_average_reads (string):
    average=0
    factor1=1
    index1=0
    for index0 in users:
        if index0['name']== string:
            condition1=users[index1]['items']
            if len (condition1) >(0):
                index2=0
                for index3 in condition1:
                    if 'reads' in index3:
                        average+=index3['reads']
                        if index3['reads']>1000:
                            x=0
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
        return average/len(condition1)
    else:
        return 0

i=0
while(i<5):
     
     inputs=input(f'Enter name number{i+1}: ')
     print(f'{inputs} {author_average_reads(inputs)}')
     i+=1