from NumberRangeChecker import NumberRangeChecker

# うるう年判定を行うクラス
class Ex02:
    
    # うるう年判定を行うメソッド
    nrc:NumberRangeChecker = NumberRangeChecker(1900, 2500)
    
    while True:
        try:
            print('うるう年判定を行います。')
            year = int(input('西暦: '))
            if not nrc.is_within_range(year):
                print('正しい値を入力してください。')
            else:
                break
        except ValueError:
            print('数値を入力してください。')    
        
    # うるう年判定
    '''
    うるう年の条件(グレゴリオ暦):
    1. 西暦年が4で割り切れる年はうるう年
    2. 1の条件を満たしても100で割り切れる年は平年
    3. 2の条件を満たしても400で割り切れる年はうるう年
    例外: 1900年は平年だが、4で割り切れるためうるう年として判定される
    kokugo: うるう年は2月が29日まである年のことです。
    例: 2000年はうるう年です。2月29日まであります。
    ※ 400は100と4で割り切れることに注目
    '''    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(f'{year}年はうるう年です。') 
    else:
        print(f'{year}年は平年です。')
