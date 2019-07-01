import SQLiteDB
import json

#注册用户
def register(username, password):
    if password == "":
        return False
    fetch_sql = "SELECT * FROM users WHERE username = '" + username + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) == 0:
        add_sql = '''INSERT INTO users values (?, ?, ?, ?, ?)'''
        data = [(username, password, '', username, ''),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.save(conn, add_sql, data)
        return True
    else:
        return False
# def test_reg1():
#     assert(register('阿信','')==False)
# #用户名不存在，密码为空
# def test_reg2():
#     assert(register('刘畅','')==False)
# #用户名存在，密码为空
# def test_reg3():
#     assert(register('坤坤','123456')==True)
# #用户名不存在，密码不为空
# def test_reg4():
#     assert(register('刘畅','123456')==False)
#用户名存在，密码不为空
#用户登录 
def login(username, password):
    fetch_sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) > 0:
        return True
    else:
        return False
# def test_log1():
#     assert(login('吴京','')==False)
# #用户名不存在
# def test_log2():
#     assert(login('刘畅','123456')==False)
# #用户名存在，密码错误
# def test_log3():
#     assert(login('刘畅','liuchang')==True)
# #用户名存在，密码正确

#设置用户头像
def update_profile(username, profile):
    fetch_sql = "SELECT * FROM users WHERE username = '" + username + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) > 0:
        update_sql = '''UPDATE users SET profile = ? WHERE username = ? '''
        data = [(profile, username),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.update(conn, update_sql, data)
        return True
    else:
        return False

#设置用户昵称
def update_nickname(username, nickname):
    fetch_sql = "SELECT * FROM users WHERE username = '" + username + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) > 0:
        update_sql = '''UPDATE users SET nickname = ? WHERE username = ? '''
        data = [(nickname, username),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.update(conn, update_sql, data)
        return True
    else:
        return False

#绑定QQ号
def binding_qq(username, qq_number):
    fetch_sql = "SELECT * FROM users WHERE username = '" + username + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) > 0:
        update_sql = '''UPDATE users SET qqnumber = ? WHERE username = ? '''
        data = [(qq_number, username),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.update(conn, update_sql, data)
        return True
    else:
        return False

# def test_qq1():
#     assert(binding_qq('周董','')==False)
# #用户名不存在，QQ为空
# def test_qq2():
#     assert(binding_qq('刘畅','')==False)
# #用户名存在，QQ为空
# def test_qq3():
#     assert(binding_qq('周董','123456')==False)
# #用户名不存在，QQ不为空
# def test_qq4():
#     assert(binding_qq('刘畅','123456')==True)
# # 用户名存在，QQ不为空

#获取用户歌单
def songlist_test(username):
    #username = input("请输入用户名：")
    count_sql = "SELECT count(*) FROM user_songs NATURAL JOIN songs WHERE username = '" + username + "'"
    fetchqq_sql = "SELECT qqnumber FROM users WHERE username = '" + username + "'"
    fetchall_sql = "SELECT songmid, songname, singers, albumname, albummid, interval, videoid, songid FROM user_songs NATURAL JOIN songs WHERE username = '" + username + "'"
    #count_sql = "SELECT count(*) FROM user_songs NATURAL JOIN song WHERE name = 'huangjinrong'"
    #fetchall_sql = "SELECT songid, songname, singers, albumname, albumid, interval FROM user_songs NATURAL JOIN song WHERE name = 'huangjinrong'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    num = SQLiteDB.fetchall(conn, count_sql)
    #print(num[0][0])
    qqnumber = SQLiteDB.fetchall(conn, fetchqq_sql)
    songs = SQLiteDB.fetchall(conn, fetchall_sql)
    songlist = []
    if len(songs) > 0:
        for i in range(len(songs)):
            song = {
                'songmid':songs[i][0],
                'songname':songs[i][1],
                'singers':songs[i][2],
                'album':songs[i][3],
                'albummid':songs[i][4],
                'interval':songs[i][5],
                'videoid':songs[i][6],
                'songid':songs[i][7]
            }
            songlist.append(song)
            #print(table[i])
    else:
        return False
    dic = {'num':num[0][0], 'songlist':songlist, 'qqnumber':qqnumber[0][0]}
    myjson = json.dumps(dic, ensure_ascii = False)
    # print(myjson)
    return myjson

# def test_songlist1():
#     assert (songlist_test('吴亦凡')==False)
# #用户不存在
#
# def test_songlist2():
#     assert (songlist_test('刘畅')!=False)
# #用户存在
#添加歌曲到用户歌单
def add_to(username, songmid):
    fetch_sql = "SELECT * FROM user_songs WHERE username = '" + username + "' AND songmid = '" + songmid + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) == 0:
        add_sql = '''INSERT INTO user_songs values (?, ?)'''
        data = [(songmid, username),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.save(conn, add_sql, data)
        return True
    else:
        return False
# def test_add1():
#     assert add_to('刘畅','0039MnYb0qxYhV')==True
# #用户名存在，未添加
# def test_add2():
#     assert add_to('金大大','0039MnYb0qxYhV')==False
#用户名不存在
# def test_add3():
#     assert add_to('刘畅','0039MnYb0qxYhV')==False
# #用户名存在，已添加

#添加歌曲到歌曲信息表    
def add_song_to(songname, songmid, interval, singers, album, albummid, videoid, songid):
    fetch_sql = "SELECT * FROM songs WHERE songmid = '" + songmid + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) == 0:
        add_sql = '''INSERT INTO songs values (?, ?, ?, ?, ?, ?, ?, ?)'''
        data = [(songmid, songname, singers, album, albummid, interval, videoid, songid),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.save(conn, add_sql, data)
        add_sql = '''INSERT INTO hotsongs values (?, ?)'''
        data = [(songmid, 1),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.save(conn, add_sql, data)
    else:
        pass

#从歌单中移除歌曲
def delete_from(username, songmid):
    fetch_sql = "SELECT * FROM user_songs WHERE username = '" + username + "' AND songmid = '" + songmid + "'"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    table = SQLiteDB.fetchall(conn, fetch_sql)
    if len(table) > 0:
        delect_sql = '''DELETE FROM user_songs WHERE username = ? AND songmid = ? '''
        data = [(username, songmid),]
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        SQLiteDB.update(conn, delect_sql, data)
        return True
    else:
        return False

#增加歌曲热门指数
def add_count(songmid):
    update_sql = "UPDATE hotsongs SET count = count + 1 WHERE songmid = ? "
    data = [(songmid,),]
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    SQLiteDB.update(conn, update_sql, data)

#返回热门歌曲
def get_top(num):
    count_sql = "SELECT count(*) FROM hotsongs"
    fetch_sql = "SELECT songmid FROM hotsongs ORDER BY count DESC"
    conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
    total = SQLiteDB.fetchall(conn, count_sql)
    if total[0][0] < num:
        number = total[0][0]
    else:
        number = num
    if number==0:
        return False;
    table = SQLiteDB.fetchmany(conn, fetch_sql, num)
    topsonglist = []
    for i in range(number):
        fetch_sql = "SELECT songmid, songname, singers, albumname, albummid, interval, videoid, songid FROM songs WHERE songmid = '" + table[i][0] + "'"
        conn = SQLiteDB.get_conn(SQLiteDB.UserDB_FILE_PATH)
        songs = SQLiteDB.fetchall(conn, fetch_sql)
        # print(songs)
        if len(songs) > 0:
            song = {
                'songmid':songs[0][0],
                'songname':songs[0][1],
                'singers':songs[0][2],
                'album':songs[0][3],
                'albummid':songs[0][4],
                'interval':songs[0][5],
                'videoid':songs[0][6],
                'songid':songs[0][7]
            }
            topsonglist.append(song)
    dic = {'num':number, 'songlist':topsonglist}
    myjson = json.dumps(dic, ensure_ascii = False)
    # print(myjson)
    return myjson

# #边界值测试，top歌曲
# def test_top2():
#     assert(get_top(1)!=False)
# def test_top3():
#     assert(get_top(2)!=False)
# def test_top4():
#     assert(get_top(25)!=False)
# def test_top5():
#     assert(get_top(49)!=False)
# def test_top6():
#     assert(get_top(50)!=False)

