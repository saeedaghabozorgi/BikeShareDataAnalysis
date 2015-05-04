

offer <- function(o){
  #o is added to list if o is bigger than the lowest number in the result list
  i<-length(x[x>o])  # index of the larger value than o,  O(k)
  x<-append(x,o,after=i)  #O(1): insert into the list
  x<-x[1:k]  # to truncate it
  y<-x[!is.na(x)]
  return (y)
}

getTopK<-function()
{
  return (x)
}

app<-function(n)
{
  k<<-n
}

################ test

x=c() 
k=0
app(3)

getTopK()
x<-offer('a')
getTopK()
x<-offer('b')
getTopK()
x<-offer('aa')
getTopK()
x<-offer('c')
getTopK()
x<-offer('a')
getTopK()
x<-offer('d')
getTopK()








