# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 15:02:23 2016

@author: Damien
"""

import sys
sys.path.insert(0,"~/cipherchallenge.py")
import cipherchallenge as cipher

def digram(text):
    dictFreqGroup = {}
    length = len(text)
    for j in range(0, length - 1):
        init = text[j:j+2]
        dictFreqGroup[init] = []
        count = 1
        i = 1
        print(init)
        while (i < length):
            if ((text[i:i+2]) == init):    
                print(text[i:i+2])
                print("Count " + str(count))
                dictFreqGroup[init].append(count)        
                count = 1
                i+=1                
            else:
                count +=1
                i+=1
    return dictFreqGroup

def quadrigram(text):
    dictFreqGroup = {}
    length = len(text)
    for j in range(0, length - 1):
        init = text[j:j+4]
        dictFreqGroup[init] = []
        count = 1
        i = 1
        print(init)
        while (i < length):
            if ((text[i:i+4]) == init):    
                print(text[i:i+4])
                print("Count " + str(count))
                dictFreqGroup[init].append(count)        
                count = 1
                i+=1                
            else:
                count +=1
                i+=1
    return dictFreqGroup

    
stage3 = '''IXDVMUFXLFEEFXSOQXYQVXSQTUIXWF*FMXYQVFJ*FXEFQUQX
JFPTUFXMX*ISSFLQTUQXMXRPQEUMXUMTUIXYFSSFI*MXKFJ
F*FMXLQXTIEUVFXEQTEFXSOQXLQ*XVFWMTQTUQXTITXKIJ*F
MUQXTQJMVX*QEYQVFQTHMXLFVQUVIXM*XEI*XLQ*XWITLIXE
QTHGXJQTUQXSITEFLQVGUQX*GXKIEUVGXEQWQTHGXDGUFXTIT
XDIEUQXGXKFKQVXSIWQXAVPUFXWGXYQVXEQJPFVXKFVUPUQXQX
SGTIESQTHGX*FXWFQFXSIWYGJTFXDQSFIXEFXGJPUFXSITXRPQEUG
XIVGHFITXYFSSFI*CXC*XSCWWFTIXSOQXCXYQTCXYIESFCX*FXCKV
QFXVFUQTPUFXQXKI*UCXTIEUVCXYIYYCXTQ*XWCUUFTIXLQFXVQW
FXDCSQWWIXC*FXC*XDI**QXKI*IXEQWYVQXCSRPFEUCTLIXLC*X*C
UIXWCTSFTIXUPUUQX*QXEUQ**QXJFCXLQX*C*UVIXYI*IXKQLQCX*CX
TIUUQXQX*XTIEUVIXUCTUIXACEEIXSOQXTITXEPVJQCXDPIVXLQ*X
WCVFTXEPI*IXSFTRPQXKI*UQXVCSSQEIXQXUCTUIXSCEEIX*IX*PWQ
XQVZXLFXEIUUIXLZX*ZX*PTZXYIFXSOQXTUVZUFXQVZKZWXTQX*Z*
UIXYZEEIRPZTLIXTZYYZVKQXPTZXWITUZJTZXAVPTZXYQVX*ZXLFEUZT
HZXQXYZVKQWFXZ*UZXUZTUIXRPZTUIXKQLPUZXTITXZKQZ
XZ*SPTZXTIFXSFXZ**QJVNWWIXQXUIEUIXUIVTIXFTXYFNTUIXS
OQXLQX*NXTIKNXUQVVNXPTXUPVAIXTNSRPQXQXYQVSIEE
QXLQ*X*QJTIXF*XYVFWIXSNTUIXUVQXKI*UQXF*XDQXJFVBVXSI
TXUPUUQX*BSRPQXBX*BXRPBVUBX*QKBVX*BXYIYYBXFTXEPEIXQX
*BXYVIVBXFVQXFTXJFPXSIWB*UVPFXYFBSRPQFTDFTXSOQX*XWBVXDP
XEIYVBXTIFXVFSOFPEIXX*BXYBVI*BXFTXSILFSQXQXQRPBUIV'''

stage3 = stage3.replace("\n", "")

freqAnalysis, totalCount = cipher.frequency(stage3)
trigrams = cipher.trigram(stage3)
digrams = digram(stage3)
cipher.hist(freqAnalysis)


hypotheses = {}
hypotheses['X'] = ' '
hypotheses['Q'] = 'e'
hypotheses['I'] = 'a'
#F ends a lot of words => o
hypotheses['F'] = 'i'

#trigrams SOe frequents => che, + frequencies of S and O matches c and h
hypotheses['S'] = 'c'
hypotheses['O'] = 'h'

#iT frequent => T in l
hypotheses['T'] = 'l'
#trigrams lUa frequents => U in l
hypotheses['U'] = 'l'
stage3hyp = cipher.decodage(stage3, hypotheses)
stage3hyp = stage3hyp.replace(" ", "_")
trigrams = cipher.trigram(stage3hyp)
digrams = digram(stage3hyp)
quadrigrams = quadrigram(stage3hyp)