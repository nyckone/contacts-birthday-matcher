import pytest

import contact_utils.contact_utils

DICT1 = {"0500000000": "Gabriel Shalom", "0501111111": "James Bond", "0502222222": "Jimmy Kimble"}


@pytest.mark.parametrize("contact_dict,exact_name,output",
                         [(DICT1, "Gab Sha", ("0500000000", "Gabriel Shalom")),
                          (DICT1, "Ja ond", ("0501111111", "James Bond")),
                          (DICT1, "Jam", None),
                          (DICT1, "Jimmy ond", None),
                          (DICT1, "Gab ond", None)])
def test_find_contained_contact_sanity(contact_dict, exact_name, output):
    assert contact_utils.contact_utils.find_contained_contact(contact_dict, exact_name) == output


@pytest.mark.parametrize("contact_dict,exact_name,output",
                         [(DICT1, "Jam a", ("0501111111", "James Bond")),
                          (DICT1, "Gab ab", ("0500000000", "Gabriel Shalom")),
                          (DICT1, "Sha ab", ("0500000000", "Gabriel Shalom")),
                          (DICT1, "Sha Jim", None)])
def test_find_contained_contact_names_contained_inside_weird_combination(contact_dict, exact_name, output):
    assert contact_utils.contact_utils.find_contained_contact(contact_dict, exact_name) == output


@pytest.mark.parametrize("contact_dict,exact_name,output",
                         [(DICT1, "jam a", None),
                          (DICT1, "gab ab", None),
                          (DICT1, "sha ab", None),
                          (DICT1, "sha jim", None)])
def test_find_contained_contact_names_contained_lower_case_different(contact_dict, exact_name, output):
    assert contact_utils.contact_utils.find_contained_contact(contact_dict, exact_name) == output


@pytest.mark.parametrize("contact_dict,name,output",
                         [(DICT1, "Gabriel Shalom", ("0500000000", "Gabriel Shalom")),
                          (DICT1, "James Bond", ("0501111111", "James Bond")),
                          (DICT1, "James Bon", None),
                          (DICT1, "James Bondi", None),
                          (DICT1, "aJames Bond", None),
                          (DICT1, "Jimmy kimble", None),
                          (DICT1, "Gab ond", None)])
def test_find_exact_contact_sanity(contact_dict, name, output):
    assert contact_utils.contact_utils.find_exact_contact(contact_dict, name) == output


@pytest.mark.parametrize("contact_dict,name,distance,output",
                         [(DICT1, "Gabriel Shalom", 0, ("0500000000", "Gabriel Shalom")),
                          (DICT1, "James Bond", 0, ("0501111111", "James Bond")),
                          (DICT1, "James Bon", 0, None),
                          (DICT1, "James Bondi", 1, ("0501111111", "James Bond")),
                          (DICT1, "Gabriel Shalo", 1, ("0500000000", "Gabriel Shalom")),
                          (DICT1, "aJames Bonda", 1, None),
                          (DICT1, "James Bondi", 2, ("0501111111", "James Bond")),
                          (DICT1, "aJames Bondi", 2, ("0501111111", "James Bond")),
                          (DICT1, "fabriel Shalo", 2, ("0500000000", "Gabriel Shalom")),
                          (DICT1, "jimmyy kimble", 2, None),
                          (DICT1, "James Bondi", 3, ("0501111111", "James Bond")),
                          (DICT1, "aJames bondi", 3, ("0501111111", "James Bond")),
                          (DICT1, "fabriel 0Shalo", 3, ("0500000000", "Gabriel Shalom")),
                          (DICT1, "Gab ond", 3, None)])
def test_find_distanced_contact_sanity(contact_dict, name, distance, output):
    assert contact_utils.contact_utils.find_distanced_contact(contact_dict, name, distance) == output
