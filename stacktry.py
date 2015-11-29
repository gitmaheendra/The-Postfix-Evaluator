stack = []
def get_input():
    Token_list =raw_input("Enter the string")
    return Token_list

def push_n_pop(input_string):
    operators= ["+","-","*","/"]
    top= -1
    for input in input_string :
        if input in  "0123456789":
            stack.append(int(input))
        elif input in operators:
            operand2= stack.pop()
            operand1= stack.pop()
            operator= input
            call_calc= calc(operand2,operand1,operator)
            stack.append(call_calc)
        else:
            print "wrong symbol in the postfix expresssion"
           
    print stack 
        
def calc(var2,var1,operator):
    if operator in "*":
        return var1*var2
    elif operator in "/":
        return var1/var2
    elif operator in "+":
        return var1+var2
    elif operator in "-":
        return var1-var2
    else:
        print "wrong operator !!!!!"
        

token=get_input()
push_n_pop(token)

