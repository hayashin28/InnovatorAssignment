from asyncio.log import logger


class Ex02:

    print('----------')

    #(1)
    '''
    整数値を入力しているため、numは数値型（int）
    '''
    try:
        num:int = 50
        var = 35 + num
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       

    #(2)
    '''
    数値型に文字列型（int）は代入できない
    ゆえに数値型へのキャストが必要
    '''
    try: 
        num += int('7')
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       

    #(3)
    '''
    文字列結合が行わてれいるため、文字列（str）型
    '''
    try:
        GROBAL:str = '世界' + str(num) + '箇国'
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       

    #(4)
    '''
    除算を行われているため、商は実数型（float）になる
    '''
    try:
        chech_code:int =  num * (9 / 3)
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       
    
    print('----------')
