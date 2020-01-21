word = input("Enter word :")
word=word.split(',')
word=sorted(word)
ans=''

for x in word:
    if x != word[len(word)-1]:
        ans=ans+x+','
    else:
        ans=ans+x
print(ans)
