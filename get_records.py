import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('sheetapi-edb6ae5e27c3.json', scope)
client = gspread.authorize(creds)

# 시트주소, 시트이름 지정 (api e-mail추가할 것)
sheetUrl = 'https://docs.google.com/spreadsheets/d/1s4Jq0JSf-FbpRMEB-gskN4wBcJSviRZUCYq48xMEtDE/edit#gid=119070282'
doc = client.open_by_url(sheetUrl)
sheet = doc.worksheet('Sheet2')

# https://gspread.readthedocs.io/en/latest/index.html

# cell value 불러오기 to list
cell_data = sheet.acell('B1').value
print(cell_data)

# row 불러오기 to list
row_data = sheet.row_values(2)
print(row_data)

# column 불러오기 to list
column_data = sheet.col_values(1)
print(column_data)

# 범위선택
range_list = sheet.range('A1:D5')
print(range_list)
# 범위에서 각 셀 값 가져오기
for cell in range_list:
    print(cell.value)

# cell 업데이트
sheet.update_acell('N1', 'N1 updated')

# row 추가
sheet.append_row(['new1', 'new2', 'new3', 'new4'])

# row 삽입
sheet.insert_row(['new1', 'new2', 'new3', 'new4'], 4)

# 크기조정
# sheet.resize(10,4)


# 문서생성
gs = client.create('new google sheet')

# 시트생성
worksheet = gs.add_worksheet(title='시트1', rows='1', cols='1')

# 공유, 소유권 부여
gs.share('wjpark11@gmail.com', perm_type='user', role='owner')