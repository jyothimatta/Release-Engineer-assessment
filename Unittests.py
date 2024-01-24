def run_tests():
    # Test 1
    paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
    page_width = 20
    justified_lines = justify_paragraph(paragraph, page_width)
    expected_output = [
        "This   is  a  sample",
        "text      but      a",
        "complicated  problem",
        "to  be solved, so we",
        "are adding more text",
        "to   see   that   it",
        "actually      works."
    ]
    assert justified_lines == expected_output
    print("Test 1 Passed\n")

    # Test 2
    paragraph = "  Leading and trailing spaces  "
    page_width = 30
    justified_lines = justify_paragraph(paragraph, page_width)
    expected_output = [
        "Leading and trailing spaces"
    ]
    assert justified_lines == expected_output
    print("Test 2 Passed\n")

    # Test 3
    paragraph = "Short text."
    page_width = 15
    justified_lines = justify_paragraph(paragraph, page_width)
    expected_output = [
        "Short text."
    ]
    assert justified_lines == expected_output
    print("Test 3 Passed\n")

    # Test 4
    paragraph = "This"
    page_width = 5
    justified_lines = justify_paragraph(paragraph, page_width)
    expected_output = [
        "This"
    ]
    assert justified_lines == expected_output
    print("Test 4 Passed\n")

    # Test 5
    paragraph = "  Multiple   spaces   between   words.  "
    page_width = 15
    justified_lines = justify_paragraph(paragraph, page_width)
    expected_output = [
        "Multiple   spaces",
        "between   words."
    ]
    assert justified_lines == expected_output
    print("Test 5 Passed\n")
    # Test 6
    paragraph = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    page_width = 10
    justified_lines = justify_paragraph(paragraph, page_width)
    expected_output = [
        "A B C D E",
        "F G H I J",
        "K L M N O",
        "P Q R S T",
        "U V W X Y",
        "Z"
    ]
    assert justified_lines == expected_output
    print("Test 6 Passed\n")

# Run the tests
run_tests()
