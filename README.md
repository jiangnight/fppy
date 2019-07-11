# fppy add some fp functions to python

## WordCount use One line
```
fp.Fp("will night hello will".split(" ")) \
  .maps(lambda x:(x,1)) \
  .reduceByKey(lambda x,y:x+y) \
  .data   ## {'will': 2, 'hello': 1, 'night': 1}
  
fp.Fp("will night hello will".split(" ")) \
  .groupBy(lambda x:x) \
  .mapValues(lambda x:len(x)) \
  .data   ## {'will': 2, 'hello': 1, 'night': 1}
  
```

## install 
> git clone https://github.com/jiangnight/fppy.git && 
> cd fppy && 
> python setup.py install

## use package

### first convert python Iterator(list,set,dict..) to Fp object and use .data to get data
```
import fppy.core.fp_python as fp
data=[1,2,3]
## convert data to fp object
fpobj = fp.Fp(data)
##get data
origindata = fpobj.data
```

### second you can use suffix notation to use some higher-order function

#### functions 


* **maps** the same as built-in map to make a function act on each element
```
fpobj.maps(lambda x:x+1).data == [2,3,4]
```
* **filters** the same as built-in filter 
```
fpobj.filters(lambda x:x%2==0).data==[2]
```
* **filterNot**
```
fpobj.filterNot(lambda x:x%2==0).data==[1,3]
```
* **flatten**
```
fpobj.maps(lambda x:list(range(0,x))).flatten().data==[0, 0, 1, 0, 1, 2]
```
* **reduce**
```
fpobj.reduces(lambda x,y:x+y).data==6
```

* **fold** you can give a init value to reduce
```
fpobj.fold(1,lambda x,y:x+y).data == 7
```

* **flatMap**
```
fpobj.flatMap(lambda x:list(range(0,x))).data==[0, 0, 1, 0, 1, 2]
```
* **mapValues** for dict
```
data = {'a':1,'b':2}
fpobj = fp.Fp(data)
fpobj.mapValues(lambda x:x+1) ## {'a': 2, 'b': 3}
```

* **groupBy** 
```
data = ["will","night","hello","will"]
fpobj = fp.Fp(data)
fpobj.groupBy(lambda x:x).data ## {'will': ['will', 'will'], 'hello': ['hello'], 'night': ['night']}
fpobj.groupBy(lambda x:x[1:2]).data ##{'i': ['will', 'night', 'will'], 'e': ['hello']}
```




