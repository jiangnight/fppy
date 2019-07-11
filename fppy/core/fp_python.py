#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
class Fp(object):
    def __init__(self,dataobj:object):
        self.data = dataobj
    
    def foreach(self,func:'f:A=>Unit') ->None:
        for i in self.data:
            func(i)

    # iterator[A]=>iterator[A]
    def maps(self,func:'f:A=>A') -> 'Fp[List[A]]':
        temp = list(map(func,self.data))
        return Fp(temp)

    # iterator[A]=>iterator[A]
    def filters(self,func:'f:A=>Boolean') -> 'Fp[List[A]]':
        return Fp(list(filter(func,self.data)))
    
    #iterator[A]=>iterator[A]
    def filterNot(self,func:'f:A=>Boolean') -> 'Fp[List[A]]':
        temp = []
        for i in self.data:
            if not (func(i)):
                temp.append(i)
        return Fp(temp)
    
    #iterator[iterator[A]]=>iterator[A]
    def flatten(self) ->'Fp[List]':
        temp = []
        for item in self.data:
            for i in item:
                temp.append(i)
        return Fp(temp)
    
    #iterator[A]=>iterator[B]
    def flatMap(self,func:'f:A=>List[B]') -> 'Fp[List[B]]':
        return self.maps(func).flatten()


    #iterator[A]=>A
    def reduces(self,func:'f:(A,A)=>A') ->'Fp[A]':
        return Fp(reduce(func,self.data))

    # Iterator[(A,B)] => dict[A,B]
    def reduceByKey(self,func:'f:(A,A)=>A') -> 'Fp[dict[(K,V)]]':
        tempdict = {}
        for item in self.data:
            if tempdict.__contains__(item[0]):
                tempdict[item[0]] = func(tempdict[item[0]],item[1])
            else:
                tempdict[item[0]]=item[1]
        return Fp(tempdict)

    #iterator[A]=>A
    def fold(self,init:'B',func:'f:(B,A)=>B') ->'Fp[B]':
        temp = init
        for i in self.data:
            temp = func(temp,i)
        return Fp(temp)

    #Itrator[A] => dict[B,List[A]]
    def groupBy(self,func: 'f:A=>B') -> 'Fp[dict[B,List[A]]]':
        tempdict = {}
        for i in self.data:
            key = func(i)
            if tempdict.__contains__(key):
                tempdict[key].append(i)
            else:
                tempdict[key]=[]
                tempdict[key].append(i)
        return Fp(tempdict)
        


    ## dict[K,V] => dict[K,V]
    def mapValues(self,func:"f:V=>T") -> 'dict[K,T]':
        dictdata = {}
        for (k,v) in self.data.items():
            dictdata[k] = func(v)
        return Fp(dictdata)



    def test(self):
        return Fp(self.data)



            

