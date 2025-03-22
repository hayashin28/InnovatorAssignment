from datetime import datetime, timedelta
import ntplib
import sys


'''
NTPClientクラス (NTPClient.py)
NTPサーバーから時刻を取得するクラス (NTPClient) を定義します。
このクラスは、ntp.nict.jp というデフォルトのNTPサーバーから時刻を取得します。
getNowTimeメソッドは、NTPサーバーから取得した時刻を返します。
'''
class NTPClient:
    def __init__(self, ntp_server_host='ntp.nict.jp'):
        self.ntp_client = ntplib.NTPClient()
        self.ntp_server_host = ntp_server_host

    def getNowTime(self, timeformat='%Y-%m-%d %H:%M:%S')->str:
        try:
            response = self.ntp_client.request(self.ntp_server_host, version=3)
            nowtime = datetime.utcfromtimestamp(response.tx_time) + timedelta(hours=9)
            return nowtime.strftime(timeformat)
        except Exception as e:
            sys.exit(f"Error: {e}")
