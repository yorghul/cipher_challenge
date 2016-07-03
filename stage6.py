# -*- coding: utf-8 -*-
"""
Decoding stage6 from Simon Singh Cipher Challenge
"""

from cipherchallenge import frequency, hist, quadrigram
from math import log10
import nltk
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
            print(float(quadgram[1])/N)
            logprob += log10(float(quadgram[1])/N)
    return(logprob, proba)
