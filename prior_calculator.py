# 함수 재활용
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # 0으로 나누는 경우 예외 처리
    if b == 0:
        print("Error: Division by zero.")
        return None
    return a / b

# 연산자 우선순위 정의 (숫자가 높을수록 우선순위가 높음)
precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# 연산자와 함수 매핑
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

# 숫자인지 여부를 확인하는 함수 (토큰 단위)
def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

# 중위 표기식을 후위 표기식으로 변환하는 함수 (Shunting Yard 알고리즘)
def infix_to_postfix(tokens):
    output = []  # 출력 큐
    stack = []   # 연산자 스택

    for token in tokens:
        if is_number(token):
            output.append(token)  # 숫자는 그대로 출력
        elif token in precedence:
            # 우선순위 높은 연산자는 스택에서 꺼내 출력
            while (stack and stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)  # 여는 괄호는 무조건 스택에 push
        elif token == ')':
            # 닫는 괄호를 만나면 여는 괄호를 만날 때까지 pop 함
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack:
                print("Invalid input.")  # 여는 괄호가 없을 때 출력 (예외 처리)
                return None
            stack.pop()  # 여는 괄호 제거 (
        else:
            print("Invalid input.")  # 허용되지 않은 토큰인 경우임 (예외 처리)
            return None

    # 남아 있는 연산자 모두 출력
    while stack:
        if stack[-1] in '()':  # 괄호가 남아있으면 오류
            print("Invalid input.")
            return None
        output.append(stack.pop())

    return output

# 후위 표기식 계산 함수
def evaluate_postfix(postfix_tokens):
    stack = []  # 계산용 스택

    for token in postfix_tokens:
        if is_number(token):
            stack.append(float(token))  # 숫자는 push
        elif token in operations:
            if len(stack) < 2:
                print("Invalid input.")  # 피연산자가 부족함
                return None
            b = stack.pop()
            a = stack.pop()
            result = operations[token](a, b)
            if result is None:  # 나눗셈 에러 등
                return None
            stack.append(result)
        else:
            print("Invalid input.")  # unexpected 토큰이 있을 때 출력 (예외 처리)
            return None

    if len(stack) != 1:  # 결과가 하나가 아니면 출력 (예외 처리)
        print("Invalid input.")
        return None

    return stack[0]

# 메인 실행 함수
def main():
    expr = input("Enter expression: ").strip()

    if not expr:
        print("Invalid input.")
        return

    tokens = expr.split()  # 띄어쓰기 기준으로 토큰 분리

    postfix = infix_to_postfix(tokens)
    if postfix is None:
        return  # 변환 실패 시 종료

    result = evaluate_postfix(postfix)
    if result is not None:
        print(f"Result: {result}")

# 프로그램 실행 진입점
if __name__ == "__main__":
    main()
