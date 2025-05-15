import re
import base64

#本程序仅适用于敏感内容脱敏，不可用于非法用途

#核心函数，文字正常化punycode版本，可以自动识别编码前后的敏感词并自动转化
def normalize_puny(text:str)->str:
	if all(map(lambda x:x.isascii(),text)):return text.encode().decode('punycode')
	else: return str(text.encode('punycode'))[2:-1]

#核心函数，文字正常化base64版本，可以自动识别编码前后的敏感词并自动转化
def normalize_b64(text:str)->str:
	if all(map(lambda x:x.isascii(),text)):return base64.b64decode(text.encode()).decode()
	else: return str(base64.b64encode(text.encode()))[2:-1]

#核心函数，文字正常化base32版本，可以自动识别编码前后的敏感词并自动转化
def normalize_b32(text:str)->str:
	if all(map(lambda x:x.isascii(),text)):return base64.b32decode(text.encode()).decode()
	else: return str(base64.b32encode(text.encode()))[2:-1]

#核心函数，文字正常化base64版本，可以自动识别编码前后的敏感词并自动转化
def normalize_b16(text:str)->str:
	if all(map(lambda x:x.isascii(),text)):return base64.b16decode(text.encode()).decode()
	else: return str(base64.b16encode(text.encode()))[2:-1]

#字典映射函数，方便统一调用和后续扩展，三位数字、小写字母混合组成的正常化代码
normalize = {
    'pny':normalize_puny,
    'b64':normalize_b64,
    'b32':normalize_b32,
    'b16':normalize_b16   
    }

#TODO:
# 1,利用正则替换，识别{{敏感词}}或者{{zgu16gx17b}}，调用normalize来转化
# 2,支持将文件名作为参数自动处理整个文件
# 3,加入其他绕过敏感字检查的编码，并可以扩展简易加密算法来保护,防止自动识别
# 4,支持敏感词典，自动处理指定的敏感词
# 5,序列化敏感词，自动创建为一个绑定{序列号:敏感词}的敏感词数据库（SQLite），一对一解密。

if __name__ == '__main__':
    word = '敏感词'
    print('原文为:',word)
    print('Punycode脱敏结果为：',(words := normalize['pny'](word)),',原文还原结果为：',normalize['pny'](words))
    print('Base64脱敏结果为：',(words := normalize['b64'](word)),',原文还原结果为：',normalize['b64'](words))
    print('Base32脱敏结果为：',(words := normalize['b32'](word)),',原文还原结果为：',normalize['b32'](words))
    print('Base16脱敏结果为：',(words := normalize['b16'](word)),',原文还原结果为：',normalize['b16'](words))