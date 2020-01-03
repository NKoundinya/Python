def p(n,k):
 if n<k:
 # print "1 = "
  return 1
 else:
  print n,"*"
  x=n*p(n-1,k)
 return x
def show(n,k):
 if n<k:
  print "Not possible"
 else:
  if n==k:
   print n,"!"
  else:
   print n,"P",k
def createword(word2):
 word2=word2.lower()
 word=""
 for i in range(0,len(word2)):
   if word2[i] in word:
    continue
   else:
    word+=word2[i]
 return word
def createnew(word,word2,k):
 new=[]
 for i in range(0,len(word)):
  for j in range(0,len(word2)):
   if word[i]==word2[j]:
    k=k+1
   else:
    continue
  new.append(k)
  k=0
 return new
def per(new,n,word2,word):
 print word2," in ",n," places is "
 show(len(word2),n)
 x=p(len(word2),len(word2)-n+1)
 for i in range(0,len(word)):
  if new[i]>1:
   print " * 1/",new[i],"!"
   x=x/p(new[i],1)
 print "="
 return x
#def together():
    
def main():
 word2=raw_input("Enter your word: ")
 word=createword(word2)
 new=createnew(word,word2,0)
 print "Your Permutation for ",per(new,input("Spaces: "),word2,word)
main()
