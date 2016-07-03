# -*- coding: utf-8 -*-
"""
The Cipher challenge
http://simonsingh.net/cryptography/cipher-challenge/the-ciphertexts/
"""

#Stage 1:

import nltk
import string
import matplotlib.pyplot as plt
import numpy as np
import csv

def read_file(path):
    with open(path, 'rb') as f:
        fileCSV = csv.reader(f, delimiter=',')
        dicti = {}
        for row in fileCSV:
            if '#' not in row[0]:
                dicti[row[0]] = float(row[1])
    return dicti
    
digramsenglish = read_file('C:/Users/Damien/Documents/GitHub/cipher_challenge/english-digrams.csv')  
trigramsenglish = read_file(str('C:/Users/Damien/Documents/GitHub/cipher_challenge/english-trigrams.csv'))
freqEnglish = read_file('C:/Users/Damien/Documents/GitHub/cipher_challenge/english-letter-frequency.csv')  


def topN(dictionnary, N):
    L = sorted(dictionnary, key=dictionnary.get, reverse=True)
    l = []
    for i in range(0,N):
        l.append(L[i])
    return l

def words(string):
    return nltk.wordpunct_tokenize(string)

def frequency(codedText):
    dictionnary = {}
    countTotal = 0
    for char in list(string.ascii_uppercase):
        dictionnary[char] = 0
    for char in codedText:
        if char in dictionnary.keys():
            dictionnary[char] += 1
            countTotal += 1
    for key in dictionnary.keys():
        dictionnary[key] = round(dictionnary[key]*100.0/countTotal,1)
    return(dictionnary, countTotal)

stage1 = "BT JPX RMLX PCUV AMLX ICVJP IBTWXVR CI M LMT’R PMTN, MTN YVCJX CDXV MWMBTRJ JPX AMTNGXRJBAH UQCT JPX QGMRJXV CI JPX YMGG CI JPX HBTW’R QMGMAX; MTN JPX HBTW RMY JPX QMVJ CI JPX PMTN JPMJ YVCJX. JPXT JPX HBTW’R ACUTJXTMTAX YMR APMTWXN, MTN PBR JPCUWPJR JVCUFGXN PBL, RC JPMJ JPX SCBTJR CI PBR GCBTR YXVX GCCRXN, MTN PBR HTXXR RLCJX CTX MWMBTRJ MTCJPXV. JPX HBTW AVBXN MGCUN JC FVBTW BT JPX MRJVCGCWXVR, JPX APMGNXMTR, MTN JPX RCCJPRMEXVR. MTN JPX HBTW RQMHX, MTN RMBN JC JPX YBRX LXT CI FMFEGCT, YPCRCXDXV RPMGG VXMN JPBR YVBJBTW, MTN RPCY LX JPX BTJXVQVXJMJBCT JPXVXCI, RPMGG FX AGCJPXN YBJP RAM"
    
freqAnalysis, totalCharacter = frequency(stage1)

def hist(dictionnary):
    X = np.arange(len(dictionnary)) + 1
    plt.bar(X, dictionnary.values(), align = 'center', width=0.5)
    plt.xticks(X, sorted(dictionnary.keys()))
    plt.show()
    return 0
    
hist(freqAnalysis)
hist(freqEnglish)
l = list(string.ascii_lowercase)
L = list(string.ascii_uppercase)

codedDict = {}
for j in range(0,len(l)):
    codedDict = {}
    for i in range(0, len(L)):
        if (i + j < len(L)):    
            codedDict[L[i+j]] = l[i]
        else:
            codedDict[L[i+j-26]] = l[i]
    decode = ""
    for char in stage1:
        if char in L:
            decode += codedDict[char]
        else:
            decode += char
    print("New letter:")
    print(l[j])
    print(decode)
                  
codedDict = {}
codedDict['A']= 'c'
codedDict['B']= 'i'
codedDict['C']= 'o' 
codedDict['D']= 'v'	 
codedDict['E']= 'y'
codedDict['F']= 'b' 
codedDict['G']= "l"
codedDict['H']= 'k'	 
codedDict['I']= 'n'
codedDict['J']= 't'	  
codedDict['L']= 'm'	 
codedDict['M']= 'a' 
codedDict['N']= 'd'	 
codedDict['P']= 'h'	 
codedDict['Q']= 'p'
codedDict['R']= 's' 
codedDict['S']= 'j'	 
codedDict['T']= 'n'
codedDict['U']= 'u'	 
codedDict['V']= 'r'	 
codedDict['W']= 'g'	 
codedDict['X']= 'e'	 
codedDict['Y']= 'w'	 

decode = ""
for i in range(0, len(stage1)):
    if stage1[i] in codedDict.keys():
        decode += codedDict[stage1[i]]
    elif stage1[i] in L:
        decode += "."
    else:
        decode += stage1[i]
print(decode)

decodeWithLetters = ""
for i in range(0, len(stage1)):
    if stage1[i] in codedDict.keys():
        decodeWithLetters += codedDict[stage1[i]]
    else:
        decodeWithLetters += stage1[i]
print(decodeWithLetters)

decodedCode = "in the same hour came north ningers on a man’s hand, and wrote over against the candlestick upon the plaster on the wall on the king’s palace; and the king saw the part on the hand that wrote. then the king’s countenance was changed, and his thoughts troubled him, so that the joints on his loins were loosed, and his knees smote one against another. the king cried aloud to bring in the astrologers, the chaldeans, and the soothsayers. and the king spake, and said to the wise men on babylon, whosoever shall read this writing, and show me the interpretation thereon, shall be clothed with sca"


#Stage 2:
stage2 = "MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU"
freqAnalysis2, totalCharacter2 = frequency(stage2)
hist(freqAnalysis2)

l = list(string.ascii_lowercase)
L = list(string.ascii_uppercase)

codedDict = {}
for j in range(0,len(l)):
    codedDict = {}
    for i in range(0, len(L)):
        if (i + j < len(L)):    
            codedDict[L[i+j]] = l[i]
        else:
            codedDict[L[i+j-26]] = l[i]
    decode = ""
    for char in stage2:
        if char in L:
            decode += codedDict[char]
        else:
            decode += char
    print("New letter: " + str(j))
    print(l[j])
    print(decode)

#Solution    
#New letter: 7
#h
#faber est suae quisque fortunae appius claudius caecus dictum arcanum est neutron

#Stage 4: Vigenere
stage4 = """K Q O W E F V J P U J U U N U K G L M E K J I

N M W U X F Q M K J B G W R L F N F G H U D W

U U M B S V L P S N C M U E K Q C T E S W R E

E K O Y S S I W C T U A X Y O T A P X P L W P

N T C G O J B G F Q H T D W X I Z A Y G F F N

S X C S E Y N C T S S P N T U J N Y T G G W Z

G R W U U N E J U U Q E A P Y M E K Q H U I D

U X F P G U Y T S M T F F S H N U O C Z G M R

U W E Y T R G K M E E D C T V R E C F B D J Q

C U S W V B P N L G O Y L S K M T E F V J J T

W W M F M W P N M E M T M H R S P X F S S K F

F S T N U O C Z G M D O E O Y E E K C P J R G

P M U R S K H F R S E I U E V G O Y C W X I Z

A Y G O S A A N Y D O E O Y J L W U N H A M E

B F E L X Y V L W N O J N S I O F R W U C C E

S W K V I D G M U C G O C R U W G N M A A F F

V N S I U D E K Q H C E U C P F C M P V S U D

G A V E M N Y M A M V L F M A O Y F N T Q C U

A F V F J N X K L N E I W C W O D C C U L W R

I F T W G M U S W O V M A T N Y B U H T C O C

W F Y T N M G Y T Q M K B B N L G F B T W O J

F T W G N T E J K N E E D C L D H W T V B U V

G F B I J G Y Y I D G M V R D G M P L S W G J

L A G O E E K J O F E K N Y N O L R I V R W V

U H E I W U U R W G M U T J C D B N K G M B I

D G M E E Y G U O T D G G Q E U J Y O T V G G

B R U J Y S"""

stage4 = stage4.replace(" ", "")
stage4 = stage4.replace("\n", "")
#balayage par groupe

dictFreqGroup = {}
for j in range(0, len(stage4) - 2):
    init = stage4[j:j+3]
    dictFreqGroup[init] = []
    count = 1
    i = 1
    print(init)
    while (i < len(stage4)):
        if ((stage4[i:i+3]) == init):    
            print(stage4[i:i+3])
            print("Count " + str(count))
            dictFreqGroup[init].append(count)        
            count = 1
            i+=1                
        else:
            count +=1
            i+=1


alphaB = []
for i in range(0,5):
    alphaB.append("")

j=0
i=0 
while i< len(stage4):       
    while i < len(stage4) and j<5:
        alphaB[j]+=stage4[i]
        j+=1
        i+=1
    j=0

listFreq = []    
for i in range(0,5):
    dic, count =  frequency(alphaB[i])
    listFreq.append(dic)
    
hist(listFreq[0])

def ceasar (decalage):
    codedDict = {}
    l = list(string.ascii_lowercase)
    L = list(string.ascii_uppercase)
    for i in range(0, 26):
        while i + decalage < 26:    
           codedDict[L[i+decalage]] = l[i]
           i+=1
        codedDict[L[i+decalage-26]] = l[i]
    return(codedDict)


def decode(text, decalage):
    if decalage == 0:
        return(text)
    else:
        clearText = ""
        dico = ceasar(decalage)
        for i in range(0, len(text)):
            clearText += dico[text[i]]
        print clearText
        return(clearText)
    
decode(alphaB[0],18)

hypothesis = []
hypothesis.append(18)
hypothesis.append(2)
hypothesis.append(20)
hypothesis.append(1)
hypothesis.append(26)

def vigenere(textList, hypothesis):
    keyLength = len(hypothesis)
    clearText = ""
    decodeList = []
    k=0
    j=0
    l=0
    textLength = 0
    for i in range(0, keyLength):
        textLength += len(textList[i])
        decodeList.append(decode(textList[i], hypothesis[i]))
    while k<textLength and l<len(textList[keyLength-1]):
        while k<textLength and j < keyLength:
            clearText+=decodeList[j][l]
            j+=1
            k+=1
        l+=1        
        j=0
    return(clearText)


vigenere(alphaB, hypothesis)

alphaBtest = []
for i in range(0,5):
    alphaBtest.append([])
for i in range(0, len(alphaB[0])):
    alphaBtest[0].append(alphaB[0][i])
for i in range(0, len(alphaB[1])):
    alphaBtest[1].append(alphaB[1][i])
for i in range(0, len(alphaB[2])):
    alphaBtest[2].append(alphaB[2][i])
for i in range(0, len(alphaB[3])):
    alphaBtest[3].append(alphaB[3][i])
for i in range(0, len(alphaB[4])):
    alphaBtest[4].append(alphaB[4][i])

alphaBtestDot = []
for i in range(0,5):
    alphaBtestDot.append([])
for i in range(0, len(alphaB[0])):
    alphaBtestDot[0].append(alphaB[0][i])
for i in range(0, len(alphaB[1])):
    alphaBtestDot[1].append(alphaB[1][i])
for i in range(0, len(alphaB[2])):
    alphaBtestDot[2].append(alphaB[2][i])
for i in range(0, len(alphaB[3])):
    alphaBtestDot[3].append(alphaB[3][i])
for i in range(0, len(alphaB[4])):
    alphaBtestDot[4].append(alphaB[4][i])

vigenere(alphaBtest, hypothesis)

#stage 4 Solution:
stage4sol = '''souventpoursamuserleshommesdequipageprennentdesalbatrosvastesoiseauxdesmersquisuiventindolentscompagnonsdevoyagelenavireglissantsurlesgouffresamersapeinelesontilsdeposessurlesplanchesquecesroisdelazurmaladroitsethonteuxlaissentpiteusementleursgrandesailesblanchescommedesavironstraineracotedeuxcevoyageurailecommeilestgaucheetveuleluinagueresibeauquilestcomiqueetlaidlunagacesonbecavecunbrulegueulelautremimeenboitantlinfirmequivolaitlepoeteestsemblableauprincedesnueesquihantelatempeteetseritdelarcherbaudelaireexilesurlesolaumilieudeshueeslemotpouretagequatreesttrajansesailesdegeantlempechentdemar'''
#Baudelaire!!

#Stage 3:
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

def frequency(codedText):
    dictionnary = {}
    countTotal = 0
    for char in list(string.ascii_uppercase):
        dictionnary[char] = 0
    dictionnary['*']=0
    for char in codedText:
        if char in dictionnary.keys():
            dictionnary[char] += 1
            countTotal += 1
    for key in dictionnary.keys():
        dictionnary[key] = round(dictionnary[key]*100.0/countTotal,1)
    return dictionnary
    
    
charFreq = frequency(stage3)
#hist(charFreq)

def trigram(text):
    dictFreqGroup = {}
    length = len(text)
    for j in range(0, length - 2):
        init = text[j:j+3]
        count = 0
        i=0
        print(init)
        while (i < length - 2):
            if ((text[i:i+3]) == init):         
                count += 1
                i+=1                
            else:
                i+=1
        if count > 1:
            dictFreqGroup[init]=count
    return dictFreqGroup

tris = trigram(stage3)

hypothese = {}
hypothese['X']=' '
hypothese['T']='n'
hypothese['I']='o' #non = TIT
# hypothese['F']='u' - FT = un --> NOK. Obligation: F = i
# S = f,t, d, n, s
#N,Z,B = a,e,i,o,u
#P=a,i,o,p,u
#Y=c,n,p
#F,M=a,d,e,h,i
hypothese['F']='i'
#hypothese['*']='c' not good, come up with n?c
#Q=e,o -- only e if E=s
#E=c,s
#U=c,n,t,z from no***
#*=l,n,p
#from ?i?i?i?, get M=o,a,s,e,i
#o???ion = opinion?? -- no good, P NOK

hypothese['V']='r'
hypothese['U']='t'
hypothese['E']='s'
hypothese['*']='l'
hypothese['L']='d'
hypothese['Y']='p'
hypothese['Z']='a'
hypothese['W']='m'
hypothese['B']='a'
hypothese['Q']='e'
hypothese['S']='c'
hypothese['C']='a'
hypothese['J']='g'
hypothese['O']='h'
hypothese['D']='v'
hypothese['G']='a'
hypothese['P']='u'
hypothese['R']='q'
hypothese['M']='a'
hypothese['H']='z'
hypothese['K']='v'
hypothese['A']='b'
hypothese['N']='o'

#P=e,u
#B=e,a
#N=e,a,o
#K=e,u,v

#voyelles: I, M, Q, T, 

def decodage(text, hyp):
    clearText = ""
    for i in range(0, len(text)):
        char = text[i]
        if char in hyp.keys():
            clearText+= hyp[char]
        else:
            clearText+= text[i]
    return clearText

decodage(stage3, hypothese)


def smallWords(text, wlen):
    dico = {}
    leng = len(text)
    i = 0
    for i in range(0, leng):
        if text[i]==' ':
            for j in range(0, wlen):
                if text[i+j+2]==' ':
                   word = text[i+1:i+j+2]
                   if word in dico.keys():
                       dico[word]+=1
                   else:
                       dico[word]=1
    return dico

shorties = smallWords(stage3, 3)

def permu(xs):
    if xs:
        r , h = [],[]
        for x in xs:
            if x not in h:
                ts = xs[:]; ts.remove(x)
                for p in permu(ts):
                    r.append([x]+p)
            h.append(x)
        return r
    else:
        return [[]]
        
        
permu([1,2,3,4,5])

def options(freqCoded, freqClear, error):
    alphaCod = freqCoded.keys()
    alphaClear = freqClear.keys()
    permuCod = permu(alphaCod)
    hypotheses = []
    length = len(freqCoded)
    for i in range(0, len(permuCod)):
            k = 0
            dico = {}
            cod = permuCod[i] 
            while (k < length) and (freqCoded[cod[k]]<=freqClear[alphaClear[k]]*error):
                dico[permuCod[i][k]]=alphaClear[k]          
                k+=1
            if k == length:
                hypotheses.append(dico)
    return hypotheses


commons = {}
for i in tris.keys():
    tri = tris[i] 
    if tri >3 and i[1] <>' ' and i[0] <>' ' and i[2] <>' ':
        commons[i] = tri
        
freqIta = {}
freqIta['e']=11.49
freqIta['a']=10.85
freqIta['i']=10.18
freqIta['o']=9.97
freqIta['n']=7.02
freqIta['t']=6.97
freqIta['r']=6.19
freqIta['l']=5.7
freqIta['s']=5.5
freqIta['c']=4.3



freqCode = {}
freqCode['Q']=11.3
freqCode['I']=9.7
freqCode['F']=8.6
freqCode['T']=7.9
freqCode['U']=7.7
freqCode['*']=6.8
freqCode['V']=6.1
freqCode['E']=4.6
freqCode['S']=4.6

try1 = options(freqCode, freqIta, 1.3)


for i in range(0,len(try1)):
    print decodage(stage3, try1[i])
    print '\n'


#Stage 6
stage6 = '''OCOYFOLBVNPIASAKOPVYGESKOVMUFGUWMLNOOEDRNCFORSO

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

    EPGCHK'''
    
stage6 = stage6.replace('\n', '')
stage6 = stage6.replace(' ', '')

def frequency(codedText):
    dictionnary = {}
    countTotal = 0
    for char in list(string.ascii_uppercase):
        dictionnary[char] = 0
    for char in codedText:
        if char in dictionnary.keys():
            dictionnary[char] += 1
            countTotal += 1
    for key in dictionnary.keys():
        dictionnary[key] = round(dictionnary[key]*100.0/countTotal,1)
    return dictionnary
    
    
charFreq = frequency(stage6)

def decodageDi(text, hyp):
    clearText = ""
    for i in range(0, len(text), 3):
        di = text[i:i+2]
        print(di)
        if di in hyp.keys():
            clearText+= hyp[di]
            clearText+='-'
        else:
            clearText+= di
            clearText+='-'
    return clearText



def digram(text):
    dictFreqGroup = {}
    length = len(text)
    for j in range(0, length - 1, 2):
        init = text[j:j+2]
        count = 0
        i=0
        print(init)
        while (i < length - 1):
            if ((text[i:i+2]) == init):         
                count += 1
                i+=2              
            else:
                i+=2
        if count > 1:
            dictFreqGroup[init]=count
    return dictFreqGroup
    
dis = digram(stage6)

    
    
def quadrigram(text):
    dictFreqGroup = {}
    length = len(text)
    for j in range(0, length, 3):
        init = text[j:j+5]
        count = 0
        i=0
        print(init)
        while (i < length - 4):
            if ((text[i:i+5]) == init):         
                count += 1
                i+=3                
            else:
                i+=3
        if count > 1:
            dictFreqGroup[init]=count
    return dictFreqGroup
    


def topN(dictionnary, N):
    L = sorted(dictionnary, key=dictionnary.get, reverse=True)
    l = []
    for i in range(0,N):
        l.append(L[i])
    return l

commonDis = topN(dis, 10)

stage6S = ''''''
for i in range(0, len(stage6), 2):
    stage6S+=stage6[i]
    stage6S+=stage6[i+1]
    stage6S+='-'

hypothese = {}
hypothese['FO']='th'
hypothese['LB']='at'
hypothese['RS']='er'
hypothese['OF']='ht'
hypothese['BL']='ta'
hypothese['SR']='re'

quadris = quadrigram(stage6S)
decodageDi(stage6S,hypothese)