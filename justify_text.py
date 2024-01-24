def justify_paragraph(paragraph, page_width):
    words = paragraph.split()
    result = []
    current_line = []

    for word in words:
        if len(' '.join(current_line + [word])) <= page_width:
            current_line.append(word)
        else:
            result.append(current_line)
            current_line = [word]

    # Handling the last line
    if current_line:
        result.append(current_line)

    justified_lines = []

    for line in result:
        num_words = len(line)
        total_spaces = page_width - sum(len(word) for word in line)
        
        if num_words == 1:
            justified_lines.append(line[0].ljust(page_width))
        else:
            space_between_words = total_spaces // (num_words - 1)
            extra_spaces = total_spaces % (num_words - 1)
            
            justified_line = line[0]
            for i in range(1, num_words):
                justified_line += ' ' * (space_between_words + (1 if i <= extra_spaces else 0)) + line[i]
            
            justified_lines.append(justified_line)

    return justified_lines

# Sample input values
# paragraph = "This is a sample text but a complicated problem to be solved, so we are adding more text to see that it actually works."
# page_width = 20

# Getting justified lines
justified_lines = justify_paragraph(paragraph, page_width)

# Printing the result
for line in justified_lines:
    print(f"Array = \"{line}\"")
