HAI 1.2
BTW This is a test file for basic operations in LOLCODE

BTW Variable declarations and assignments
I HAS A number ITZ 143
I HAS A string ITZ "HELLO WORLD"
I HAS A flag ITZ WIN

BTW Print variables
VISIBLE SMOOSH "The number is: " AN number MKAY
VISIBLE SMOOSH "The string is: " AN string MKAY

BTW Handle boolean printing
BOTH SAEM flag AN WIN, O RLY?
    YA RLY
        VISIBLE "The boolean is: WIN"
    NO WAI
        VISIBLE "The boolean is: FAIL"
OIC

BTW Arithmetic operations
I HAS A sum ITZ SUM OF number AN 1
I HAS A difference ITZ DIFF OF number AN 2
I HAS A product ITZ PRODUKT OF number AN 2
I HAS A quotient ITZ QUOSHUNT OF number AN 5
I HAS A remainder ITZ MOD OF number AN 5

VISIBLE SMOOSH "Sum: " AN sum MKAY
VISIBLE SMOOSH "Difference: " AN difference MKAY
VISIBLE SMOOSH "Product: " AN product MKAY
VISIBLE SMOOSH "Quotient: " AN quotient MKAY
VISIBLE SMOOSH "Remainder: " AN remainder MKAY

BTW Math with variables
I HAS A result ITZ SUM OF product AN difference
VISIBLE SMOOSH "Result of product + difference: " AN result MKAY

BTW Variable reassignment
number R 100
VISIBLE SMOOSH "New number value: " AN number MKAY

BTW Basic boolean logic
I HAS A bool1 ITZ WIN
I HAS A bool2 ITZ FAIL

I HAS A andResult ITZ BOTH OF bool1 AN bool2
I HAS A orResult ITZ EITHER OF bool1 AN bool2
I HAS A notResult ITZ NOT bool2

BOTH SAEM andResult AN WIN, O RLY?
    YA RLY
        VISIBLE "AND result: WIN"
    NO WAI
        VISIBLE "AND result: FAIL"
OIC

BOTH SAEM orResult AN WIN, O RLY?
    YA RLY
        VISIBLE "OR result: WIN"
    NO WAI
        VISIBLE "OR result: FAIL"
OIC

BOTH SAEM notResult AN WIN, O RLY?
    YA RLY
        VISIBLE "NOT result: WIN"
    NO WAI
        VISIBLE "NOT result: FAIL"
OIC

KTHXBYE
