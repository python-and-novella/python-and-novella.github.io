import hashlib
import datetime
#基于校验码的身份校验原型演示
#函数核心hashlib.sha3_512(''.encode()).hexdigest()
#生成校验码，基于有效期或权限
def get_checkcode(user_info:str)->str:
    return hashlib.sha3_512(user_info.encode()).hexdigest()
current_date = datetime.datetime.now().strftime('%Y%m%d')
#全部雇员信息
users_info = {
    'ABC000刘丽霞':{'access':'ZZZ','invalid_date':'20231221'},
    'ABC099李芳':{'access':'567','invalid_date':'30211231'},
    'ABC098李勇':{'access':'789','invalid_date':'30211231'},
    'ABC097李四':{'access':'234','invalid_date':'30211231'},
    'ABC000访客用户01':{'access':'999','invalid_date':current_date},
    'ABC000访客用户02':{'access':'888','invalid_date':current_date},
    'ABC000访客用户03':{'access':'777','invalid_date':current_date},
    'AAA000特权用户':{'access':'zzz','invalid_date':'99991231'}, 
    }
#根据用户信息+失效日期得到的校验码与用户基本信息的对应字典，每日更新，常用于访客和短期雇员，但也包含长期雇员
checkcode_user = { get_checkcode(i+users_info[i]['invalid_date']):i for i in users_info.keys() if users_info[i]['invalid_date']>=current_date}
#根据用户名得到的校验码与用户基本信息的对应字典，每周更新，用于长期雇员
checkcode_user2 = { hashlib.md5(i[6:].encode()).hexdigest():i for i in users_info.keys()}
print(checkcode_user.keys())
print(checkcode_user2.keys())
#检查权限
def check_access(checkcode:str,access_level='777')->bool:
    if len(checkcode) < 128:
        if checkcode not in checkcode_user2.keys():return False
        checkcode = get_checkcode((i:=checkcode_user2[checkcode])+users_info[i]['invalid_date'])
    if checkcode not in checkcode_user.keys():return False
    user_info = users_info[checkcode_user[checkcode]]
    access = user_info['access']
    res = [ i[2] for i in zip(access,access_level,['虹膜','人脸','指纹']) if  i[0]>=i[1]]
    res_required = [ i[2] for i in zip(access,access_level,['虹膜','人脸','指纹']) if  i[1]>'0' ]
    print('必须的权限验证方式为：',res_required)
    if res :
        print('可用的权限验证方式为：',res)
        return True
    else:
        return False
#检查有效期
def check_valid(checkcode:str)->bool:
    if len(checkcode) < 128:
        if checkcode not in checkcode_user2.keys():return False
        checkcode = get_checkcode((i:=checkcode_user2[checkcode])+users_info[i]['invalid_date'])
    if checkcode not in checkcode_user.keys():return False
    user_info = users_info[checkcode_user[checkcode]]
    invalid_date = user_info['invalid_date']
    global current_date
    if invalid_date == current_date:print('用户有效期已到期，请今天结束前更新校验码！')
    if invalid_date < current_date:return False
    return True
def main():
    checkcode = input('请扫码输入用户信息校验码:')[:]
    if check_access(checkcode,'077') and check_valid(checkcode):
        print('校验通过！请根据权限提示进行生物特征验证。')
    else:
        print('校验失败！请检查校验码是否合法，或联系管理员核实权限和身份有效期后更新用户信息校验码。')
    del checkcode  
    
if __name__ == '__main__':
    main()
