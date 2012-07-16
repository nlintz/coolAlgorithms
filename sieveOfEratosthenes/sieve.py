def sieve(n):
   l = range(n+1)
   l.remove(0)
   p=2
   while p<n:
       defineRemovers(n,p,l)
       p+=1
   return l

def defineRemovers(n,p,l):
    i=2
    while (i*p)<=n:
        if(i*p in l):
            l.remove(i*p)
        i+=1
    
    return l

