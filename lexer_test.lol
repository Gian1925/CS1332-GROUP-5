BTW this file is a test for the lexer if it can return the tokens
BTW this is a comment, lexer should skip it
HAI
    I HAS A x
    I HAS A y
    I HAS A variable_name ITZ 5
    VISIBLE variable_name

    I HAS A another_variable ITZ "hello"
    VISIBLE another_variable
    VISIBLE "HELLO LORD" 


    BTW **Arithmetic operations:** `SUM OF`, `DIFF OF`, `PRODUKT OF`, `QUOSHUNT OF`, `MOD OF`, `BIGGR OF`, `SMALLR OF`
    I HAS A m ITZ 4
    I HAS A n ITZ 2
        VISIBLE SUM OF m AN n      BTW +
        VISIBLE DIFF OF m AN n     BTW -
        VISIBLE PRODUKT OF m AN n  BTW *
        VISIBLE QUOSHUNT OF m AN n BTW /
        VISIBLE MOD OF m AN n      BTW modulo
        VISIBLE BIGGR OF m AN n    BTW max
        VISIBLE SMALLR OF m AN n   BTW min

    BTW **Logical operations:** `BOTH SAEM`, `DIFFRINT`, `NOT`, `BOTH OF`, `EITHER OF`
    BTW WIN is true and FAIL is false
    I HAS A truth ITZ WIN
    VISIBLE truth

    VISIBLE BOTH SAEM 10 AN 10
    VISIBLE DIFFRINT "hello" AN "world"

    VISIBLE NOT WIN
    VISIBLE BOTH OF WIN AN FAIL
    VISIBLE EITHER OF WIN AN FAIL

    BTW **Conditional execution:** `O RLY?`, `YA RLY`, `NO WAI`, `OIC`
    O RLY?
        YA RLY
            VISIBLE "Inside if block"
        NO WAI
            VISIBLE "Inside else block"
    OIC

    I HAS A name ITZ A YARN BTW DECLARE A VARIABLE FOR LATER USE
    VISIBLE "TYPE SOMETHING AND ENTER"
    GIMMEH name BTW GET INPUT (STRING) INTO VARIABLE
    VISIBLE name

KTHXBYE
BTW This is a comment