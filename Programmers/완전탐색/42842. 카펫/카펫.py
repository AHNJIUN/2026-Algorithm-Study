'''def solution(brown, yellow):
    for w in range(yellow+1):
        if w>=1 and yellow % w == 0:
            h = yellow/w
            if w>=h and (w+2)*2 + 2*h == brown:
                return [w+2,h+2]'''
import math

def solution(brown, yellow):
    return next([(yellow//h)+2, h+2] for h in range(1,math.isqrt(yellow)+1) if yellow %h==0 if (yellow//h+2)*2 + 2*h == brown)