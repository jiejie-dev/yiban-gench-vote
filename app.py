from votelib import VoteHelper
import xlrd


xls_file_name = 'users.xls'
data = xlrd.open_workbook(xls_file_name)
data_result = {'200':0,'206':0,'211':0,'204':0}

for table_index in range(0,9):
    table = data.sheet_by_index(table_index)
    for i in range(2,table.nrows):
        username = str(table.cell(i,3).value).replace('.0','')
        password = str(table.cell(i,4).value).replace('.0','')

        print("[用户名：%s 密码: %s]" % (username, password))
        helper = VoteHelper()
        helper.vote(username,password)

print('投票结束！')
input()
