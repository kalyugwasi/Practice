import re
def count_tokens(code):
    token_pattern = (
        r'"[^*]*"|'      #checks all ""     
        r'\b\d+\b|'      #checks all numbers  
        r'\b[a-zA-Z_]\w*\b|' #checks all words
        r'[+\-*/%=;]'     #checks all symbols
    )
    tokens = re.findall(token_pattern, code)
    return len(tokens), tokens

fode = "x=y+3;"
code = 'x="y+3";'

count, token_list = count_tokens(fode)
print("Tokens:", token_list," =", count)
count, token_list = count_tokens(code)
print("Tokens:", token_list," =", count)


