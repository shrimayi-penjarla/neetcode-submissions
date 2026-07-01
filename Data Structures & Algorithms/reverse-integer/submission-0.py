class Solution:
    def reverse(self, x: int) -> int:
        output = ""
        sign = ""
        if x<0:
            sign = "-"
        if x==0:
            return 0
        converted = str(x)
        print(converted)
        if "-" in converted:
            converted = converted[1:]
            print(converted)
        rev = converted[::-1]
        index = 0
        leading_end = False
        while ( index<len(rev) and rev[index]=="0"):
            index+=1
        rev = rev[index:]
        output += sign + rev
        int_output = int(output)
        if (-2**31 <= int_output <= 2**31 - 1):
            return int_output
        return 0
            


        

    '''
    Understand
    input: signed 32-bit integer
    output: signed 32-bit integer
    edge cases: 
        x = 0: return 0
        x is negative: make sure to include negative sign in output
        leading zeros after reversing, so remove leading 0s in output
        x is out of range after reversing
    if reversing x makes the value go beyond [-2^31, 2^31 - 1], then return 0.

    Plan:
    make function reverse with input as int
    make a string called sign and if int is positive, keep it empty, and if negative, add a negative sign
    make an output string 
    make int into a string (remove negative sign if it's there using slicing)
    use the slicing shortcut to reverse string
    keep a counter string
    remove any leading 0s from string by going through the string and if the char you're at is 0, increment the loop to find the index where leading 0s stop then exit the loop then use slicing to reasign the portion of the string without leading 0s to the reverse string
    add sign string then reversed string to output string
    convert string into int 
    if int is not within range then return 0
    return int

    Implement: code

    '''
