#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
class Fp(object):
    def __init__(self,dataobj:object):
        self.data = dataobj
    
    def foreach(self,func:'f:A=>Unit') ->None:
        for i in self.data:
            func(i)

    def maps(self,func:'f:A=>A') ->list:
        return list(map(func,self.data))

    def filters(self,func:'f:A=>Boolean') -> list:
        return list(filter(func,self.data))
    
    def filterNot(self,func:'f:A=>Boolean') -> list:
        temp = []
        for i in self.data:
            if not (func(i)):
                temp.append(i)
        return temp

    def flatten(self) ->list:
        temp = []
        for item in self.data:
            for i in item:
                temp.append(i)
        return temp
    
    def flatMap(self,func:'f:A=>List[B]') ->'List[B]':
        new_list = self.maps(func)
        return Fp(new_list).flatten()
        

    def reduces(self,func:'f:(A,A)=>A') ->'A':
        return reduce(func,self.data)

    def fold(self,init:'B',func:'f:(B,A)=>B') ->'B':
        temp = init
        for i in self.data:
            temp = func(temp,i)
        return temp


    def test(self):
        return Fp(self.data)



            

