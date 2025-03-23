# フィボナッチ数列のうち、1000未満の数列を求める関数を作成してください。
def fibonacciUnder() -> list:
    numbers = [0, 1]
    while True:
        nextValue = numbers[-1] + numbers[-2]
        if nextValue >= 1000:
            break
        numbers.append(nextValue)
    return numbers

print(f'1000未満のフィボナッチ数列は{fibonacciUnder()}')


# フィボナッチ数列のひとつ前の値で割った数列を求める関数を作成してください。
def fibonacciRatios() -> list:
    fibSequence = fibonacciUnder()
    ratios = []
    for i in range(2, len(fibSequence)):
        ratios.append(fibSequence[i] / fibSequence[i - 1])
    return ratios

print(f'フィボナッチ数列のひとつ前の値で割った数列は{fibonacciRatios()}')


# フィボナッチ数列のひとつ前の値で割った数列を小数点第3位まで求める関数を作成してください。
def formattedFibonacciRatios() -> list:
    ratios = fibonacciRatios()
    formatted_ratios = [round(ratio, 3) for ratio in ratios]
    return formatted_ratios

print(f'フィボナッチ数列のひとつ前の値で割った数列（小数点第3位まで）は{formattedFibonacciRatios()}')