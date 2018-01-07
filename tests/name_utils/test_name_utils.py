import pytest

import contacts.contacts
import name_utils.name_utils

DICT1 = {"0500000000": "Gabriel Shalom", "0501111111": "James Bond", "0502222222": "Jimmy Kimble"}

NAME_BIRTHDAY_DICT1 = {"Gabriel Shalom": "1/1/1990", "Gab Shal": "2/2/1990", "James Bond": "1/1/1991",
                       "Jimmy Kimble": "2/2/1991"}

NAME_BIRTHDAY_DICT2 = {"Gabriel Shalom": "1/1/1990", "Gab Shal": "2/2/1990", "James Bond": "1/1/1991",
                       "Jimmy Kimble": "1/1/1992"}

NAME_BIRTHDAY_DICT3 = {"Gabriel Shalom": "1/1/1990", "James Bond": "1/1/1991",
                       "Jimmy Kimble": "1/1/1992"}

CONTACT_DICT1 = {"0500000000": "Gabriel Shalom", "0501111111": "James bond", "0502222222": "Jimmy Kimle"}

CONTACT_DICT2 = {"0500000000": "Gabriel Shalom", "0511111111": "James Bon", "0501111111": "James Bond",
                 "0512222222": "Jimmy Kimle", "0502222222": "Jimmy Kimble"}

CONTACT_DICT3 = {"0500000000": "Gabr Shal", "0501111111": "Ja B", "0511111111": "James bond",
                 "0502222222": "Jimmy K", "0512222222": "jimmy kimble"}

OUTPUT_DICT1 = {"0500000000": ("Gabriel Shalom", "Gabriel Shalom", "1/1/1990"),
                "0501111111": ("James bond", "James Bond", "1/1/1991"),
                "0502222222": ("Jimmy Kimle", "Jimmy Kimble", "2/2/1991")}

OUTPUT_DICT2 = {"0500000000": ("Gabriel Shalom", "Gabriel Shalom", "1/1/1990"),
                "0501111111": ("James Bond", "James Bond", "1/1/1991"),
                "0502222222": ("Jimmy Kimble", "Jimmy Kimble", "1/1/1992")}

OUTPUT_DICT3 = {"0500000000": ("Gabr Shal", "Gabriel Shalom", "1/1/1990"),
                "0501111111": ("Ja B", "James Bond", "1/1/1991"),
                "0502222222": ("Jimmy K", "Jimmy Kimble", "1/1/1992")}


@pytest.mark.parametrize("name1,name2,output",
                         [("a", "ab", False),
                          ("ab", "a", False),
                          ("abc", "ab", False),
                          ("wow", None, False),
                          (None, "None", False),
                          ("have you ever seen", "e", False),
                          ("a", "a a", True)])
def test_is_contained_name_sanity(name1, name2, output):
    assert name_utils.name_utils.is_contained_name(name1, name2) is output


@pytest.mark.parametrize("name_birthday_dict,contact_dict,output",
                         [(NAME_BIRTHDAY_DICT1, CONTACT_DICT1, OUTPUT_DICT1),
                          ({}, {}, {})])
def test_add_birthday_to_contacts_sanity(name_birthday_dict, contact_dict, output):
    assert contacts.contacts.add_birthday_to_contacts(name_birthday_dict, contact_dict) == output


@pytest.mark.parametrize("name_birthday_dict,contact_dict,output",
                         [(NAME_BIRTHDAY_DICT2, CONTACT_DICT2, OUTPUT_DICT2)])
def test_add_birthday_to_contacts_check_equal_before_all(name_birthday_dict, contact_dict, output):
    assert contacts.contacts.add_birthday_to_contacts(name_birthday_dict, contact_dict) == output


@pytest.mark.parametrize("name_birthday_dict,contact_dict,output",
                         [(NAME_BIRTHDAY_DICT3, CONTACT_DICT3, OUTPUT_DICT3)])
def test_add_birthday_to_contacts_check_contains_before_distance(name_birthday_dict, contact_dict, output):
    assert contacts.contacts.add_birthday_to_contacts(name_birthday_dict, contact_dict) == output
