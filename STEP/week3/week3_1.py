def readNumber(line, index):
    number = 0
    while index < len(line) and line[index].isdigit():
        number = number * 10 + int(line[index])
        index += 1
    if index < len(line) and line[index] == '.':
        index += 1
        keta = 0.1
        while index < len(line) and line[index].isdigit():
            number += int(line[index]) * keta
            keta /= 10
            index += 1
    token = {'type': 'NUMBER', 'number': number}
    return token, index

def readPlus(line, index):
    token = {'type': 'PLUS'}
    return token, index + 1

def readMinus(line, index):
    token = {'type': 'MINUS'}
    return token, index + 1

def readMultiply(line,index):
    token = {'type': 'MULTIPLY'}
    return token, index + 1

def readDevide(line,index):
    token = {'type': 'DEVIDE'}
    return token, index + 1

def tokenize(line):
    tokens = []
    index = 0
    while index < len(line):
        if line[index].isdigit():
            (token, index) = readNumber(line, index)
        elif line[index] == '+':
            (token, index) = readPlus(line, index)
        elif line[index] == '-':
            (token, index) = readMinus(line, index)
        elif line[index] == '*':
            (token, index) = readMultiply(line, index)
        elif line[index] == '/':
            (token, index) = readDevide(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def mul_and_div(tokens):
    index = 1
    new_tokens = [tokens[0]]
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTIPLY':
            if tokens[index+1]['type'] == 'MINUS':
                new_tokens[-1]['number'] *= -1
                index += 1
            new_tokens[-1]['number'] *= tokens[index+1]['number']
            index += 1
        elif tokens[index]['type'] == 'DEVIDE':
            if tokens[index+1]['type'] == 'MINUS':
                new_tokens[-1]['number'] *= -1
                index += 1
            new_tokens[-1]['number'] /= tokens[index+1]['number']
            index += 1
        elif tokens[index]['type'] in ['NUMBER','PLUS','MINUS']:
            new_tokens.append(tokens[index]) 
        else:
            print('Invalid syntax')
            print(index)
            exit(1)
        index += 1   
    return new_tokens

def plus_and_minus(tokens):
    answer = 0
    index = 1
    new_tokens = [tokens[0]]
    while index < len(tokens):
        if tokens[index]['type'] == 'NUMBER':
            if tokens[index - 1]['type'] == 'PLUS':
                answer += tokens[index]['number']
            elif tokens[index - 1]['type'] == 'MINUS':
                answer -= tokens[index]['number']
            else:
                print('Invalid syntax')
                exit(1)
        index += 1
    return answer

def evaluate(tokens):
    tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
    for i in range(2):
        if i == 0:
            tokens = mul_and_div(tokens)
        else:
            answer = plus_and_minus(tokens)
    return answer

def test(line):
    tokens = tokenize(line)
    actualAnswer = evaluate(tokens)
    expectedAnswer = eval(line)
    if abs(actualAnswer - expectedAnswer) < 1e-8:
        print("PASS! (%s = %f)" % (line, expectedAnswer))
    else:
        print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))


# Add more tests to this function :)
def runTest():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    test("-1.5+2*10")
    test("3/-5+2*-4")
    test('-3+-4*5')
    test('-8+2/-4+5.5*2*-3*-3')
    print("==== Test finished! ====\n")

runTest()

while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    answer = evaluate(tokens)
    print("answer = %f\n" % answer)