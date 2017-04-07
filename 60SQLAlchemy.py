# -*- coding: utf-8 -*- 
from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///proxy.db',echo=True)
DBSession = sessionmaker(bind=engine)
#这里初始化一个ORM对象BASE，用于连接数据库，除了连接不同数据库写法不同，其余都是一样的

class proxy(Base):
    __tablename__ = 'proxy'
    ipaddr = Column(String,primary_key=True)
    port = Column(String)
    ishttp = Column(String)
    isTranspar = Column(String)
    zone = Column(String)

class status(Base):
    __tablename__ = 'status'
    ipaddr = Column(String,primary_key=True)
    site = Column(String)
    lag = Column(String)
    statu = Column(String)
    updatetime = Column(String)
#这里同样声明数据库类型，对已知的数据库，告知程序他的结构是怎样的
#一个表是一个类，表当中的字段名称为类定义的属性


session = DBSession()
new_proxy = proxy(ipaddr='10.166.1.37',port='8080',ishttp='http',isTranspar='高匿名',zone='中国')
session.add(new_proxy)
session.commit()
session.close()
#这里使用类来添加内容到数据库，语法如上

session = DBSession()
proxy_select = session.query(proxy).filter(proxy.ipaddr=='10.166.1.37').one()
print('type',type(proxy_select))
print('port',proxy_select.port)
session.close()
#查询内容
