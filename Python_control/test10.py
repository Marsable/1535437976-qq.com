my_text = "wo ai xiaohuangya"
# char_count = {c:my_text.count(c) for c in my_text}
# print(char_count)
char_count={}
for c in my_text:
    char_count[c] = my_text.count(c)
print(char_count)