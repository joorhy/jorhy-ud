#!/usr/bin/env python
#_*_ encoding=utf-8 _*_

from framework.core import Singleton
from service.data_base.canteen import *


class SvcAreaSetting(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfoArea).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(TableInfoArea.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        table_info_area = TableInfoArea()
        table_info_area.vch_name = data[1]
            
        session = SqlManager.session
        session.add(table_info_area)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfoArea).filter(TableInfoArea.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfoArea).filter(TableInfoArea.num_id == data[0]).update({TableInfoArea.vch_name: data[1]})
        session.flush()
        session.commit()


class SvcCategorySetting(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishCategory).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(DishCategory.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        unit = DishCategory()
        unit.vch_name = data[1]
            
        session = SqlManager.session
        session.add(unit)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishCategory).filter(DishCategory.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishCategory).filter(DishCategory.num_id == data[0]).update({DishCategory.vch_name: data[1]})
        session.flush()
        session.commit()


class SvcDepartment(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(UDept).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(UDept.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        department = UDept()
        department.vch_name = data[1]
            
        session = SqlManager.session
        session.add(department)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(UDept).filter(UDept.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(UDept).filter(UDept.num_id == data[0]).update({UDept.vch_name: data[1]})
        session.flush()
        session.commit()


class SvcDishesInfo(Singleton):
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishPublish).all()   
                               
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), 
                         int(item.num_code),
                         item.vch_name, 
                         item.vch_spell,
                         item.num_spec.vch_name, 
                         item.dish_category.vch_name, 
                         int(item.num_default_price), 
                         item.unit.vch_name,
                         item.num_style.vch_name,
                         item.num_ticheng,
                         item.num_discount,
                         True,
                         item.vch_picname,
                         "" if item.num_printer_scheme is None else item.num_printer_scheme.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_items(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishPublish).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), 
                         int(item.num_code),
                         item.vch_name, 
                         item.vch_spell,
                         item.num_spec_id, 
                         item.num_category, 
                         int(item.num_default_price), 
                         item.num_unit,
                         item.num_style_id,
                         item.num_ticheng,
                         item.num_discount,
                         True,
                         item.vch_picname,
                         item.num_printer_scheme_id])
            index += 1
            
        return data
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        dish_publish = DishPublish()
        dish_publish.num_code = data[0]
        dish_publish.vch_name = data[1]
        dish_publish.vch_spell = data[2]
        dish_publish.num_spec_id = data[3]
        dish_publish.num_category = data[4]
        dish_publish.num_default_price = data[5]
        dish_publish.num_unit = data[6]
        dish_publish.num_style_id = data[7]
        dish_publish.num_ticheng = data[8]
        dish_publish.num_discount = data[9]
        dish_publish.vch_picname = data[11]
            
        session = SqlManager.session
        session.add(dish_publish)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishPublish).filter(DishPublish.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishPublish).filter(DishPublish.num_id == data[0]) \
            .update({DishPublish.num_code: data[1],
                     DishPublish.vch_name: data[2],
                     DishPublish.vch_spell: data[3],
                     DishPublish.num_spec_id: data[4],
                     DishPublish.num_category: data[5],
                     DishPublish.num_default_price: data[6],
                     DishPublish.num_unit: data[7],
                     DishPublish.num_style_id: data[8],
                     DishPublish.num_ticheng: data[9],
                     DishPublish.num_discount: data[10],
                     DishPublish.vch_picname: data[12],
                     DishPublish.num_printer_scheme_id: data[13]})
        session.flush()
        session.commit()
        
    @classmethod
    def update_print_scheme(cls, data):
        if not data:
            return
            
        session = SqlManager.session
        session.query(DishPublish).filter(DishPublish.num_id == data[0]) \
            .update({DishPublish.num_printer_scheme_id: data[1]})
        session.flush()
        session.commit()


class SvcDishSpec(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishSpec).all()
        data = list()
        for item in result:
            data.append([int(item.num_id), item.vch_name, int(item.num_price)])
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(DishSpec.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        dish_spec = DishSpec()
        dish_spec.vch_name = data[1]
        dish_spec.num_price = data[2]
            
        session = SqlManager.session
        session.add(dish_spec)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishSpec).filter(DishSpec.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishSpec).filter(DishSpec.num_id == data[0]).update({DishSpec.vch_name: data[1],
                                                                           DishSpec.num_price: data[2]})
        session.flush()
        session.commit()


class SvcDishStyle(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(DishStyle).all()
        data = list()
        for item in result:
            data.append([int(item.num_id), item.vch_name, int(item.num_priceadd), item.ch_mountadd])
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(DishStyle.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        dish_style = DishStyle()
        dish_style.vch_name = data[1]
        dish_style.num_priceadd = data[2]
        dish_style.ch_mountadd = data[3]
            
        session = SqlManager.session
        session.add(dish_style)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishStyle).filter(DishStyle.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(DishStyle).filter(DishStyle.num_id == data[0]).update({DishStyle.vch_name: data[1],
                                                                             DishStyle.num_priceadd: data[2],
                                                                             DishStyle.ch_mountadd: data[3]})
        session.flush()
        session.commit()


class SvcEmployee(Singleton):
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        session = SqlManager.session
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
    
    @classmethod
    def get_items(cls):
        session = SqlManager.session
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
    
    @classmethod
    def add_item(cls, data):
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

        session = SqlManager.session
        session.add(user_details)
        session.flush()
        session.commit()
        
        user_info = UUserinfo()
        user_info.vch_name = data[0]
        user_info.vch_psw = "0000"
        li_id_item = session.query(UUserdetail.num_id).all()
        li_id = list()
        for id_item in li_id_item:
            li_id.append(id_item[0])
        user_info.num_userdetails_id = int(max(li_id))
        
        session.add(user_info)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(UUserinfo).filter(UUserinfo.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(UUserinfo).filter(UUserinfo.num_id == data[0]).update({UUserinfo.vch_name: data[1]})
                                           
        detail_id = session.query(UUserinfo.num_userdetails_id).filter(UUserinfo.num_id == data[0]).all()
        session.query(UUserdetail).filter(UUserdetail.num_id == int(detail_id[0][0])) \
            .update({UUserdetail.vch_realname: data[2],
                     UUserdetail.dt_birthday: data[3],
                     UUserdetail.num_dept: data[5],
                     UUserdetail.num_gender: data[6],
                     UUserdetail.num_phone: data[7],
                     UUserdetail.vch_idcard: data[8],
                     UUserdetail.vch_address: data[10],
                     UUserdetail.vch_email: data[11],
                     UUserdetail.vch_memo: data[12]})
        session.flush()
        session.commit()


class SvcMinExpenseSetting(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfoMinexpense).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, int(item.num_amount)])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(TableInfoMinexpense.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        table_info_min_expense = TableInfoMinexpense()
        table_info_min_expense.vch_name = data[1]
        table_info_min_expense.num_amount = data[2]
            
        session = SqlManager.session
        session.add(table_info_min_expense)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfoMinexpense).filter(TableInfoMinexpense.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfoMinexpense).filter(TableInfoMinexpense.num_id == data[0]) \
            .update({TableInfoMinexpense.vch_name: data[1], TableInfoMinexpense.num_amount: data[2]})
        session.flush()
        session.commit()


class SvcPrinterScheme(Singleton):
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(PrinterScheme).all()   
                               
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, item.num_valid, 
                         item.printer_scheme_type.vch_name, int(item.num_print_count), u"无"])
            index += 1
            
        return data
    
    @classmethod
    def get_items(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(PrinterScheme).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, item.num_valid, 
                         int(item.num_bill_type), int(item.num_print_count), u"无"])
            index += 1
            
        return data
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        print_scheme = PrinterScheme()
        print_scheme.num_id = data[0]
        print_scheme.vch_name = data[1]
        print_scheme.num_valid = data[2]
        print_scheme.num_bill_type = data[3]
        print_scheme.num_print_count = data[4]
            
        session = SqlManager.session
        session.add(print_scheme)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(PrinterScheme).filter(PrinterScheme.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(PrinterScheme).filter(PrinterScheme.num_id == data[0]).\
            update({PrinterScheme.vch_name: data[1],
                    PrinterScheme.num_valid: data[2],
                    PrinterScheme.num_bill_type: data[3],
                    PrinterScheme.num_print_count: data[4]})
        session.flush()
        session.commit()


class SvcSchemeType(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(PrinterSchemeType).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(PrinterSchemeType.num_id).all()
        result.reverse()
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        scheme_type = PrinterSchemeType()
        scheme_type.vch_name = data[1]
            
        session = SqlManager.session
        session.add(scheme_type)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(PrinterSchemeType).filter(PrinterSchemeType.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(PrinterSchemeType).filter(PrinterSchemeType.num_id == data[0]) \
            .update({PrinterSchemeType.vch_name: data[1]})
        session.flush()
        session.commit()


class SvcTableInfo(Singleton):
    def __init__(self):
        pass

    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfo).all()   
                               
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name, item.table_info_type.vch_name, 
                         item.table_info_area.vch_name, int(item.num_people_amount),
                         item.table_info_minexpense.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_items(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfo.num_id, 
                               TableInfo.vch_name, 
                               TableInfo.num_people_amount, 
                               TableInfo.num_minexpense_type, 
                               TableInfo.num_area, 
                               TableInfo.num_type
                               ).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item[0]), item[1], int(item[5]), int(item[4]), int(item[2]), int(item[3])])
            index += 1
            
        return data
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        table_info = TableInfo()
        table_info.vch_name = data[1]
        table_info.num_type = data[2]
        table_info.num_area = data[3]
        table_info.num_people_amount = data[4]
        table_info.num_minexpense_type = data[5]
            
        session = SqlManager.session
        session.add(table_info)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfo).filter(TableInfo.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfo).filter(TableInfo.num_id == data[0]) \
            .update({TableInfo.vch_name: data[1],
                     TableInfo.num_type: data[2],
                     TableInfo.num_area: data[3],
                     TableInfo.num_people_amount: data[4],
                     TableInfo.num_minexpense_type: data[5]})
        session.flush()
        session.commit()


class SvcTypeSetting(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(TableInfoType).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(TableInfoType.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        table_info_type = TableInfoType()
        table_info_type.vch_name = data[1]
            
        session = SqlManager.session
        session.add(table_info_type)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfoType).filter(TableInfoType.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(TableInfoType).filter(TableInfoType.num_id == data[0]).update({TableInfoType.vch_name: data[1]})
        session.flush()
        session.commit()


class SvcUnitSetting(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(Unit).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), item.vch_name])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(Unit.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        unit = Unit()
        unit.vch_name = data[1]
            
        session = SqlManager.session
        session.add(unit)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(Unit).filter(Unit.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(Unit).filter(Unit.num_id == data[0]).update({Unit.vch_name: data[1]})
        session.flush()
        session.commit()


class SvcUserRole(Singleton):
    def __init__(self):
        pass
    
    @classmethod
    def get_all(cls):
        session = SqlManager.session
        session.flush()
        session.commit()
        
        result = session.query(UPermission).all()
        index = 0
        data = list()
        for item in result:
            data.append([index, int(item.num_id), int(item.num_perm_code), item.vch_perm_desc])
            index += 1
            
        return data
    
    @classmethod
    def get_id(cls):
        session = SqlManager.session
        result = session.query(UPermission.num_id).all()
        result.reverse()
        print result[0][0]
        return int(result[0][0])
    
    @classmethod
    def add_item(cls, data):
        if not data:
            return
        
        user_role = UPermission()
        user_role.num_perm_code = data[1]
        user_role.vch_perm_desc = data[2]
            
        session = SqlManager.session
        session.add(user_role)
        session.flush()
        session.commit()
        
    @classmethod
    def delete_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(UPermission).filter(UPermission.num_id == data[0]).delete()
        session.flush()
        session.commit()
    
    @classmethod
    def update_item(cls, data):
        if not data:
            return
        
        session = SqlManager.session
        session.query(UPermission).filter(UPermission.num_id == data[0]) \
            .update({UPermission.num_perm_code: data[1], UPermission.vch_perm_desc: data[2]})
        session.flush()
        session.commit()
