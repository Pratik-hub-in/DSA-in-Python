"""
Program: String Compression

Description:
This program compresses a string using the Run-Length Encoding (RLE)
technique.

Run-Length Encoding replaces consecutive repeated characters
with the character followed by its count.

Example:
Input:
"aaabbccccdaa"

Output:
"a3b2c4d1a2"

If the compressed string is not shorter than the original,
the original string is returned.

Time Complexity:
- O(n)

Space Complexity:
- O(n)

Learning Outcomes:
- Learn the Run-Length Encoding technique.
- Understand efficient string construction.
- Practice character traversal.
"""


def compress_string(text: str) -> str:
    """
    Compresses a string using Run-Length Encoding.

    Args:
        text (str): Input string.

    Returns:
        str: Compressed string if shorter,
             otherwise the original string.
    """
    if not text:
        return ""

    compressed = []
    count = 1

    for index in range(1, len(text)):
        if text[index] == text[index - 1]:
            count += 1
        else:
            compressed.append(text[index - 1])
            compressed.append(str(count))
            count = 1

    compressed.append(text[-1])
    compressed.append(str(count))

    compressed_text = "".join(compressed)

    if len(compressed_text) < len(text):
        return compressed_text

    return text


if __name__ == "__main__":
    text = "aaabbccccdaa"

    print("Original String:")
    print(text)

    compressed = compress_string(text)

    print("\nCompressed String:")
    print(compressed)


# Key Takeaways:
# • Run-Length Encoding (RLE) compresses consecutive repeated characters.
# • Lists are more efficient than repeated string concatenation.
# • Return the original string if compression does not reduce its length.
# • String compression is a common interview question.
