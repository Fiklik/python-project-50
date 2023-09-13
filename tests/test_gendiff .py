import pytest
from gendiff.formatters.format import format_diff
from gendiff.scripts.diff import get_difference_between_files


# @pytest.mark.usefixtures
# @pytest.mark.parametrize(
#     "diff, format, example_text",
#     [
#         #(get_difference_between_files(file1, file2), 'stylish',flat_text),
#         (diff, 'stylish', stylish_text),
#         (diff, 'plain', plain_text)
#         #(get_difference_between_files(file1, file2), 'json', json_text)
#     ]
# )
@pytest.mark.usefixtures
def test_flat_diff(flat_diff, flat_text):
    assert format_diff(flat_diff) == flat_text


@pytest.mark.usefixtures
def test_stylish_diff(nested_diff, stylish_text):
    assert format_diff(nested_diff) == stylish_text


@pytest.mark.usefixtures
def test_plain_diff(nested_diff, plain_text):
    assert format_diff(nested_diff, format='plain') == plain_text


@pytest.mark.usefixtures
def test_json_diff(nested_diff, json_text):
    assert format_diff(nested_diff, format='json') == json_text