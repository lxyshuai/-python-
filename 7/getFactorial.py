# coding=utf-8
"""
求n!的结果
"""
def getFactorial(n):
    if n == 1:
        return 1
    return n * getFactorial(n - 1)
