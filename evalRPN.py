class Solution:
    # @param tokens, a list of string
    # @return an integer
    def is_int(self, mysteryString):
        try:
            attempt = int(mysteryString)
            return True
        except ValueError:
            return False
    
    def evalRPN(self, tokens):
        tempList = list()
        result = 0
        inBetweener = 0
        for x in tokens:
            if self.is_int(x):
                tempList.append(x)
                result=int(x)
            elif x =='+':
                result=int(tempList.pop())+int(tempList.pop())
                tempList.append(result)
            elif x=='-':
                inBetweener=int(tempList.pop())
                result=int(tempList.pop())-inBetweener
                tempList.append(result)
            elif x=='*':
                result=int(tempList.pop())*int(tempList.pop())
                tempList.append(result)
            elif x=='/':
                inBetweener=int(tempList.pop())
                result=int(float(tempList.pop())/float(inBetweener))
                tempList.append(result)
            else: return 'Invalid Input'
        return result
