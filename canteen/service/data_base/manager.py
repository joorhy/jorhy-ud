#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from service.data_base.mode import *


class SvcCanteenInfo():
    def __init__(self, type_):
        self.type = type_

    def get_id(self):
        session = SqlManager.session
        result = None
        if self.type == 'AreaInfo':
            result = session.query(TableInfoArea.id).all()
        elif self.type == 'CategoryInfo':
            result = session.query(DishCategory.id).all()
        elif self.type == 'DepartmentInfo':
            result = session.query(UDept.id).all()
        elif self.type == 'SpecInfo':
            result = session.query(DishSpec.id).all()
        elif self.type == 'StyleInfo':
            result = session.query(DishStyle.id).all()
        elif self.type == 'MinExpenseInfo':
            result = session.query(TableInfoMinexpense.id).all()
        elif self.type == 'SchemeTypeInfo':
            result = session.query(PrinterSchemeType.id).all()
        elif self.type == 'TableTypeInfo':
            result = session.query(TableInfoType.id).all()
        elif self.type == 'UnitInfo':
            result = session.query(Unit.id).all()
        elif self.type == 'RoleInfo':
            result = session.query(UPermission.id).all()

        result.reverse()
        return int(result[0][0])

    def get_all(self):
        session = SqlManager.session
        session.flush()
        session.commit()

        data = list()
        if self.type == 'AreaInfo':
            result = session.query(TableInfoArea).all()
            for item in result:
                data.append(ModeTableInfoArea(item))
        elif self.type == 'CategoryInfo':
            result = session.query(DishCategory).all()
            for item in result:
                data.append(ModeDishCategory(item))
        elif self.type == 'DepartmentInfo':
            result = session.query(UDept).all()
            for item in result:
                data.append(ModeUDept(item))
        elif self.type == 'SpecInfo':
            result = session.query(DishSpec).all()
            for item in result:
                data.append(ModeDishSpec(item))
        elif self.type == 'StyleInfo':
            result = session.query(DishStyle).all()
            for item in result:
                data.append(ModeDishStyle(item))
        elif self.type == 'MinExponseInfo':
            result = session.query(TableInfoMinexpense).all()
            for item in result:
                data.append(ModeTableInfoExpense(item))
        elif self.type == 'SchemeTypeInfo':
            result = session.query(PrinterSchemeType).all()
            for item in result:
                data.append(ModePrintSchemeType(item))
        elif self.type == 'TableTypeInfo':
            result = session.query(TableInfoType).all()
            for item in result:
                data.append(ModeTableInfoType(item))
        elif self.type == 'UnitInfo':
            result = session.query(Unit).all()
            for item in result:
                data.append(ModeUnit(item))
        elif self.type == 'RoleInfo':
            result = session.query(UPermission).all()
            for item in result:
                data.append(ModeUPermission(item))
        elif self.type == 'DishInfo':
            result = session.query(DishPublish).all()
            for item in result:
                data.append(ModeDishPublish(item))
        elif self.type == 'EmployeeInfo':
            result = session.query(UUserinfo).all()
            for item in result:
                data.append(ModeUUserInfo(item))
        elif self.type == 'PrintSchemeInfo':
            result = session.query(PrinterScheme).all()
            for item in result:
                data.append(ModePrintScheme(item))
        elif self.type == 'TableInfo':
            result = session.query(TableInfo).all()
            for item in result:
                data.append(ModeTableInfo(item))

        return data

    def add_item(self, data):
        if data is None:
            return

        session = SqlManager.session
        item = None
        if self.type == 'AreaInfo':
            item = TableInfoArea()
            item.vch_name = data.name
        elif self.type == 'CategoryInfo':
            item = DishCategory()
            item.vch_name = data.name
        elif self.type == 'DepartmentInfo':
            item = UDept()
            item.vch_name = data.name
        elif self.type == 'SpecInfo':
            item = DishSpec()
            item.vch_name = data.name
            item.num_price = data.price
        elif self.type == 'StyleInfo':
            item = DishStyle()
            item.vch_name = data.name
            item.num_priceadd = data.price_add
            item.ch_mountadd = data.amount_add
        elif self.type == 'MinExpenseInfo':
            item = TableInfoMinexpense()
            item.vch_name = data.name
            item.num_amount = data.price
        elif self.type == 'SchemeTypeInfo':
            item = PrinterSchemeType()
            item.vch_name = data.name
        elif self.type == 'TableTypeInfo':
            item = TableInfoType()
            item.vch_name = data.name
        elif self.type == 'UnitInfo':
            item = Unit()
            item.vch_name = data.name
        elif self.type == 'RoleInfo':
            item = UPermission()
            item.num_perm_code = data.code
            item.vch_perm_desc = data.name
        elif self.type == 'DishInfo':
            item = DishPublish()
            item.num_code = data.code
            item.vch_name = data.name
            item.vch_spell = data.spell
            item.num_spec_id = data.spec
            item.num_category = data.category
            item.num_default_price = data.price
            item.num_unit = data.unit
            item.num_style_id = data.style
            item.num_ticheng = data.commisssion
            item.num_discount = data.discount
            item.ch_disabled = data.stop
            item.vch_picname = data.image_url
            item.num_printer_scheme_id = data.printer_scheme
        elif self.type == 'EmployeeInfo':
            item = UUserdetail()
            item.vch_realname = data.name
            item.vch_englishname = ''
            item.dt_birthday = data.birthday
            item.num_dept = data.department
            item.num_gender = data.sex
            item.num_phone = data.telephone
            item.vch_idcard = data.id_card
            item.num_status = data.state
            item.vch_address = data.address
            item.vch_email = data.email
            item.vch_memo = data.note
        elif self.type == 'PrintSchemeInfo':
            item = PrinterScheme()
            item.id = data.id
            item.vch_name = data.name
            item.num_valid = data.valid
            item.num_bill_type = data.scheme_type
            item.num_print_count = data.print_count
            item.num_backup_scheme_id = data.backup
        elif self.type == 'TableInfo':
            item = TableInfo()
            item.vch_name = data.name
            item.num_type = data.table_type
            item.num_area = data.area
            item.num_people_amount = data.people_num
            item.num_minexpense_type = data.min_type

        session.add(item)
        session.flush()
        session.commit()

        if self.type == 'EmployeeInfo':
            user_info = UUserinfo()
            user_info.vch_name = data.code
            user_info.vch_psw = "0000"
            li_id_item = session.query(UUserdetail.id).all()
            li_id = list()
            for id_item in li_id_item:
                li_id.append(id_item[0])
            user_info.num_userdetails_id = int(max(li_id))

            session.add(user_info)
            session.flush()
            session.commit()

    def delete_item(self, data):
        if data is None:
            return

        session = SqlManager.session
        if self.type == 'AreaInfo':
            session.query(TableInfoArea).filter(TableInfoArea.id == data.id).delete()
        elif self.type == 'CategoryInfo':
            session.query(DishCategory).filter(DishCategory.id == data.id).delete()
        elif self.type == 'DepartmentInfo':
            session.query(UDept).filter(UDept.id == data.id).delete()
        elif self.type == 'SpecInfo':
            session.query(DishSpec).filter(DishSpec.id == data.id).delete()
        elif self.type == 'StyleInfo':
            session.query(DishStyle).filter(DishStyle.id == data.id).delete()
        elif self.type == 'MinExpenseInfo':
            session.query(TableInfoMinexpense).filter(TableInfoMinexpense.id == data.id).delete()
        elif self.type == 'SchemeTypeInfo':
            session.query(PrinterSchemeType).filter(PrinterSchemeType.id == data.id).delete()
        elif self.type == 'TableTypeInfo':
            session.query(TableInfoType).filter(TableInfoType.id == data.id).delete()
        elif self.type == 'UnitInfo':
            session.query(Unit).filter(Unit.id == data.id).delete()
        elif self.type == 'RoleInfo':
            session.query(UPermission).filter(UPermission.id == data.id).delete()
        elif self.type == 'DishInfo':
            session.query(DishPublish).filter(DishPublish.id == data.id).delete()
        elif self.type == 'EmployeeInfo':
            session.query(UUserinfo).filter(UUserinfo.id == data.id).delete()
        elif self.type == 'PrintSchemeInfo':
            session.query(PrinterScheme).filter(PrinterScheme.id == data.id).delete()
        elif self.type == 'TableInfo':
            session.query(TableInfo).filter(TableInfo.id == data.id).delete()

        session.flush()
        session.commit()

    def update_item(self, data):
        if data is None:
            return

        session = SqlManager.session
        if self.type == 'AreaInfo':
            session.query(TableInfoArea).filter(TableInfoArea.id == data.id).update({TableInfoArea.vch_name: data.name})
        elif self.type == 'CategoryInfo':
            session.query(DishCategory).filter(DishCategory.id == data.id).update({DishCategory.vch_name: data.name})
        elif self.type == 'DepartmentInfo':
            session.query(UDept).filter(UDept.id == data.id).update({UDept.vch_name: data.name})
        elif self.type == 'SpecInfo':
            session.query(DishSpec).filter(DishSpec.id == data.id).update({DishSpec.vch_name: data.name,
                                                                           DishSpec.num_price: data.price})
        elif self.type == 'StyleInfo':
            session.query(DishStyle).filter(DishStyle.id == data.id).update({DishStyle.vch_name: data.name,
                                                                             DishStyle.num_priceadd: data.price_add,
                                                                             DishStyle.ch_mountadd: data.amount_add})
        elif self.type == 'MinExpenseInfo':
            session.query(TableInfoMinexpense).filter(TableInfoMinexpense.id == data.id) \
                .update({TableInfoMinexpense.vch_name: data.name, TableInfoMinexpense.num_amount: data.price})
        elif self.type == 'SchemeTypeInfo':
            session.query(PrinterSchemeType).filter(PrinterSchemeType.id == data.id) \
                .update({PrinterSchemeType.vch_name: data.name})
        elif self.type == 'TableTypeInfo':
            session.query(TableInfoType).filter(TableInfoType.id == data.id).update({TableInfoType.vch_name: data.name})
        elif self.type == 'UnitInfo':
            session.query(Unit).filter(Unit.id == data.id).update({Unit.vch_name: data.name})
        elif self.type == 'RoleInfo':
            session.query(UPermission).filter(UPermission.id == data.id) \
                .update({UPermission.num_perm_code: data.code, UPermission.vch_perm_desc: data.name})
        elif self.type == 'DishInfo':
            session.query(DishPublish).filter(DishPublish.id == data[0]) \
                .update({DishPublish.num_code: data.code,
                         DishPublish.vch_name: data.name,
                         DishPublish.vch_spell: data.spell,
                         DishPublish.num_spec_id: data.spec,
                         DishPublish.num_category: data.category,
                         DishPublish.num_default_price: data.price,
                         DishPublish.num_unit: data.unit,
                         DishPublish.num_style_id: data.style,
                         DishPublish.num_ticheng: data.commisssion,
                         DishPublish.num_discount: data.discount,
                         DishPublish.vch_picname: data.image_url,
                         DishPublish.item.ch_disabled: data.stop,
                         DishPublish.num_printer_scheme_id: data.printer_scheme})
        elif self.type == 'EmployeeInfo':
            session.query(UUserinfo).filter(UUserinfo.id == data.id).update({UUserinfo.vch_name: data.code})

            detail_id = session.query(UUserinfo.num_userdetails_id).filter(UUserinfo.id == data.id).all()
            session.query(UUserdetail).filter(UUserdetail.id == int(detail_id[0][0])) \
                .update({UUserdetail.vch_realname: data.name,
                         UUserdetail.dt_birthday: data.birthday,
                         UUserdetail.num_dept: data.department,
                         UUserdetail.num_gender: data.sex,
                         UUserdetail.num_phone: data.telephone,
                         UUserdetail.vch_idcard: data.id_card,
                         UUserdetail.vch_address: data.address,
                         UUserdetail.vch_email: data.email,
                         UUserdetail.vch_memo: data.note})
        elif self.type == 'PrintSchemeInfo':
            session.query(PrinterScheme).filter(PrinterScheme.id == data.id).\
                update({PrinterScheme.vch_name: data.name,
                        PrinterScheme.num_valid: data.valid,
                        PrinterScheme.num_bill_type: data.scheme_type,
                        PrinterScheme.num_print_count: data.print_count})
        elif self.type == 'TableInfo':
            session.query(TableInfo).filter(TableInfo.id == data[0]) \
                .update({TableInfo.vch_name: data.name,
                         TableInfo.num_type: data.table_type,
                         TableInfo.num_area: data.area,
                         TableInfo.num_people_amount: data.people_num,
                         TableInfo.num_minexpense_type: data.min_type})

        session.flush()
        session.commit()


class SvcPrintScheme():
    def __init__(self):
        pass

    def update_print_scheme(self, data):
        if not data:
            return

        if self.type != 'DishInfo':
            return

        session = SqlManager.session
        session.query(DishPublish).filter(DishPublish.id == data[0]) \
            .update({DishPublish.num_printer_scheme_id: data[1]})
        session.flush()
        session.commit()