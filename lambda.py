'''
def sorter(item):
    return item['name']
'''

#using Lambda functions
presenters = [
    {'name': 'Susan', 'age': '50'},
    {'name': 'Ahmed Adel', 'age': '12'}
]

presenters.sort(key = lambda item: item['name'])
print(presenters)

presenters.sort(key = lambda item: len(item['name']))