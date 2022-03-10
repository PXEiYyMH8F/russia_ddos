import pytest as pytest

import ripper


# @pytest.mark.parametrize('actual_ip, expected_result', [
#     ('127.0.0.1', '127.*.*.*'),
#     ('42.199.100.200', '42.*.*.*'),
#     ('42', '42')
# ])
# def test_get_first_ip_part(actual_ip, expected_result):
#     assert get_first_ip_part(actual_ip) == expected_result


@pytest.mark.parametrize('actual, expected', [
    (0, '0 B'),
    (100, '100.0 B'),
    (1024, '1.0 KB'),
    (16384096, '15.63 MB'),
    (32256798429, '30.04 GB'),
    (620832256798429, '564.64 TB'),
])
def test_convert_size(actual, expected):
    assert ripper.common.convert_size(actual) == expected
