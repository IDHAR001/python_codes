import argparse


def func01(a,*args,b,**kwargs):
    print(a)
    print(args)
    print(b)
    print(kwargs)
func01(1,2,3,b=4,c=5,d=6)