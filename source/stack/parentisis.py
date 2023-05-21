# from DSA.Stack import Stack
from Stack import Stack

paren = {'}':'{', ']':'[', ')':'('}

def isBalanced(str1):
    st = Stack()
    for i in str1:
        if i in paren.keys():
            if st.pop() != paren[i]:
                print(str1, "not balanced",st.toString())
                break
        else:
            st.push(i)

    if st.isEmpty():
        print(str1, "is balanced",st.toString())
    else:
        print(str1, "is not balanced", st.toString())

s1 = "{([])}()"
isBalanced(s1)