#WAF to find in which line of the file does the word "learning".
def check_line():
    word="learning"
    data=True
    line=1
    with open("practice.txt","r") as f:
     while data:
      data=f.readline()
      if(word in data):
        print(line)
        return
    line+=1
check_line()
    
