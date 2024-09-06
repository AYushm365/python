def longest_palindromic_substring(s: str) -> str:
    def expand_from_center(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Check for odd length palindromes
        odd_palindrome = expand_from_center(i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome
        # Check for even length palindromes
        even_palindrome = expand_from_center(i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

    return longest

# Example usage
print(longest_palindromic_substring("babad"))  # Output: "bab" or "aba"
