from core import fp_python as fp
data=[1,2,3]
fpobj = fp.Fp(data)
# maps
print(fpobj.maps(lambda x:x+1).data == [2,3,4])
#filters
print(fpobj.filters(lambda x:x%2==0).data==[2])
#filterNot
print(fpobj.filterNot(lambda x:x%2==0).data==[1,3])
#flatten
print(fpobj.maps(lambda x:list(range(0,x))).flatten().data==[0, 0, 1, 0, 1, 2])
#reduces
print(fpobj.reduces(lambda x,y:x+y).data==6)
#fold
print(fpobj.fold(1,lambda x,y:x+y).data == 7)
#foreach
fpobj.foreach(print)
#flatMap
print(fpobj.flatMap(lambda x:list(range(0,x))).data==[0, 0, 1, 0, 1, 2])
#chain call function
print(fpobj.maps(lambda x:x+1).maps(lambda x:x*2).reduces(lambda x,y:x+y).data)

#wordCount
string  = "will night hello will"
fpstr = fp.Fp(string.split(" "))
print(fpstr.maps(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).data) 
print(fpstr.groupBy(lambda x:x).mapValues(lambda x:len(x)).data)