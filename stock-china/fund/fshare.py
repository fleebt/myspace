# 本文件包装了tushare接口
# tushare接口地址
# https://tushare.pro/document/2

# 获取本地存储的tushare token
try:
    settingFile = open('/data/stock-setting.txt', 'r')
    settings = settingFile.read()
    token = settings.split()[0]
    secretUrl = settings.split()[1]
    settingFile.close()
except IOError:
    print('File is not accessible.')

# 获取tushare平台token
def getToken():
    return token

# 获取妖股助手的接口地址
def getSecretUrl():
    return secretUrl