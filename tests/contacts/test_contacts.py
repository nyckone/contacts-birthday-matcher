import pytest

import contacts.contacts

NAME_BIRTHDAY_DICT1 = {"Gabriel Shalom": "1/1/1990", "Gab Shal": "2/2/1990", "James bond": "1/1/1991",
                       "Jimmy Kimble": "2/2/1991", }

CONTACT_DICT1 = {"0500000000": "Gabriel Shalom", "0501111111": "James Bond", "0502222222": "Jimmy Kimle"}

OUTPUT_DICT1 = {"0500000000": ("Gabriel Shalom", "1/1/1990"), "0501111111": ("James Bond", "1/1/1991"), "0502222222":
                ("Jimmy Kimble", "2/2/1991")}


@pytest.mark.parametrize("name_birthday_dict,contact_dict,output",
                         [(NAME_BIRTHDAY_DICT1, CONTACT_DICT1, OUTPUT_DICT1),
                          ("a", "a a", True)])
def test_add_birthday_to_contacts_sanity(name_birthday_dict, contact_dict, output):
    assert contacts.contacts.add_birthday_to_contacts(name_birthday_dict, contact_dict) == output
