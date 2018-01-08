# contacts-birthday_matcher
Input is a json containing dicts of contacts and birthday separated when the key to the contact_dict is "contact_dict"
 and the key to the birthday_dict is "birthday_dict".
 The output is a contact dict with birthdays added

The input json should be Posted to the uploaded url with /get_contacts_with_birthday in order for the outcome to receive

contact_dict is a dict from phone to name, meaning:
contact_phone -> contact_name

birthday_dict is a dict as well of the form:
contact_name -> contact_birthday

and the main function returns a dict containing a tuple from the form:
contact_phone->(contact_name, exact_name, contact_birthday)

the exact_name is the name as it appears in the birthday dict - our assumption that those are accurate names.

so the main function signature looks like this:
([contact_phone->contact_name], [contact_name->contact_birthday]) ->
[contact_phone->(contact_name, exact_name, contact_birthday)]