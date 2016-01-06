#!/usr/bin/env python
# -*- coding: utf-8 -*

# Import modules
import sys                      # allows for system variables
import copy                     # allows for copying lists
import os                       # allows for OS specific functions
import pickle                   # allows for loading and dumping into binary files
from random import randint      # allows for generation of random integer

# Making code python3-compatible; fail to run on python2.x
if sys.version_info[0] == 3:
    basestring = str
else:
    print("\n")
    print("Error:")
    print("   Cause:      Cannot run under Python version 2.")
    print("   Resolution: Install Python version 3 (or higher).")
    print("\n")
    exit()

# Clear progress by saving empty files for relevant character set
def clear_progress(intMenuChoice):
    clear_screen()
    lstDefault = []
    file_save(intMenuChoice,
              "Right",
              lstDefault)
    file_save(intMenuChoice,
              "Wrong",
              lstDefault)
    file_save(intMenuChoice,
              "Learned",
              lstDefault)
    strCharacterSet = get_character_set(intMenuChoice)
    print("Progress for {} has been cleared.".format(strCharacterSet))
    display_menu()

def clear_screen():
    os.system('clear')
    # on linux / os x

# Display error if menu choice outside range
def display_error_outside_range(intFirstMenuItem,
                                intLastMenuItem):
    clear_screen()
    strResolution = display_menu_error_resolution(intFirstMenuItem,
                                                  intLastMenuItem)
    print("Error:")
    print("   Cause:      The value entered is not a menu item.")
    print(strResolution)
    display_menu()

# Display error if menu choice is not a number
def display_error_value(intFirstMenuItem,
                        intLastMenuItem):
    clear_screen()
    strResolution = display_menu_error_resolution(intFirstMenuItem,
                                                  intLastMenuItem)
    print("Error:")
    print("   Cause:      The value entered was not a number.")
    print(strResolution)
    display_menu()

def display_menu():
    print()
    for item in lstMenu:
        print(item)

# Common error resolution for display_error_outside_range and display_error_value
def display_menu_error_resolution(intFirstMenuItem,
                                  intLastMenuItem):
    strResolution = "   Resolution: Enter a number between {} and {}.".format(str(intFirstMenuItem),
                                                                              str(intLastMenuItem))
    return strResolution

# Display results after each test
def display_result(intLenTest,
                   intCorrect):
    print("Items in Test: {}".format(str(intLenTest)))
    print("Questions correct: {}".format(str(intCorrect)))
    print("Percentage correct: {}".format(str(round((intCorrect / intLenTest * 100),
                                                    2))))
    display_menu()

# Load list from relevant file: If file is empty, return empty list; if file not found then create it
def file_load(intMenuChoice,
              strFileType):
    lstDefault = []
    try:
        strFileName = get_filename(intMenuChoice,
                                   strFileType)
        with open(strFileName,
                  'rb') as f:
            lstLoadFile = pickle.load(f)
        return lstLoadFile
    except EOFError:
        return lstDefault
    except FileNotFoundError:
        file_save(intMenuChoice,
                  strFileType,
                  lstDefault)
        return lstDefault

# Save list into relevant file
def file_save(intMenuChoice,
              strFileType,
              lstSaveFile):
    lstSaveFile.sort()
    strFileName = get_filename(intMenuChoice,
                               strFileType)
    with open(strFileName,
              'wb') as f:
        pickle.dump(lstSaveFile, f)

# Get character set name either "Hiragana" or "Katakana"
def get_character_set(intMenuChoice):
    if intMenuChoice in (1,
                         3,
                         5):
        strCharacterSet = "Hiragana"
    elif intMenuChoice in (2,
                           4,
                           6):
        strCharacterSet = "Katakana"
    return strCharacterSet

# Get filename, based on menu choice and file type
def get_filename(intMenuChoice,
                 strFileType):
    strProgram = "Kana"
    strCharacterSet = get_character_set(intMenuChoice)
    strExtenstion = "bin"
    strFileName = "{}{}{}.{}".format(strProgram,
                                     strCharacterSet,
                                     strFileType,
                                     strExtenstion)
    return strFileName

# intItemLimit is used to set intLesson and intTest
def get_item_limit():
    intItemLimit = 9
    return intItemLimit

# intItemCount is to set count for moving items to Learned or Mistake
def get_item_count():
    intItemCount = 5
    return intItemCount

# A Mistake is several Wrongs (set from get_item_count):
# These are "problematic" characters which require attention (will be returned first in study or test lists)
def get_mistakes(lstWrong):
    lstMistake = []
    intItemMistakeCount = get_item_count()
    for item in lstWrong:
        if lstWrong.count(item) >= intItemMistakeCount:
            if item not in lstMistake:
                lstMistake.append(item)
    return lstMistake

# add leading spaces to pad out character to same length
def get_padded_item(strItem):
    strPaddedItem = (" " * (2 * (2 - len(strItem)))) + strItem
    return strPaddedItem

# Study: random items from lstMistake before random items from lstStudy
def perform_study(intMenuChoice,
                  lstStudy):  # lstStudy is copy of either lstHiragana or lstKatakana
    clear_screen()
    intStudy = 1
    intLesson = get_item_limit()
    lstWrong = file_load(intMenuChoice,
                         "Wrong")
    lstLearned = file_load(intMenuChoice,
                           "Learned")
    lstMistake = get_mistakes(lstWrong)
    lstItems = lstLearned[:]
    # copy lstLearned into lstItems so that learned items are not tested
    strCharacterSet = get_character_set(intMenuChoice)
    # if all characters have been learned, then no need to study
    if len(lstLearned) == len(lstStudy):
        print("\n" +
              "All characters for the lesson: {} have been learned.".format(strCharacterSet))
        display_menu()
    else:
        intLenStudy = len(lstStudy) - len(lstLearned)
        # lesson consists of testable items which have not been learned
        # but, if fewer items than intLesson (9) require questioning,
        # then only question those; otherwise study full amount: intStudy
        if intLenStudy < intLesson:
            intStudyLen = intLenStudy
        else:
            intStudyLen = intLesson
        while intStudy <= intStudyLen:
            # If Mistakes are present, test them first, else random character from lstStudy
            if len(lstMistake) != 0:
                intMistake = randint(0,
                                     len(lstMistake) - 1)
                intItem = lstMistake[intMistake]
                lstMistake.remove(intItem)
            else:
                intItem = randint(0,
                                  len(lstStudy) - 1)
            if intItem not in lstItems:
                lstItems.append(intItem)
                # append to lstItems so that a character can only be questioned once
                strPaddedItem = get_padded_item(lstStudy[intItem][0])
                # lstStudy[intItem] identifies tuple from lstStudy; [0] shows character (e.g. "え") from that tuple
                print("Lesson {} of {}: [ {} ] has the sound: {}".format(str(intStudy),
                                                                         str(intStudyLen),
                                                                         strPaddedItem,
                                                                         lstStudy[intItem][1]))
                intStudy += 1
        display_menu()

# Test: random items from lstMistake before random items from lstTest
def perform_test(intMenuChoice,
                 lstTest):
                 # lstTest is copy of either lstHiragana or lstKatakana
    clear_screen()
    intCorrect = 0
    intQuestion = 1
    intTest = get_item_limit()
    lstRight= file_load(intMenuChoice,
                        "Right")
    lstWrong = file_load(intMenuChoice,
                         "Wrong")
    lstLearned = file_load(intMenuChoice,
                           "Learned")
    lstMistake = get_mistakes(lstWrong)
    lstItems = lstLearned[:]
    # copy lstLearned into lstItems so that learned items are not tested
    strCharacterSet = get_character_set(intMenuChoice)
    # if all characters have been learned, then no need to test
    if len(lstLearned) == len(lstTest):
        print("\n" +
              "All characters for the test {} have been learned.".format(strCharacterSet))
        display_menu()
    else:
        intLenTest = len(lstTest) - len(lstLearned)
        # test consists of testable items which have not been learned
        # but, if fewer items than intTest (9) require testing,
        # then only test those; otherwise test full amount: intTest
        if intLenTest < intTest:
            intTestLen = intLenTest
        else:
            intTestLen = intTest
        print("You have learned {} out of {} {} characters.".format(str(len(lstLearned)),
                                                                    str(len(lstTest)),
                                                                    strCharacterSet))
        # loop while questions remain to be answered
        while intQuestion <= intTestLen:
            strCorrectAnswer = ""
            # If Mistakes are present, test them first, else random character from lstTest
            if len(lstMistake) != 0:
                intMistake = randint(0,
                                     len(lstMistake) - 1)
                intItem = lstMistake[intMistake]
                lstMistake.remove(intItem)
            else:
                intItem = randint(0,
                                  len(lstTest) - 1)
            if intItem not in lstItems:
                lstItems.append(intItem)
                # append to lstItems so that a character can only be tested once
                strPaddedItem = get_padded_item(lstTest[intItem][0])
                # lstTest[intItem] identifies tuple from lstTest; [0] shows character (e.g. "え") from that tuple
                strAnswer = input("\n" +
                                  "Question {} of {}: What is the sound of [ {} ]?: ".format(str(intQuestion),
                                                                                             str(intTestLen),
                                                                                             strPaddedItem,
                                                                                             lstTest[intItem][0]))
                strCorrectAnswer = lstTest[intItem][1]
                strAnswer = strAnswer.lower()
                if strAnswer == strCorrectAnswer:
                    print("Correct")
                    lstRight.append(intItem)
                    # if character has been correct several times (set from get_item_count), then add it to learned list
                    intItemRightCount = get_item_count()
                    if lstRight.count(intItem) == intItemRightCount:
                        lstLearned.append(intItem)
                        print("Character {} has been added to the Learned list.".format(lstTest[intItem][0]))
                        # Once character is learned, remove it from lstWrong; thus, mistakes decrease.
                        while intItem in lstWrong:
                            lstWrong.remove(intItem)
                    intCorrect += 1
                else:
                    print("Incorrect. The correct answer is: {}".format(strCorrectAnswer))
                    # Append intItem to lstWrong
                    lstWrong.append(intItem)
                    # Remove all occurrences of intItem from lstRight; e.g. if "i" is answered for "え",
                    # then (all) "え" is removed; lstTest[intItem][0]
                    while intItem in lstRight:
                        lstRight.remove(intItem)
                    # Remove all occurrences of strAnswer from lstRight; e.g. if "i" is answered for "え",
                    # then (all) "い" is removed; lstTest[lstTest.index(value)][0]
                    for value in lstTest:
                        if value[1] == strAnswer:
                        # value[1] is a sound from the tuple (e.g. "i")
                            while lstTest.index(value) in lstRight:
                            # index(value) is the corresponding index for that tuple
                                lstRight.remove(lstTest.index(value))
                    # Remove all occurrences of strAnswer from lstLearned; e.g. if "i" is answered for "え",
                    # then (all) "い" is removed
                    for value in lstTest:
                        if value[1] == strAnswer: # value[1] is a sound from the tuple (e.g. "i")
                            while lstTest.index(value) in lstLearned:
                            # index(value) is the corresponding index for that tuple
                                lstLearned.remove(lstTest.index(value))
                                print("Character {} has been removed from the Learned list."
                                      .format(lstTest[lstTest.index(value)][0]))
                intQuestion += 1
        print()
        file_save(intMenuChoice,
                  "Right",
                  lstRight)
        file_save(intMenuChoice,
                  "Wrong",
                  lstWrong)
        file_save(intMenuChoice,
                  "Learned",
                  lstLearned)
        display_result(intTestLen,
                       intCorrect)

# Menu Items
lstMenu = []
lstMenu.append("1. Study Hiragana")
lstMenu.append("2. Study Katakana")
lstMenu.append("3. Test Hiragana")
lstMenu.append("4. Test Katakana")
lstMenu.append("5. Clear Progress Hiragana")
lstMenu.append("6. Clear Progress Katakana")
lstMenu.append("7. Exit")

lstHiragana = [
                (u"\u3042", "a"), (u"\u3044", "i"), (u"\u3046", "u"), (u"\u3048", "e"), (u"\u304A", "o"),
                (u"\u304B", "ka"), (u"\u304D", "ki"), (u"\u304F", "ku"), (u"\u3051", "ke"), (u"\u3053", "ko"),
                (u"\u3055", "sa"), (u"\u3057", "shi"), (u"\u3059", "su"), (u"\u305B", "se"), (u"\u305D", "so"),
                (u"\u305F", "ta"), (u"\u3061", "chi"), (u"\u3064", "tsu"), (u"\u3066", "te"), (u"\u3068", "to"),
                (u"\u306A", "na"), (u"\u306B", "ni"), (u"\u306C", "nu"), (u"\u306D", "ne"), (u"\u306E", "no"),
                (u"\u306F", "ha"), (u"\u3072", "hi"), (u"\u3075", "fu"), (u"\u3078", "he"), (u"\u307B", "ho"),
                (u"\u307E", "ma"), (u"\u307F", "mi"), (u"\u3080", "mu"), (u"\u3081", "me"), (u"\u3082", "mo"),
                (u"\u3084", "ya"), (u"\u3086", "yu"), (u"\u3088", "yo"),
                (u"\u3089", "ra"), (u"\u308A", "ri"), (u"\u308B", "ru"), (u"\u308C", "re"), (u"\u308D", "ro"),
                (u"\u308F", "wa"), (u"\u3092", "wo"),
                (u"\u3093", "n"),
                (u"\u304C", "ga"), (u"\u304E", "gi"), (u"\u3050", "gu"), (u"\u3052", "ge"), (u"\u3054", "go"),
                (u"\u3056", "za"), (u"\u3058", "ji"), (u"\u305A", "zu"), (u"\u305C", "ze"),  (u"\u305E", "zo"),
                (u"\u3060", "da"), (u"\u3067", "de"), (u"\u3069", "do"),
                (u"\u3070", "ba"), (u"\u3073", "bi"), (u"\u3076", "bu"), (u"\u3079", "be"), (u"\u307C", "bo"),
                (u"\u3071", "pa"), (u"\u3074", "pi"), (u"\u3077", "pu"), (u"\u307A", "pe"), (u"\u307D", "po"),
                (u"\u304D" + u"\u3083", "kya"), (u"\u304D" + u"\u3085", "kyu"), (u"\u304D" + u"\u3087", "kyo"),
                (u"\u3055" + u"\u3083", "sha"), (u"\u3059" + u"\u3085", "shu"), (u"\u305D" + u"\u3087", "sho"),
                (u"\u305F" + u"\u3083", "cha"), (u"\u3064" + u"\u3085", "chu"), (u"\u3068" + u"\u3087", "cho"),
                (u"\u306A" + u"\u3083", "nya"), (u"\u306C" + u"\u3085", "nyu"), (u"\u306E" + u"\u3087", "nyo"),
                (u"\u306F" + u"\u3083", "hya"), (u"\u3075" + u"\u3085", "hyu"), (u"\u307B" + u"\u3087", "hyo"),
                (u"\u307E" + u"\u3083", "mya"), (u"\u3080" + u"\u3085", "myu"), (u"\u3082" + u"\u3087", "myo"),
                (u"\u3089" + u"\u3083", "rya"), (u"\u308B" + u"\u3085", "ryu"), (u"\u308D" + u"\u3087", "ryo")
                # (u"\u3090", "wi"), (u"\u3091", "we"),
                # (u"\u3094", "vu"),
                # (u"\u3062", "di"), (u"\u3065", "du")
              ]

lstKatakana = [
                (u"\u30A2", "a"), (u"\u30A4", "i"), (u"\u30A6", "u"), (u"\u30A8", "e"), (u"\u30AA", "o"),
                (u"\u30AB", "ka"), (u"\u30AD", "ki"), (u"\u30AF", "ku"), (u"\u30B1", "ke"), (u"\u30B3", "ko"),
                (u"\u30AC", "ga"), (u"\u30AE", "gi"), (u"\u30B0", "gu"), (u"\u30B2", "ge"), (u"\u30B4", "go"),
                (u"\u30B5", "sa"), (u"\u30B7", "shi"), (u"\u30B9", "su"), (u"\u30BB", "se"), (u"\u30BD", "so"),
                (u"\u30BF", "ta"), (u"\u30C1", "chi"), (u"\u30C4", "tsu"), (u"\u30C6", "te"), (u"\u30C8", "to"),
                (u"\u30CA", "na"), (u"\u30CB", "ni"), (u"\u30CC", "nu"), (u"\u30CD", "ne"), (u"\u30CE", "no"),
                (u"\u30CF", "ha"), (u"\u30D2", "hi"), (u"\u30D5", "fu"), (u"\u30D8", "he"), (u"\u30DB", "ho"),
                (u"\u30DE", "ma"), (u"\u30DF", "mi"), (u"\u30E0", "mu"), (u"\u30E1", "me"), (u"\u30E2", "mo"),
                (u"\u30E4", "ya"), (u"\u30E6", "yu"), (u"\u30E8", "yo"),
                (u"\u30E9", "ra"), (u"\u30EA", "ri"), (u"\u30EB", "ru"), (u"\u30EC", "re"), (u"\u30ED", "ro"),
                (u"\u30EF", "wa"), (u"\u30F2", "wo"),
                (u"\u30F3", "n"),
                (u"\u30B6", "za"), (u"\u30B8", "ji"), (u"\u30BA", "zu"), (u"\u30BC", "ze"), (u"\u30BE", "zo"),
                (u"\u30C0", "da"), (u"\u30C7", "de"), (u"\u30C9", "do"),
                (u"\u30D0", "ba"), (u"\u30D3", "bi"), (u"\u30D6", "bu"), (u"\u30D9", "be"), (u"\u30DC", "bo"),
                (u"\u30D1", "pa"), (u"\u30D4", "pi"), (u"\u30D7", "pu"), (u"\u30DA", "pe"), (u"\u30DD", "po"),
                (u"\u30AB" + u"\u30E3","kya"), (u"\u30AD" + u"\u30E5","kyu"), (u"\u30AD" + u"\u30E7", "kyo"),
                (u"\u30B5" + u"\u30E3","sha"), (u"\u30B9" + u"\u30E5","shu"), (u"\u30BD" + u"\u30E7", "sho"),
                (u"\u30BF" + u"\u30E3","cha"), (u"\u30C4" + u"\u30E5","chu"), (u"\u30C8" + u"\u30E7", "cho"),
                (u"\u30CA" + u"\u30E3","nya"), (u"\u30CC" + u"\u30E5","nyu"), (u"\u30CE" + u"\u30E7", "nyo"),
                (u"\u30CF" + u"\u30E3","hya"), (u"\u30D5" + u"\u30E5","hyu"), (u"\u30DB" + u"\u30E7", "hyo"),
                (u"\u30DE" + u"\u30E3","mya"), (u"\u30E0" + u"\u30E5","myu"), (u"\u30E2" + u"\u30E7", "myo"),
                (u"\u30E9" + u"\u30E3","rya"), (u"\u30EB" + u"\u30E5","ryu"), (u"\u30ED" + u"\u30E7", "ryo")
                # (u"\u30F0", "wi"), (u"\u30F1", "we"),
                # (u"\u30F4", "vu"),
                # (u"\u30C2", "di"), (u"\u30C5", "du")
              ]


clear_screen()
intMenuChoice = 0
display_menu()
intFirstMenuItem = int(lstMenu[0][0])
# lstMenu[0] shows first entry in lstMenu;
# [0] shows first character from left of that entry
intLastMenuItem = int(lstMenu[-1][0])
# lstMenu[-1] shows last entry in lstMenu;
# [0] shows first character from left of that entry
while intMenuChoice != intLastMenuItem:
    try:
        intMenuChoice = int(input("\n" +
                                  "Enter a choice from the Menu: "))
        if intMenuChoice == 1:
            perform_study(intMenuChoice,
                          copy.deepcopy(lstHiragana))
        elif intMenuChoice == 2:
            perform_study(intMenuChoice,
                          copy.deepcopy(lstKatakana))
        elif intMenuChoice == 3:
            perform_test(intMenuChoice,
                         copy.deepcopy(lstHiragana))
        elif intMenuChoice == 4:
            perform_test(intMenuChoice,
                         copy.deepcopy(lstKatakana))
        elif intMenuChoice == 5:
            clear_progress(intMenuChoice)
        elif intMenuChoice == 6:
            clear_progress(intMenuChoice)
        elif intMenuChoice != intLastMenuItem:
            display_error_outside_range(intFirstMenuItem,
                                        intLastMenuItem)
    except ValueError:
        display_error_value(intFirstMenuItem,
                            intLastMenuItem)
print()

# new option 7: Preference
# load preference file (create blank if does ot exist)
