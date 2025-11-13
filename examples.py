"""
Example usage of the string_randomizer package.
"""

from string_randomizer import randomize_string, randomize_words


def main():
    """Demonstrate string randomization functionality."""

    print("String Randomizer - Example Usage")
    print("=" * 50)

    # Example 1: Basic string randomization
    print("\n1. Basic string randomization:")
    text1 = "hello world"
    result1 = randomize_string(text1)
    print(f"   Original: '{text1}'")
    print(f"   Randomized: '{result1}'")

    # Example 2: Randomize with seed for reproducibility
    print("\n2. Randomize with seed (reproducible):")
    text2 = "python package"
    result2a = randomize_string(text2, seed=42)
    result2b = randomize_string(text2, seed=42)
    print(f"   Original: '{text2}'")
    print(f"   Result 1: '{result2a}'")
    print(f"   Result 2: '{result2b}'")
    print(f"   Same? {result2a == result2b}")

    # Example 3: Randomize words (preserve word boundaries)
    print("\n3. Randomize letters within words:")
    text3 = "the quick brown fox"
    result3 = randomize_words(text3)
    print(f"   Original: '{text3}'")
    print(f"   Randomized: '{result3}'")

    # Example 4: Multiple randomizations show variability
    print("\n4. Multiple randomizations of same input:")
    text4 = "example"
    print(f"   Original: '{text4}'")
    for i in range(5):
        result4 = randomize_string(text4)
        print(f"   Attempt {i+1}: '{result4}'")

    # Example 5: Works with different types of characters
    print("\n5. Works with numbers and special characters:")
    text5 = "abc123!@#"
    result5 = randomize_string(text5)
    print(f"   Original: '{text5}'")
    print(f"   Randomized: '{result5}'")

    print("\n" + "=" * 50)
    print("Examples completed!")


if __name__ == "__main__":
    main()
