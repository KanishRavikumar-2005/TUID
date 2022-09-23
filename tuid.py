from base64 import encode
from datetime import datetime
from hashlib import *
from random_word import RandomWords

RAND = RandomWords()

def generate(seperator=False, sepstring="-", print_process=False):
    if print_process:
            print(f"\n>\tPROCESS PRINTING STARTS")
    RECORDING_DATE_TIME = datetime.now()
    if print_process:
        print(f">\tRECIVED DATE TIME [ {RECORDING_DATE_TIME} ]")
    DATE_TIME_EXPANDED = str(RECORDING_DATE_TIME).split()
    if print_process:
        print(f">\tSPLIT DATE TIME [ {DATE_TIME_EXPANDED} ]")
    COMBINED_U_LOCAL = ""

    for part in DATE_TIME_EXPANDED:
        HASH_PART = md5(part.encode()).hexdigest()
        if print_process:
            print(f">\tHASHED PART OF DATE TIME [ {HASH_PART} ]")
        COMBINED_U_LOCAL += str(HASH_PART)
        if print_process:
            print(f">\tJOINED TO COMBINED LOCAL [ {COMBINED_U_LOCAL} ]")

    RANDOM_WORD = RAND.get_random_word()
    if print_process:
        print(f">\tRECIVED RANDOM WORD [ {RANDOM_WORD} ]")
    if RANDOM_WORD == None:
        RANDOM_WORD = RAND.get_random_word()
        if print_process:
            print(f">\tRE-RECIEVED RANDOM WORD DUE TO NONE ERROR [ {RANDOM_WORD} ]")



    LOCAL_STR_VALUE = COMBINED_U_LOCAL+str(RANDOM_WORD)
    if print_process:
            print(f">\tCREATED LOCAL STRING [ {LOCAL_STR_VALUE} ]")

    END_TUID = sha256(LOCAL_STR_VALUE.encode('utf-8')).hexdigest()
    if print_process:
            print(f">\tCREATED UINQUE VALUE [ {END_TUID} ]")

    FINAL_RESULT = ""

    if seperator:
        sepstr = sepstring
        if print_process:
            print(f">\tSEPERATOR REQUESTED [ {sepstr} ]")
        F8 = END_TUID[:8]
        F6 = END_TUID[8:14]
        S6 = END_TUID[14:20]
        F4 = END_TUID[20:24]
        S4 = END_TUID[24:28]
        T4 = END_TUID[28:32]
        FO4 = END_TUID[32:36]
        T6 = END_TUID[36:42]
        FO6 = END_TUID[42:48]
        F16 = END_TUID[48:]
        FINAL_RESULT = F8+sepstr+F6+sepstr+S6+sepstr+F4+sepstr+S4+sepstr+T4+sepstr+FO4+sepstr+T6+sepstr+FO6+sepstr+F16
        if print_process:
            print(f">\tFINAL RESULT OUT-PUT [ {FINAL_RESULT} ]")

    else:
        FINAL_RESULT = END_TUID
        if print_process:
            print(f">\tFINAL RESULT OUT-PUT [ {FINAL_RESULT} ]")

    if print_process:
            print(f">\tPROCESS PRINTING ENDS\n\n")
    return FINAL_RESULT

print(generate(True, ";"))
