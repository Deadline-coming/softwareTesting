#创建房间
def test_creatroom1():
    assert (create_room('')==False)

def test_creatroom2():
    assert (create_room('    ') == False)

def test_creatroom3():
    assert (create_room('蔡徐坤粉丝俱乐部') != False)
#房间重命名
def test_rename1():
    assert(rename_room('10000','')==False)

def test_rename2():
    assert(rename_room('2014','')==False)

def test_rename3():
    assert(rename_room('10000','ikun')==False)

def test_rename4():
    assert(rename_room('2014','ikun')==True)
#注册

def test_reg1():
    assert(register('阿信','')==False)
#用户名不存在，密码为空
def test_reg2():
    assert(register('刘畅','')==False)
#用户名存在，密码为空
def test_reg3():
    assert(register('坤坤','123456')==True)
#用户名不存在，密码不为空
def test_reg4():
    assert(register('刘畅','123456')==False)
#登陆

def test_log1():
    assert(login('吴京','')==False)
#用户名不存在
def test_log2():
    assert(login('刘畅','123456')==False)
#用户名存在，密码错误
def test_log3():
    assert(login('刘畅','liuchang')==True)
#用户名存在，密码正确

#绑定QQ
def test_qq1():
    assert(binding_qq('周董','')==False)
#用户名不存在，QQ为空
def test_qq2():
    assert(binding_qq('刘畅','')==False)
#用户名存在，QQ为空
def test_qq3():
    assert(binding_qq('周董','123456')==False)
#用户名不存在，QQ不为空
def test_qq4():
    assert(binding_qq('刘畅','123456')==True)
# 用户名存在，QQ不为空

#获取用户歌单
def test_songlist1():
    assert (songlist_test('吴亦凡')==False)
#用户不存在

def test_songlist2():
    assert (songlist_test('刘畅')!=False)
#用户存在

#边界值测试，top歌曲
def test_top2():
    assert(get_top(1)!=False)
def test_top3():
    assert(get_top(2)!=False)
def test_top4():
    assert(get_top(25)!=False)
def test_top5():
    assert(get_top(49)!=False)
def test_top6():
    assert(get_top(50)!=False)

#添加歌曲到歌单
def test_add1():
    assert add_to('刘畅','0039MnYb0qxYhV')==True
#用户名存在，未添加
def test_add2():
    assert add_to('金大大','0039MnYb0qxYhV')==False
#用户名不存在
def test_add3():
    assert add_to('刘畅','0039MnYb0qxYhV')==False
#用户名存在，已添加

#查找歌词
#存在歌曲id
def test_Ly():
    assert getLyric('0039MnYb0qxYhV')!=False
    #无效歌曲id
def test_Ly2():
    assert getLyric('00300000000000')==False
