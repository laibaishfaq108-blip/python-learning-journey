sentence="python is easy and python is fun."
word=sentence.split()
freq={}
for w in word:
    if w in freq:
      freq[w]+=1
    else:  
       freq[w]=1
print(freq)       