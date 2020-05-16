from log_file_processor import LogFileProcessor
from pprint import pprint

process = LogFileProcessor()

print('---------------------------------------------------------------------')
print('------------------------  QUAKE LOG PARSER  -------------------------')
print('---------------------------------------------------------------------')
response = process.start()

for key in response.keys():
    print('\n\n\n')
    print('---------------------------------------------------------------------')
    print(f'------------------------\t{key.upper().replace("_", " ")}      ------------------------')
    print('---------------------------------------------------------------------')
    print('---------------------------------------------------------------------')
    dic = response[key]['kills']
    rancking = []
    count = 0
    for item in sorted(dic, key = dic.get):
        rancking.append(item)
    print(f'------------------------\tRANKING      ------------------------')
    print('---------------------------------------------------------------------')
    print(f"----|\tPOS\t\t{'PLAYER' + (20 - len('PLAYER')) * ' '}\t\tKILLS\t|----")
    print('---------------------------------------------------------------------')
    for i in range(len(rancking)):
        name = rancking.pop()
        count += 1
        print(f"----|\t{count}º\t\t{name + (20 - len(name)) * ' '}\t\t{response[key]['kills'][name]}\t|----")
    print('---------------------------------------------------------------------')
    pprint(response[key])
    print('---------------------------------------------------------------------')

print('---------------------------------------------------------------------')
