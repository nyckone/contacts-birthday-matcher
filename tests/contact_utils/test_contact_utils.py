import pytest

import contact_utils.contact_utils

CONTACT_DICT = {"0500000000": "Gabriel Shalom", "0501111111": "James Bond", "0502222222": "Jimmy Kimble"}


@pytest.mark.parametrize("contact_dict,exact_name,output",
                         [(CONTACT_DICT, "Gab Sha", ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "Ja ond", ("0501111111", "James Bond")),
                          (CONTACT_DICT, "Jam", None),
                          (CONTACT_DICT, "Jimmy ond", None),
                          (CONTACT_DICT, "Gab ond", None)])
def test_find_contained_contact_sanity(contact_dict, exact_name, output):
    assert contact_utils.contact_utils.find_contained_contact(contact_dict, exact_name) == output


@pytest.mark.parametrize("contact_dict,exact_name,output",
                         [(CONTACT_DICT, "Jam a", ("0501111111", "James Bond")),
                          (CONTACT_DICT, "Gab ab", ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "Sha ab", ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "Sha Jim", None)])
def test_find_contained_contact_names_contained_inside_weird_combination(contact_dict, exact_name, output):
    assert contact_utils.contact_utils.find_contained_contact(contact_dict, exact_name) == output


@pytest.mark.parametrize("contact_dict,exact_name,output",
                         [(CONTACT_DICT, "jam a", None),
                          (CONTACT_DICT, "gab ab", None),
                          (CONTACT_DICT, "sha ab", None),
                          (CONTACT_DICT, "sha jim", None)])
def test_find_contained_contact_names_contained_lower_case_different(contact_dict, exact_name, output):
    assert contact_utils.contact_utils.find_contained_contact(contact_dict, exact_name) == output


@pytest.mark.parametrize("contact_dict,name,output",
                         [(CONTACT_DICT, "Gabriel Shalom", ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "James Bond", ("0501111111", "James Bond")),
                          (CONTACT_DICT, "James Bon", None),
                          (CONTACT_DICT, "James Bondi", None),
                          (CONTACT_DICT, "aJames Bond", None),
                          (CONTACT_DICT, "Jimmy kimble", None),
                          (CONTACT_DICT, "Gab ond", None)])
def test_find_exact_contact_sanity(contact_dict, name, output):
    assert contact_utils.contact_utils.find_exact_contact(contact_dict, name) == output


@pytest.mark.parametrize("contact_dict,name,distance,output",
                         [(CONTACT_DICT, "Gabriel Shalom", 0, ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "James Bond", 0, ("0501111111", "James Bond")),
                          (CONTACT_DICT, "James Bon", 0, None),
                          (CONTACT_DICT, "James Bondi", 1, ("0501111111", "James Bond")),
                          (CONTACT_DICT, "Gabriel Shalo", 1, ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "aJames Bonda", 1, None),
                          (CONTACT_DICT, "James Bondi", 2, ("0501111111", "James Bond")),
                          (CONTACT_DICT, "aJames Bondi", 2, ("0501111111", "James Bond")),
                          (CONTACT_DICT, "fabriel Shalo", 2, ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "jimmyy kimble", 2, None),
                          (CONTACT_DICT, "James Bondi", 3, ("0501111111", "James Bond")),
                          (CONTACT_DICT, "aJames bondi", 3, ("0501111111", "James Bond")),
                          (CONTACT_DICT, "fabriel 0Shalo", 3, ("0500000000", "Gabriel Shalom")),
                          (CONTACT_DICT, "Gab ond", 3, None)])
def test_find_distanced_contact_sanity(contact_dict, name, distance, output):
    assert contact_utils.contact_utils.find_distanced_contact(contact_dict, name, distance) == output
