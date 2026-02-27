import CSP_6_02_reading_files as HW

def test_longest_line():
    assert HW.longestLine("CSP_6_02_text_file.txt") == "Nate sits across from me\n"


def test_to_binary():
    assert HW.toBinary("CSP_6_02_binary_file.txt") == ['10101011', '10001011', '01010111', '00']
