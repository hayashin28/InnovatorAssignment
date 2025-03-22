from asyncio.log import logger


class Ex01:

    print('----------')

    #(1)
    try:
        print(2 + 10 * 5) 
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       
        
    #(2)
    try: 
        print('7' * (3 + 4))
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       

    #(3)
    try: 
        print('version{}'.format(3 + 2 * 0.1 + 9 * 0.01))
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       

    #(4)
    try: 
        print(4 *'num' + '回目のTypeError')
    except Exception as e: 
        logger.error('エラーが発生しました：'.format(e))       
    
    print('----------')
