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

def readLeftbracket(line,index):
    # ( を読み込む関数
    token = {'type': 'LEFT'}
    return token, index + 1

def readRightbracket(line,index):
    # ) を読み込む関数
    token = {'type': 'RIGHT'}
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
        elif line[index] == '(':
            (token, index) = readLeftbracket(line, index)
        elif line[index] == ')':
            (token, index) = readRightbracket(line, index)
        else:
            print('Invalid character found: ' + line[index])
            exit(1)
        tokens.append(token)
    return tokens

def make_brackets_dict(tokens):
    '''
    括弧のindexを記録した辞書を作る関数
    括弧が重なった時、内側にある括弧ほど優先順位が高いので、
    key : 外側殻数えて何層目の括弧かを表す数
    value : [(左のカッコのindex、右のカッコのindex)] (同じ層にある括弧が複数個ある場合は、随時appendしていく)
    という形にして作った辞書を返すことで、このあとの処理の順番がわかるようにする
    '''
    brackets_dict = {}
    
    index = 0
    left_lst = [] # 括弧の左側が見つかったときのindexを格納していくリスト
    highest = 0 # 括弧は最大で何重になっているのかを表す数
    while index < len(tokens):
        if tokens[index]['type'] == 'LEFT':
            left_lst.append(index)
        elif tokens[index]['type'] == 'RIGHT':
            left_index = left_lst.pop(-1) # 括弧の右側が出てきたとき、対応する左側は、そこまでで最も後に登場した括弧なので、リストの最後の要素をとりだせばよい
            right_index = index
            key = len(left_lst) + 1 # その括弧が外側からいくつめの括弧なのかは、ペアの右側が見つからずにリストに残っている左側の数+1
            if brackets_dict.get(key) == None:
                brackets_dict[key] = [(left_index,right_index)]
            else:
                brackets_dict[key].append((left_index,right_index))
            if key > highest:
                highest = key
        index += 1

    return brackets_dict

def calculate_digits_in_brackets():
    '''
    make_brackets_dict関数で得られた辞書をもとに、
    優先順位の高い括弧の中から計算し、tokensを括弧内の計算を全て終えた状態にして返す関数
    '''
    return 0

def mul_and_div(tokens):
    '''
    tokensを、掛け算と割り算を終えた状態に更新して返す関数

    たとえば、
    3 + 2 * 5　だったら、
    tokens : [{'type': 'NUMBER', 'number': 3},{'type': 'PLUS'},{'type': 'NUMBER', 'number': 2},{'type': 'MULTIPLY'},{'type': 'NUMBER', 'number': 5}]
    となっているところを、

    3 + 7　の状態に処理して、すなわち
    tokens : [{'type': 'NUMBER', 'number':3},{'type': 'PLUS'},{'type': 'NUMBER', 'number': 7}]

    にして返す
    '''
    index = 1
    new_tokens = [tokens[0]]
    while index < len(tokens):
        if tokens[index]['type'] == 'MULTIPLY':
            # 負の数に対応、掛ける数が負の数だった場合、*の次に-がくるので、-1倍する
            if tokens[index+1]['type'] == 'MINUS':
                new_tokens[-1]['number'] *= -1
                # -の次の数が欲しいのでindexを１増やす
                index += 1
            # new_tokensに格納された最後の数（直前の数）に対して、*(or *-)の次にある数を掛ける
            new_tokens[-1]['number'] *= tokens[index+1]['number']
            # 上式でindex番目の数を掛ける数として処理したので、その分indexを増加
            index += 1
        elif tokens[index]['type'] == 'DEVIDE':
            # 負の数に対応、割る数が負の数だった場合、/の次に-がくるので、-1倍する
            if tokens[index+1]['type'] == 'MINUS':
                new_tokens[-1]['number'] *= -1
                # -の次の数が欲しいのでindexを１増やす
                index += 1
            # new_tokensに格納された最後の数（直前の数）に対して、/(or /-)の次にある数で割る
            new_tokens[-1]['number'] /= tokens[index+1]['number']
            # 上式でindex番目の数を割る数として処理したので、その分indexを増加
            index += 1
        # 足し算引き算、あるいは数はそのまま格納していく
        elif tokens[index]['type'] in ['NUMBER','PLUS','MINUS']:
            new_tokens.append(tokens[index]) 
        else:
            print('Invalid syntax')
            print(index)
            exit(1)
        index += 1   
    return new_tokens

def plus_and_minus(tokens):
    '''
    掛け算と割り算を終えた状態のtokensに対して、
    残っている足し算と引き算を実行して、
    最終的な計算結果を返す関数
    '''
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
            # 一周目は掛け算・割り算を計算
            tokens = mul_and_div(tokens)
        else:
            # 二周目は足し算・引き算を計算
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