# -*- coding: utf-8 -*-
"""
Decoding stage6 from Simon Singh Cipher Challenge
"""

from cipherchallenge import frequency, hist, quadrigram, playfairDecrypt
from math import log10
import nltk
import numpy
import copy
emma = nltk.corpus.gutenberg.words("austen-emma.txt")

stage6 = """OCOYFOLBVNPIASAKOPVYGESKOVMUFGUWMLNOOEDRNCFORSO

CVMTUUTYERPFOLBVNPIASAKOPVIVKYEOCNKOCCARICVVLTS

OCOYTRFDVCVOOUEGKPVOOYVKTHZSCVMBTWTRHPNKLRCUEGM

SLNVLZSCANSCKOPORMZCKIZUSLCCVFDLVORTHZSCLEGUXMI

FOLBIMVIVKIUAYVUUFVWVCCBOVOVPFRHCACSFGEOLCKMOCG

EUMOHUEBRLXRHEMHPBMPLTVOEDRNCFORSGISTHOGILCVAIO

AMVZIRRLNIIWUSGEWSRHCAUGIMFORSKVZMGCLBCGDRNKCVC

PYUXLOKFYFOLBVCCKDOKUUHAVOCOCLCIUSYCRGUFHBEVKRO

ICSVPFTUQUMKIGPECEMGCGPGGMOQUSYEFVGFHRALAUQOLEV

KROEOKMUQIRXCCBCVMAODCLANOYNKBMVSMVCNVROEDRNCGE

SKYSYSLUUXNKGEGMZGRSONLCVAGEBGLBIMORDPROCKINANK

VCNFOLBCEUMNKPTVKTCGEFHOKPDULXSUEOPCLANOYNKVKBU

OYODORSNXLCKMGLVCVGRMNOPOYOFOCVKOCVKVWOFCLANYEF

VUAVNRPNCWMIPORDGLOSHIMOCNMLCCVGRMNOPOYHXAIFOOU

EPGCHK"""

stage6 = stage6.replace("\n", "")
    
freq = frequency(stage6)
hist(freq)
quadris = quadrigram(stage6)

def criteria_english(decodedText):
    quadrigrams = quadrigram(decodedText)
    N = len(quadrigrams.keys())
    proba = {}
    logprob = 0
    for quadgram in quadrigrams.iteritems():
        if quadgram[1] > 0:
            proba[quadgram[0]] = float(quadgram[1])/N
            logprob += log10(float(quadgram[1])/N)
    return(logprob)

def initialise(text, hypothese):
    return [['a','b','c','d','e'],['f','g','h','i','k'],['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]

def hillClimb(text, hypothese):
    key = initialise(text, hypothese)         
    crit1 = criteria_english(playfairDecrypt(text, key))
    crit2 = 0
    swapLog = []
    tries = 0
    while tries < 300:
        swap = numpy.random.randint(0,5,4)
        print(swap)
        if any(a is swap for a in swapLog) == False:    
            transKey = copy.deepcopy(key)
            transKey[swap[0]][swap[1]] = key[swap[2]][swap[3]]
            transKey[swap[2]][swap[3]] = key[swap[0]][swap[1]]
            crit2 = criteria_english(playfairDecrypt(text, transKey))
            print(crit2)
            if crit1 >= crit2:
                swapLog.append(swap)
                tries+=1
            else:
                key = transKey
                print(key)
                tries = 0
                crit1 = crit2
                swapLog = []
    return (playfairDecrypt(stage6, key), crit2)
                
hillClimb(stage6, 'a')    
  
a = (1,2,3)
a[1]

#try and swap eqrly hypothesis - random
#for each key, find swap which maximises the criteria