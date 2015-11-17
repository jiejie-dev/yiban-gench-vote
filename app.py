from votelib import VoteHelper
import xlrd
import json
import datetime

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
        result = helper.vote(username,password)
        data_result[str(result)]=data_result[str(result)]+1
        print("data result %s" % data_result)

print('投票结束！')
print('成功投票：%s' % data_result['200'])
print('投票上线：%s' % data_result['204'])
print('重复投票：%s' % data_result['206'])
print('登录失败：%s' % data_result['211'])

fname = 'result-%s.txt' % datetime.datetime.now().strftime('%Y-%m-%d-%H-%m-%s')
print('本次批量投票操作的结果存放在：%s' % fname)
handler = open(fname, 'w')
handler.write(json.dumps(data_result,sort_keys=True,indent=4))
handler.close()

input()
