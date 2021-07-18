from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부

print(account_num)
print(accounts)
print(user_id)
print(user_name)
print(keyboard)
print(firewall)

#마켓 코드를 통한 코스피 코드리스트
kospi = kiwoom.GetCodeListByMarket('0') 
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi))
print(len(kosdaq))
print(len(etf))

name = kiwoom.GetMasterCodeName("005930") # 코드네임을 통한 종목명 얻기
print(name)

state = kiwoom.GetConnectState() # 서버 연결 상태 확인
if state == 0:
    print("미연결")
elif state == 1:
    print("연결완료")