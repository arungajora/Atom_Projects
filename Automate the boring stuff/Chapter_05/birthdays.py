birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12.', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' it is the birthday of ' + name)
    else:
        print('I do not have a birthday information for ' + name)
        print ('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print ('birthday database updated.')