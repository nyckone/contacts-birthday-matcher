# facebook-contacts-birthday
Get contacts list and birthday list - returns a contact list with birthday added

contact_dict is a dict from phone to name, meaning:
contact_phone -> contact_name

birthday_dict is a dict as well of the form:
contact_name -> contact_birthday

and the main function returns a dict containing a tuple from the form:
contact_phone->(contact_name, contact_birthday)

so the main function signature looks like this:
([contact_phone->contact_name], [contact_name->contact_birthday]) -> [contact_phone->(contact_name, contact_birthday)]
