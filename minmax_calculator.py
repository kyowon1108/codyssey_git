def main():
    try:
        input_str = input("Enter numbers separated by spaces: ")
        tokens = input_str.strip().split()

        numbers = []
        for token in tokens:
            number = float(token) # float로 숫자 지정
            numbers.append(number)

        if not numbers:
            print("Invalid input.") # 0개 입력시 예외 처리
            return

        min_value = numbers[0] # 초기화
        max_value = numbers[0]

        for num in numbers[1:]:
            if num < min_value:
                min_value = num # min_value보다 작은 경우 해당 num을 min_value로 지정
            if num > max_value:
                max_value = num # max_value보다 큰 경우 해당 num을 max_value로 지정

        print(f"Min: {min_value}, Max: {max_value}")

    except ValueError:
        print("Invalid input.") # 숫자가 아닌 것들이 들어온 경우 예외 처리

if __name__ == "__main__":
    main()
