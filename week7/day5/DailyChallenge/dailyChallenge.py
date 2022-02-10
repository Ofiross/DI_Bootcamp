# Daily Challenge: Sorting
while True:
    list_to_order = input(
        'Plese inseert a list of words comma-separated: ').lower()
    if ',' not in list_to_order:
        continue
    break

words = [word for word in list_to_order.split(', ')]
words.sort()

result = ', '.join([str(item) for item in words])
print('The input in an alphbetical order is:')
print(result)
