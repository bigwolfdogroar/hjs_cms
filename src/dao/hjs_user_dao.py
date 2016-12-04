# -*- coding: utf-8 -*-

# author: s0nnet
# time: 2016-11-08
# desc: tb_user_dao


'''
# 用户操作
CREATE TABLE `tb_user` (
`uid` int(10) NOT NULL AUTO_INCREMENT,
`username` varchar(50) NOT NULL,
`nickname` varchar(50) NOT NULL,
`password` varchar(50) NOT NULL,
`phone` varchar(50) DEFAULT NULL,
`email` varchar(50) DEFAULT NULL,
`privilege` int(1) NOT NULL DEFAULT '1',
`remark` text,
PRIMARY KEY (`uid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

if __name__ == "__main__":
    import sys

    sys.path.append("..")
    sys.path.append("../base")
    from hjs_cfg import *

from bs_util import *
from bs_database_pid import *


class HjsUserDao:
    
    @staticmethod
    def query_node_by_username(userName):
        dataBase = DataBase()
        sql = "select * from tb_user where username = %s"
        param = (userName, )

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet[0]


    @staticmethod
    def query_node_by_uid(uid):
        dataBase = DataBase()
        sql = "select * from tb_user where uid = %s"
        param = (uid, )

        bRet, sRet = dataBase.query_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet

    
    @staticmethod
    def query_node_user_list():
        dataBase = DataBase()
        sql = "select * from tb_user"

        bRet, sRet = dataBase.query_data(sql, None)
        if not bRet:
            return False, sRet
        
        return True, sRet


    @staticmethod
    def insert_node_user(userName, nickName, passWord, Phone, Priv):
        dataBase = DataBase()
        sql = "insert into tb_user(username, nickname, password, phone, priv) values(%s, %s, %s, %s, %s)"
        param = (userName, nickName, passWord, Phone, Priv)

        bRet, sRet = dataBase.insert_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet


    @staticmethod
    def delete_node_user(uid):
        dataBase = DataBase()
        sql = "delete from tb_user where uid = %s"
        param = (uid, )

        bRet, sRet = dataBase.delete_data(sql, param)
        if not bRet:
            return False, sRet
        
        return True, sRet








if __name__ == "__main__":
    #print HjsUserDao.query_node_by_username('admin')
    print HjsUserDao.query_node_user_list()

    pass