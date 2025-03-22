from NTPClient import NTPClient
from datetime import datetime



# NTPClientクラスのインスタンスを生成します。
ntpClient:NTPClient = NTPClient()
# NTPサーバーから時刻を取得します。
ntpTime:str = ntpClient.getNowTime()
# NTPサーバーから取得した時刻とローカル時刻を表示します (JST)。
print(f"NTPサーバー時刻 (JST): {ntpTime}")

# NTPサーバーから取得した時刻の月を取得します。
mh:int = datetime.fromisoformat(ntpTime).month



month = [1, 3, 5, 7, 8, 10, 12] 
if mh in month:
    print(f"月の日数: 31日")
elif mh == 2:
    print(f"1年で一番寒い季節ですね。")
else:
    print(f"月の日数: 30日")



print('年が明けてから{}ヵ月が経過しました。'.format(mh))
