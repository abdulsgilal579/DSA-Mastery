"""
In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which,
for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. For example a "good" control string would
be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then
one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g.
aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a
string representing a rational whose numerator is the number of errors and the denominator the length of the control
string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

Examples:

"""

def printer_error(s):
    error_count = 0
    for character in s:
        if character < "a" or character > "m":
            error_count += 1
    return f"{error_count}/{len(s)}"

#Alternative Solution:

def printer_error(s):
    return "{}/{}".format(len([x for x in s if x not in "abcdefghijklm"]), len(s))