class Ex03:

    while True:

        try:
            print('BMIを求めます')
            cm:float = float(input('身長を入力してください（cm）：'))
            kg:float = float(input('体重を入力してください（kg）：'))
            bmi:float = kg / (cm * cm / 10000)
            print(f'あなたのBMIは{round(bmi, 2)}です')
        except Exception as e: 
            print(f'不正な処理を検知しました：{e}')       

        c:chr = ''
        while True:
            try:
                s:str = input('継続しますか？（y/n）：')
                c = s[0:1]
            except Exception as e:
                print(f'不正な処理を検知しました：{e}')       

            if (c == 'y' or c == 'n' or c == 'Y' or c == 'N'):
                break        
        
        if (c == 'n' or c == 'N'):
            break

    print('終了')