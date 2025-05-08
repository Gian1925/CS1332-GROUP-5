HAI 1.2
BTW This is a test file for I/O and conditionals in LOLCODE

BTW Say hello to the user
VISIBLE "PLEASE ENTER UR NAME: "
I HAS A userName
GIMMEH userName

BTW Basic conditional
BOTH SAEM userName AN "", O RLY?
    YA RLY
        VISIBLE "Y U NO ENTER NAME?"
    NO WAI
        VISIBLE SMOOSH "HAI " AN userName AN "! NICE 2 MEET U!" MKAY
OIC

BTW Get a number from the user
VISIBLE "GIMMEH NUMBER PLZ: "
I HAS A userNumber
GIMMEH userNumber

BTW Convert string to number
userNumber IS NOW A NUMBR

BTW More complex conditional
userNumber, WTF?
    OMG 42
        VISIBLE "U FOUND TEH ANSWER 2 LIFE, UNIVERSE AN EVERYTHIN!"
    OMG 0
        VISIBLE "Y U GIMMEH ZERO?!"
    OMG 1337
        VISIBLE "WOW, U R 1337 H4X0R!"
    OMGWTF
        BOTH SAEM BIGGR OF userNumber AN 100 AN userNumber, O RLY?
            YA RLY
                VISIBLE SMOOSH "BIG NUMBAR! " AN userNumber AN " > 100" MKAY
            NO WAI
                VISIBLE SMOOSH "SMOL NUMBAR! " AN userNumber AN " <= 100" MKAY
        OIC
OIC

BTW Looping example (count from 1 to 5)
I HAS A counter ITZ 1

IM IN YR loop UPPIN YR counter TIL BOTH SAEM counter AN 6
    VISIBLE SMOOSH "LOOP COUNTER: " AN counter MKAY
IM OUTTA YR loop

VISIBLE "KTHXBYE!"
KTHXBYE
