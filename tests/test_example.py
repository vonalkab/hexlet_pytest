from hexlet_pytest.example import reverse
from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse():
    text_for_tests = read_file("text_for_tests.txt")
    expected = read_file("result_for_text.txt")
    assert reverse(text_for_tests) == expected


def test_reverse_for_empty_string():
    assert reverse("") == ""
