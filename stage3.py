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
        count = 1
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
        count = 1
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
stage3 = stage3.replace('X', ' ')
freqAnalysis, totalCount = cipher.frequency(stage3)
trigrams = cipher.trigram(stage3)
digrams = digram(stage3)
cipher.hist(freqAnalysis)


hypotheses = {}
hypotheses['X'] = ' '
hypotheses['Q'] = 'e'
##era
#hypotheses['Z'] = 'a'
#
##F ends a lot of words => i
#hypotheses['I'] = 'o'
#hypotheses['F'] = 'i'

#trigrams SOe frequents => che, + frequencies of S and O matches c and h
hypotheses['S'] = 'c'
hypotheses['O'] = 'h'

#per = YeV
hypotheses['Y'] = 'p'
hypotheses['V'] = 'r'
#
##e_*_ = e l'
#hypotheses['*'] = 'l'
#
#hypotheses['M'] = 'a'
#hypotheses['L'] = 'd'
#iT frequent => T in l
#hypotheses['T'] = 'l'
#trigrams lUa frequents => U in l
#hypotheses['U'] = 'l'
##triagrams aEl =? all
#hypotheses['E'] = 'l'
###word lMlla + frequency M => M in o
#hypotheses['M'] = 'o'
#
##word caMice + frequency => L in m
#hypotheses['L'] = 'm'
#
##word miEEi + frequency
#hypotheses['E'] = 's'
#
##VichiPsa = richiusa 
#hypotheses['V'] = 'r'
#hypotheses['P'] = 'u'
##Droli = broli
#hypotheses['D'] = 'b'

#####che/ per IMPASSE ###########

hypotheses = {}
hypotheses['X'] = ' '
hypotheses['T'] = 'n'
hypotheses['I'] = 'o'
hypotheses['F'] = 'i'
hypotheses['*'] = 'l'
hypotheses['E'] = 's'

hypotheses['U'] = 't'
hypotheses['V'] = 'r'
hypotheses['Q'] = 'e'

hypotheses['C'] = 'a'

hypotheses['S'] = 'c'
hypotheses['O'] = 'h'
hypotheses['Y'] = 'p'

hypotheses['B'] = 'a'
hypotheses['L'] = 'd'

hypotheses['M'] = 'a'
hypotheses['W'] = 'm'
hypotheses['H'] = 'z'

hypotheses['J'] = 'g'
hypotheses['D'] = 'f'
hypotheses['P'] = 'u'
hypotheses['R'] = 'q'
hypotheses['K'] = 'v'
hypotheses['G'] = 'a'
hypotheses['Z'] = 'a'
hypotheses['N'] = 'a'
hypotheses['A'] = 'b'
stage3hyp = cipher.decodage(stage3, hypotheses)
trigrams = cipher.trigram(stage3hyp)
digrams = digram(stage3hyp)
quadrigrams = quadrigram(stage3hyp)
stage3hyp

##DANTE INFERNO!!!!!!!
stage3sol = ''''o frati dissi che per cento milia perigli siete giunti
a loccidente a questa tanto picciola vigilia de nostri sensi che del
rimanente non vogliate negar lesperienza diretro al sol del mondo senza
gente considerate la vostra semenza fati non foste a viver come bruti ma per
seguir virtute e canoscenza li miei compagni fecio si aguti con questa
orazion picciola al cammino che a pena poscia li avrei ritenuti e volta
nostra poppa nel mattino dei remi facemmo ali al folle volo sempre acquistando
dal lato mancino tutte le stelle gia de laltro polo vedea la notte e l nostro
tanto basso che non surgea fuor del marin suolo cinque volte racceso e tanto
casso lo lume era di sotto da la luna poi che ntrati eravam ne lalto
passoquando napparve una montagna bruna per la distanza e parvemi alta
tanto quanto veduta non avea alcuna noi ci allegrammo e tosto torno in
pianto che de la nova terra un turbo nacque e percosse del legno il primo
canto tre volte il fe girar con tutte lacque a la quarta levar la poppa in
suso e la prora ire in giu comaltrui piacqueinfin che l mar fu sopra noi
richiuso  la parola in codice e equator'''