def double_word(word):
    new = word * 2
    return  new + str(len(new))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0