#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from framework.CSingleton import CSingleton
from service.CSqlManager import CSqlManager
from service.data_base.canteen import UUserinfo, UType, UUserdetail

class CSvcEmployee(CSingleton):
    def __repr__(self):
        return '%s' % (self.__class__.__name__)

    @staticmethod
    def GetAll():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(UUserinfo).all()        

        index = 0
        data = list()
        for item in result:
            data.append([int(item.num_id), index, item.vch_name, item.num_userdetails.vch_realname, 
                         item.num_userdetails.dt_birthday, "", 
                         item.num_userdetails.u_dept.vch_name, int(item.num_userdetails.num_gender), 
                         int(item.num_userdetails.num_phone), item.num_userdetails.vch_idcard,
                         0, item.num_userdetails.vch_address,
                         item.num_userdetails.vch_email, item.num_userdetails.vch_memo])
            index += 1
            
        return data
    
    @staticmethod
    def GetItems():
        session = CSqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(UUserinfo).all()
        index = 0
        data = list()
        for item in result:
            data.append([int(item.num_id), index, item.vch_name, item.num_userdetails.vch_realname, 
                         item.num_userdetails.dt_birthday, "", 
                         item.num_userdetails.num_dept, int(item.num_userdetails.num_gender), 
                         int(item.num_userdetails.num_phone), item.num_userdetails.vch_idcard,
                         0, item.num_userdetails.vch_address,
                         item.num_userdetails.vch_email, item.num_userdetails.vch_memo])
            index += 1
            
        return data
    
    @staticmethod
    def AddItem(data):
        if not data:
            return
        
        user_details = UUserdetail()
        user_details.vch_realname = data[1]    
        user_details.vch_englishname = ""       
        user_details.dt_birthday = data[2]      
        user_details.num_dept = data[4]   
        user_details.num_gender = data[5]
        user_details.num_phone = data[6]
        user_details.vch_idcard = data[7]
        #user_details.num_status = data[8]
        user_details.vch_address = data[9]
        user_details.vch_email = data[10]
        user_details.vch_memo = data[11]

        session = CSqlManager.session
        session.add(user_details)
        session.flush()
        session.commit()
        
        user_info = UUserinfo()
        user_info.vch_name = data[0]
        user_info.vch_psw = "0000"
        li_id_item = session.query(UUserdetail.num_id).all()
        li_id = list()
        for id_itme in li_id_item:
            li_id.append(id_itme[0])
        user_info.num_userdetails_id = int(max(li_id))
        
        session.add(user_info)
        session.flush()
        session.commit()
        
    @staticmethod
    def DeleteItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(UUserinfo).filter(UUserinfo.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @staticmethod
    def UpdateItem(data):
        if not data:
            return
        
        session = CSqlManager.session
        session.query(UUserinfo).filter(UUserinfo.num_id == data[0]).update({UUserinfo.vch_name:data[1]})
                                           
        detail_id = session.query(UUserinfo.num_userdetails_id).filter(UUserinfo.num_id == data[0]).all()
        session.query(UUserdetail).filter(UUserdetail.num_id == int(detail_id[0][0])).update(
                                                                                                {UUserdetail.vch_realname:data[2],
                                                                                                 UUserdetail.dt_birthday:data[3],
                                                                                                 UUserdetail.num_dept:data[5],
                                                                                                 UUserdetail.num_gender:data[6],
                                                                                                 UUserdetail.num_phone:data[7],
                                                                                                 UUserdetail.vch_idcard:data[8],
                                                                                                 UUserdetail.vch_address:data[10],
                                                                                                 UUserdetail.vch_email:data[11],
                                                                                                 UUserdetail.vch_memo:data[12]
                                                                                                 })
        session.flush()
        session.commit()
