def bubble_sort(arr): # 버블 정렬 함수
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def main():
    try:
        input_str = input("Enter numbers separated by spaces: ").strip()
        if not input_str:
            raise ValueError("Invalid input.") # 숫자 이외의 입력받은 것들 예외 처리
        
        tokens = input_str.split()
        numbers = []

        for token in tokens:
            num = float(token) # 입력받은 숫자 float로 처리
            numbers.append(num)

        bubble_sort(numbers) # numbers 버블 정렬

        sorted_str = ' '.join(str(float(num)) for num in numbers) # 띄어쓰기 join해서 정렬된 float 출력
        print(f"Sorted: {sorted_str}") # 모든 숫자 float로 출력

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
