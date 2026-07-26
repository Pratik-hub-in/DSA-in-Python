"""
Program: Character Frequency

Description:
This program counts the frequency of each character in a string.

Two approaches are demonstrated:

Method 1:
- Using a dictionary.

Method 2:
- Using Python's collections.Counter class.

The program ignores letter casing by converting the input string
to lowercase.

Example:
Input:
String = "Programming"

Output:
p : 1
r : 2
o : 1
g : 2
a : 1
m : 2
i : 1
n : 1

Time Complexity:
- Dictionary Method: O(n)
- Counter Method: O(n)

Space Complexity:
- O(n)
"""

from collections import Counter


def frequency_using_dictionary(text: str) -> dict:
    """
    Counts character frequencies using a dictionary.

    Args:
        text (str): Input string.

    Returns:
        dict: Character frequency dictionary.
    """
    frequency = {}

    for character in text.lower():
        frequency[character] = frequency.get(character, 0) + 1

    return frequency


def frequency_using_counter(text: str) -> Counter:
    """
    Counts character frequencies using Counter.

    Args:
        text (str): Input string.

    Returns:
        Counter: Character frequency counter.
    """
    return Counter(text.lower())


def display_frequency(data):
    """
    Displays character frequencies in a readable format.

    Args:
        data (dict): Character frequency data.
    """
    for character, count in sorted(data.items()):
        print(f"{character} : {count}")


if __name__ == "__main__":
    text = "Programming"

    print("Original String:", text)

    print("\nMethod 1: Using Dictionary")
    dictionary_result = frequency_using_dictionary(text)
    display_frequency(dictionary_result)

    print("\nMethod 2: Using Counter")
    counter_result = frequency_using_counter(text)
    display_frequency(counter_result)


# Key Takeaways:
# • Dictionaries provide fast lookups and updates.
# • Counter is a built-in class designed for counting elements.
# • Character frequency problems are common in coding interviews.
