import pytest

import name_utils.name_utils

DICT1 = {"0500000000": "Gabriel Shalom", "0501111111": "James Bond", "0502222222": "Jimmy Kimble"}


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
