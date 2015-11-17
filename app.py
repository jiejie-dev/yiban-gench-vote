from votelib import VoteHelper


handler = open('users.txt')
line = handler.readline()
while(line):
    print('正在通过用户·%s·进行投票' % line)
    helper = VoteHelper()
    helper.vote(line,"111111")
    line = handler.readline()

print('投票结束！')
input()
