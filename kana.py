# Import modules
import sys
from random import randint #allows for generation of random integer
import os

# Making code python3-compatible
if sys.version_info[0] == 3:
    basestring = str

def fnClearScreen():
    os.system('clear') # on linux / os x

def fnPrintMenu():
    print()
    for item in lstMenu:
        print(item)
    print()

def fnPrintResult(intTest, intCorrect):
    print()
    print("Items in Test: " + str(intTest))
    print("Questions correct: " + str(intCorrect))
    print("Percentage correct: " + str(intCorrect / intTest * 100))
    print()
    fnPrintMenu()

def fnPrintValueError():
    print()
    print("Error: The value entered was not a number.")
    print()

def fnPerformStudy(lstStudy):
    fnClearScreen()
    intStudy = 1
    intLesson = 10
    lstItems = []
    while intStudy <= intLesson:
        intItem = randint(0, len(lstStudy) - 1)
        if intItem not in lstItems:
            lstItems.append(intItem)
            print("Lesson " + str(intStudy) + " of " + str(intLesson) + ": [ " + lstStudy[intItem][0] \
            #+ (" " * (2 - int(len(lstStudy[intItem][0])))) \
            + " ] has the sound of: " + lstStudy[intItem][1])
            intStudy+=1
    print()
    fnPrintMenu()

def fnPerformTest(lstTest):
    fnClearScreen()
    intCorrect = 0
    intItem = 0
    intQuestion = 1
    intTest = 10
    lstItems = []
    while intQuestion <= intTest:
        strCorrectAnswer = ""
        intItem = randint(0, len(lstTest) - 1)
        if intItem not in lstItems:
            lstItems.append(intItem)
            strAnswer = input("\n" + "Question " + str(intQuestion) + " of " + str(intTest) + ": What is the sound of [ " + lstTest[intItem][0] + " ]?: ")
            strCorrectAnswer = lstTest[intItem][1]
            if strAnswer == strCorrectAnswer:
                print("Correct")
                intCorrect+=1
            else:
                print("Incorrect. The correct answer is: " + strCorrectAnswer)
            intQuestion+=1
    fnPrintResult(intTest, intCorrect)

# Menu Items
lstMenu = []
lstMenu.append("1. Study Hiragana")
lstMenu.append("2. Study Katakana")
lstMenu.append("3. Test Hiragana")
lstMenu.append("4. Test Katakana")
lstMenu.append("5. Exit")

lstHiragana = [ \
                 (u"\u3042","a"), (u"\u3044","i"), (u"\u3046","u"), (u"\u3048","e"), (u"\u304A","o") \
               , (u"\u304B","ka"), (u"\u304D","ki"), (u"\u304F","ku"), (u"\u3051","ke"), (u"\u3053","ko") \
               , (u"\u3055","sa"), (u"\u3057","shi"), (u"\u3059","su"), (u"\u305B","se"), (u"\u305D","so") \
               , (u"\u305F","ta"), (u"\u3061","chi"), (u"\u3064","tsu"), (u"\u3066","te"), (u"\u3068","to") \
               , (u"\u306A","na"), (u"\u306B","ni"), (u"\u306C","nu"), (u"\u306D","ne"), (u"\u306E","no") \
               , (u"\u306F","ha"), (u"\u3072","hi"), (u"\u3075","fu"), (u"\u3078","he"), (u"\u307B","ho") \
               , (u"\u307E","ma"), (u"\u307F","mi"), (u"\u3080","mu"), (u"\u3081","me"), (u"\u3082","mo") \
               , (u"\u3084","ya"), (u"\u3086","yu"), (u"\u3088","yo") \
               , (u"\u3089","ra"), (u"\u308A","ri"), (u"\u308B","ru"), (u"\u308C","re"), (u"\u308D","ro") \
               , (u"\u308F","wa"), (u"\u3092","wo") \
               , (u"\u3093","n") \
               , (u"\u304C","ga"), (u"\u304E","gi"), (u"\u3050","gu"), (u"\u3052","ge"), (u"\u3054","go") \
               , (u"\u3056","za"), (u"\u3058","ji"), (u"\u305A","zu"), (u"\u305C","ze"),  (u"\u305E","zo") \
               , (u"\u3060","da"), (u"\u3067","de"), (u"\u3069","do") \
               , (u"\u3070","ba"), (u"\u3073","bi"), (u"\u3076","bu"), (u"\u3079","be"), (u"\u307C","bo") \
               , (u"\u3071","pa"), (u"\u3074","pi"), (u"\u3077","pu"), (u"\u307A","pe"), (u"\u307D","po") \
               , (u"\u304D" + u"\u3083","kya"), (u"\u304D" + u"\u3085","kyu"), (u"\u304D" + u"\u3087","kyo") \
               , (u"\u3055" + u"\u3083","sha"), (u"\u3059" + u"\u3085","shu"), (u"\u305D" + u"\u3087","sho") \
               , (u"\u305F" + u"\u3083","cha"), (u"\u3064" + u"\u3085","chu"), (u"\u3068" + u"\u3087","cho") \
               , (u"\u306A" + u"\u3083","nya"), (u"\u306C" + u"\u3085","nyu"), (u"\u306E" + u"\u3087","nyo") \
               , (u"\u306F" + u"\u3083","hya"), (u"\u3075" + u"\u3085","hyu"), (u"\u307B" + u"\u3087","hyo") \
               , (u"\u307E" + u"\u3083","mya"), (u"\u3080" + u"\u3085","myu"), (u"\u3082" + u"\u3087","myo") \
               , (u"\u3089" + u"\u3083","rya"), (u"\u308B" + u"\u3085","ryu"), (u"\u308D" + u"\u3087","ryo")            
               #, (u"\u3090","wi"), (u"\u3091","we") \
               #, (u"\u3094","vu") \
               #, (u"\u3062","di"), (u"\u3065","du")
              ]

lstKatakana = [ \
                 (u"\u30A2","a"), (u"\u30A4","i"), (u"\u30A6","u"), (u"\u30A8","e"), (u"\u30AA","o") \
               , (u"\u30AB","ka"), (u"\u30AD","ki"), (u"\u30AF","ku"), (u"\u30B1","ke"), (u"\u30B3","ko") \
               , (u"\u30AC","ga"), (u"\u30AE","gi"), (u"\u30B0","gu"), (u"\u30B2","ge"), (u"\u30B4","go") \
               , (u"\u30B5","sa"), (u"\u30B7","shi"), (u"\u30B9","su"), (u"\u30BB","se"), (u"\u30BD","so") \
               , (u"\u30BF","ta"), (u"\u30C1","chi"), (u"\u30C4","tsu"), (u"\u30C6","te"), (u"\u30C8","to") \
               , (u"\u30CA","na"), (u"\u30CB","ni"), (u"\u30CC","nu"), (u"\u30CD","ne"), (u"\u30CE","no") \
               , (u"\u30CF","ha"), (u"\u30D2","hi"), (u"\u30D5","fu"), (u"\u30D8","he"), (u"\u30DB","ho") \
               , (u"\u30DE","ma"), (u"\u30DF","mi"), (u"\u30E0","mu"), (u"\u30E1","me"), (u"\u30E2","mo") \
               , (u"\u30E4","ya"), (u"\u30E6","yu"), (u"\u30E8","yo") \
               , (u"\u30E9","ra"), (u"\u30EA","ri"), (u"\u30EB","ru"), (u"\u30EC","re"), (u"\u30ED","ro") \
               , (u"\u30EF","wa"), (u"\u30F2","wo") \
               , (u"\u30F3","n") \
               , (u"\u30B6","za"), (u"\u30B8","ji"), (u"\u30BA","zu"), (u"\u30BC","ze"), (u"\u30BE","zo") \
               , (u"\u30C0","da"), (u"\u30C7","de"), (u"\u30C9","do") \
               , (u"\u30D0","ba"), (u"\u30D3","bi"), (u"\u30D6","bu"), (u"\u30D9","be"), (u"\u30DC","bo") \
               , (u"\u30D1","pa"), (u"\u30D4","pi"), (u"\u30D7","pu"), (u"\u30DA","pe"), (u"\u30DD","po") \
               , (u"\u30AB" + u"\u30E3","kya"), (u"\u30AD" + u"\u30E5","kyu"), (u"\u30AD" + u"\u30E7","kyo") \
               , (u"\u30B5" + u"\u30E3","sha"), (u"\u30B9" + u"\u30E5","shu"), (u"\u30BD" + u"\u30E7","sho") \
               , (u"\u30BF" + u"\u30E3","cha"), (u"\u30C4" + u"\u30E5","chu"), (u"\u30C8" + u"\u30E7","cho") \
               , (u"\u30CA" + u"\u30E3","nya"), (u"\u30CC" + u"\u30E5","nyu"), (u"\u30CE" + u"\u30E7","nyo") \
               , (u"\u30CF" + u"\u30E3","hya"), (u"\u30D5" + u"\u30E5","hyu"), (u"\u30DB" + u"\u30E7","hyo") \
               , (u"\u30DE" + u"\u30E3","mya"), (u"\u30E0" + u"\u30E5","myu"), (u"\u30E2" + u"\u30E7","myo") \
               , (u"\u30E9" + u"\u30E3","rya"), (u"\u30EB" + u"\u30E5","ryu"), (u"\u30ED" + u"\u30E7","ryo")
               #, (u"\u30F0","wi"), (u"\u30F1","we") \
               #, (u"\u30F4","vu")
               #, (u"\u30C2","di"), (u"\u30C5","du")
              ]

fnClearScreen()
intMenuChoice = 0
fnPrintMenu()
intLastMenuItem = int(lstMenu[-1][0]) #[-1] shows last entry in lstMenu; [0] shows first character from left of that entry
while intMenuChoice != intLastMenuItem: 
    try:
        intMenuChoice = int(input("Enter a choice from the Menu: "))
        if intMenuChoice == 1:
            fnPerformStudy(lstHiragana)
        elif intMenuChoice == 2:
            fnPerformStudy(lstKatakana)
        elif intMenuChoice == 3:
            fnPerformTest(lstHiragana)
        elif intMenuChoice == 4:
            fnPerformTest(lstKatakana)
        elif intMenuChoice != intLastMenuItem:
            print()
            print("Error: The value entered is outside the range of menu items")
            fnPrintMenu()
    except ValueError:
        fnPrintValueError()
