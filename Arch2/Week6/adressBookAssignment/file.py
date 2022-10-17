import os
import sys
import json

addressbook = []


def display(list=addressbook):
    for contact in addressbook:
        emails = ''
        numbers = ''
        for email in contact['emails']:
            if email != contact['emails'][-1]:
                emails += email + ', '
            else:
                emails += email
        for numb in contact['phone_numbers']:
            if numb != contact['phone_numbers'][-1]:
                numbers += numb + ', '
            else:
                numbers += numb
        print(f'''
Position: {contact['id']}
First name: {contact['first_name']}
Last name: {contact['last_name']}
Emails: {emails}
Phone numbers: {numbers}
        ''')


def list_contacts():
    addressbook.sort(key=lambda x: x['last_name'])
    return addressbook


def add_contact():
    questions = ('first_name', 'last_name', 'emails', 'phone_numbers')
    contact = {}
    contact['id'] = len(addressbook) + 1
    for question in questions:
        inp = input(question)
        if question == 'emails' or question == 'phone_numbers':
            contact[question] = list([inp])
        else:
            contact[question] = inp
    addressbook.append(contact)


def remove_contact():
    inp = input('contacts id')
    for contact in addressbook:
        if inp == str(contact['id']):
            addressbook.remove(contact)
    return


def merge_contacts():
    for cont in addressbook:
        multiple = 0
        for conts in addressbook:
            if ((conts['first_name'],
                 conts['last_name']) == (cont['first_name'],
                                         cont['last_name'])):
                multiple += 1
            if multiple > 1:
                for emails in conts['emails']:
                    if emails not in cont['emails']:
                        cont['emails'].append(emails)
                for numbers in conts['phone_numbers']:
                    if numbers not in cont['phone_numbers']:
                        cont['phone_numbers'].append(numbers)
                addressbook.remove(conts)


def read_from_json(filename):
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in data:
            addressbook.append(contact)


def write_to_json(filename):
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def select_menu():
    exit = False
    menu = [
        {
            'L': list_contacts,
            'A': add_contact,
            'R': remove_contact,
            'M': merge_contacts,
        }
    ]
    while exit is False:
        inp = input('''
[L] List contacts
[A] Add contact
[R] Remove contact
[M] Merge contacts
[Q] Quit program''').upper()
        if inp in menu[0].keys():
            menu[0][inp]()
        elif inp == 'Q':
            exit = True
            return
        else:
            exit = True
            return print('invalid')
        write_to_json('contacts.json')


def main(json_file):
    read_from_json(json_file)
    select_menu()
    display()


if __name__ == "__main__":
    main('contacts.json')
