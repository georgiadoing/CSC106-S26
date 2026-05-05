# Replace this comment with an appropriate header.

# Replace this comment with your function definitions.
    

### DO NOT DELETE THIS LINE: beg testing

# Testing encipher
original = "ABC"
shift = 3
expected = "DEF"
print("Shifting '" + original + "' by", shift, "yields '" + encipher(original, shift) + "'")
print("expected:", expected)

original = "xyza"
shift = 1
expected = "yzab"
print("Shifting '" + original + "' by", shift, "yields '" + encipher(original, shift) + "'")
print("expected:", expected)

original = "Z A"
shift = 2
expected = "B C"
print("Shifting '" + original + "' by", shift, "yields '" + encipher(original, shift) + "'")
print("expected:", expected)

original = "Caesar cipher? I prefer Caesar salad."
shift = 25
expected = "Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc."
print("Shifting '" + original + "' by", shift, "yields '" + encipher(original, shift) + "'")
print("expected:", expected)


# Testing decipher -- You might want to add more tests.
# encoded = "Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc."
# shift = 25
# expected = "Caesar cipher? I prefer Caesar salad."
# print("Shifting '" + encoded + "' back by", shift, "yields '" + decipher(encoded, shift) + "'")
# print("expected:", expected)