#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by betalun on 4/4/17
from sqlalchemy import Column, String, create_engine,INT,DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base

session = None

def getSession():
    global session
    if not session:
        engine = create_engine('mysql+mysqlconnector://root:123456@localhost:3306/crawler')
        # 创建DBSession类型:
        session = sessionmaker(bind=engine)
    return session()

Base = declarative_base()

class CsdnGeek(Base):
    __tablename__ = 'csdn_geek'
    id = Column(INT, primary_key=True,autoincrement=True)
    refurl = Column(String(256))
    title = Column(String(256))
    keywords = Column(String(128))
    desc = Column(String(512))
    createTime = Column(DateTime)
