text = "Python is awesome"
vowels = "aeiouAEIOU"
count = sum(1 for char in text if char in vowels)
print(f"모음 개수: {count}")