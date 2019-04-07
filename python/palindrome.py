# Returns if a string is a palindrome

def palindrome(s):
	n = len(s)
	i = 0
	while i <= n/2  and s[i] == s[n-1-i]:
		i += 1
	if i > n/2:
		return True
	else:
		return False

# Simple tests

print(palindrome("a"))
print(palindrome("aa"))
print(palindrome("aba"))
print(palindrome("abccba"))
print(palindrome("abcdcba"))

print(palindrome("ab"))
print(palindrome("abb"))
print(palindrome("abcdba"))
print(palindrome("abcdecba"))



