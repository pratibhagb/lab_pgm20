def is_palindrome(s):
    # Normalize string: remove spaces and convert to lowercase
    cleaned_s = "".join(s.split()).lower()
    return cleaned_s == cleaned_s[::-1]


if __name__ == "__main__":
    test_strings = ["madam", "racecar", "hello", "A man a plan a canal Panama"]

    print("--- Palindrome Checker ---")
    for test_str in test_strings:
        if is_palindrome(test_str):
            print(f"'{test_str}' is a Palindrome.")
        else:
            print(f"'{test_str}' is NOT a Palindrome.")