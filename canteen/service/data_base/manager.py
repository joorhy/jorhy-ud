#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from service.data_base.mode import *


def get_id(type_):
    session = SqlManager.get_instance().session
    result = None
    if type_ == 'AreaInfo':
        result = session.query(TableInfoArea.id).all()
    elif type_ == 'CategoryInfo':
        result = session.query(DishCategory.id).all()
    elif type_ == 'DepartmentInfo':
        result = session.query(UDept.id).all()
    elif type_ == 'SpecInfo':
        result = session.query(DishSpec.id).all()
    elif type_ == 'StyleInfo':
        result = session.query(DishStyle.id).all()
    elif type_ == 'MinExpenseInfo':
        result = session.query(TableInfoMinexpense.id).all()
    elif type_ == 'SchemeTypeInfo':
        result = session.query(PrinterSchemeType.id).all()
    elif type_ == 'TableTypeInfo':
        result = session.query(TableInfoType.id).all()
    elif type_ == 'UnitInfo':
        result = session.query(Unit.id).all()
    elif type_ == 'RoleInfo':
        result = session.query(UPermGroup.id).all()
    elif type_ == 'PermList':
        result = session.query(UPermList.id).all()

    result.reverse()
    return int(result[0][0])


def get_all(type_):
    session = SqlManager.get_instance().session
    session.flush()
    session.commit()

    data = list()
    if type_ == 'AreaInfo':
        result = session.query(TableInfoArea).all()
        for item in result:
            data.append(ModeTableInfoArea(item))
    elif type_ == 'CategoryInfo':
        result = session.query(DishCategory).all()
        for item in result:
            data.append(ModeDishCategory(item))
    elif type_ == 'DepartmentInfo':
        result = session.query(UDept).all()
        for item in result:
            data.append(ModeUDept(item))
    elif type_ == 'SpecInfo':
        result = session.query(DishSpec).all()
        for item in result:
            data.append(ModeDishSpec(item))
    elif type_ == 'StyleInfo':
        result = session.query(DishStyle).all()
        for item in result:
            data.append(ModeDishStyle(item))
    elif type_ == 'MinExpenseInfo':
        result = session.query(TableInfoMinexpense).all()
        for item in result:
            data.append(ModeTableInfoExpense(item))
    elif type_ == 'SchemeTypeInfo':
        result = session.query(PrinterSchemeType).all()
        for item in result:
            data.append(ModePrintSchemeType(item))
    elif type_ == 'TableTypeInfo':
        result = session.query(TableInfoType).all()
        for item in result:
            data.append(ModeTableInfoType(item))
    elif type_ == 'UnitInfo':
        result = session.query(Unit).all()
        for item in result:
            data.append(ModeUnit(item))
    elif type_ == 'RoleInfo':
        result = session.query(UPermGroup).all()
        for item in result:
            data.append(ModeUPermGroup(item))
    elif type_ == 'PermList':
        result = session.query(UPermList).all()
        for item in result:
            data.append(ModeUPermList(item))
    elif type_ == 'DishInfo':
        result = session.query(DishPublish).all()
        for item in result:
            data.append(ModeDishPublish(item))
    elif type_ == 'EmployeeInfo':
        result = session.query(UUserinfo).all()
        for item in result:
            data.append(ModeUUserInfo(item))
    elif type_ == 'PrintSchemeInfo':
        result = session.query(PrinterScheme).all()
        for item in result:
            data.append(ModePrintScheme(item))
    elif type_ == 'TableInfo':
        result = session.query(TableInfo).all()
        for item in result:
            data.append(ModeTableInfo(item))

    return data


def add_item(type_, data):
    if data is None:
        return

    session = SqlManager.get_instance().session
    item = None
    if type_ == 'AreaInfo':
        item = TableInfoArea()
        item.vch_name = data.name
    elif type_ == 'CategoryInfo':
        item = DishCategory()
        item.vch_name = data.name
    elif type_ == 'DepartmentInfo':
        item = UDept()
        item.vch_name = data.name
    elif type_ == 'SpecInfo':
        item = DishSpec()
        item.vch_dish_code = data.dish_code
        item.vch_name = data.name
        item.num_price = data.price
    elif type_ == 'StyleInfo':
        item = DishStyle()
        item.vch_dish_code = data.dish_code
        item.vch_name = data.name
        item.num_priceadd = data.price_add
        item.ch_mountadd = data.amount_add
    elif type_ == 'MinExpenseInfo':
        item = TableInfoMinexpense()
        item.vch_name = data.name
        item.num_amount = data.price
    elif type_ == 'SchemeTypeInfo':
        item = PrinterSchemeType()
        item.vch_name = data.name
    elif type_ == 'TableTypeInfo':
        item = TableInfoType()
        item.vch_name = data.name
    elif type_ == 'UnitInfo':
        item = Unit()
        item.vch_name = data.name
    elif type_ == 'PermList':
        item = UPermList()
        item.vch_code = data.code
        item.vch_pcode = data.p_code
        item.vch_name = data.name
    elif type_ == 'DishInfo':
        item = DishPublish()
        item.vch_code = data.code
        item.vch_name = data.name
        item.vch_spell = data.spell
        item.num_category = data.category
        item.num_unit = data.unit
        item.num_ticheng = data.commission
        item.num_discount = data.discount
        item.ch_disabled = data.stop
        item.vch_picname = data.image_url
    elif type_ == 'PrintSchemeInfo':
        item = PrinterScheme()

        item.vch_name = data.name
        item.num_valid = 1 if data.valid else 0
        item.num_scheme_type = data.scheme_type
        item.num_print_count = data.print_count
        if data.backup is not None:
            item.num_backup_scheme_id = data.backup
        item.vch_code = data.code
    elif type_ == 'TableInfo':
        item = TableInfo()
        item.vch_code = ''
        item.vch_name = data.name
        item.num_type = data.table_type
        item.num_area = data.area
        item.num_people_amount = data.people_num
        item.num_minexpense_id = data.min_type

    session.add(item)
    session.flush()
    session.commit()


def delete_item(type_, data):
    if data is None:
        return

    session = SqlManager.get_instance().session
    if type_ == 'AreaInfo':
        session.query(TableInfoArea).filter(TableInfoArea.id == data.key).delete()
    elif type_ == 'CategoryInfo':
        session.query(DishCategory).filter(DishCategory.id == data.key).delete()
    elif type_ == 'DepartmentInfo':
        session.query(UDept).filter(UDept.id == data.key).delete()
    elif type_ == 'SpecInfo':
        session.query(DishSpec).filter(DishSpec.id == data.key).delete()
    elif type_ == 'StyleInfo':
        session.query(DishStyle).filter(DishStyle.id == data.key).delete()
    elif type_ == 'MinExpenseInfo':
        session.query(TableInfoMinexpense).filter(TableInfoMinexpense.id == data.key).delete()
    elif type_ == 'SchemeTypeInfo':
        session.query(PrinterSchemeType).filter(PrinterSchemeType.id == data.key).delete()
    elif type_ == 'TableTypeInfo':
        session.query(TableInfoType).filter(TableInfoType.id == data.key).delete()
    elif type_ == 'UnitInfo':
        session.query(Unit).filter(Unit.id == data.key).delete()
    elif type_ == 'RoleInfo':
        session.query(UPermGroup).filter(UPermGroup.id == data.key).delete()
    elif type_ == 'PermList':
        session.query(UPermList).filter(UPermList.id == data.key).delete()
    elif type_ == 'DishInfo':
        session.query(DishPublish).filter(DishPublish.id == data.key).delete()
    elif type_ == 'EmployeeInfo':
        session.query(UUserinfo).filter(UUserinfo.id == data.key).delete()
    elif type_ == 'PrintSchemeInfo':
        session.query(PrinterScheme).filter(PrinterScheme.id == data.key).delete()
    elif type_ == 'TableInfo':
        session.query(TableInfo).filter(TableInfo.id == data.key).delete()

    session.flush()
    session.commit()


def update_item(type_, data):
    if data is None:
        return

    session = SqlManager.get_instance().session
    if type_ == 'AreaInfo':
        session.query(TableInfoArea).filter(TableInfoArea.id == data.key).\
            update({TableInfoArea.vch_name: data.name})
    elif type_ == 'CategoryInfo':
        session.query(DishCategory).filter(DishCategory.id == data.key).update({DishCategory.vch_name: data.name})
    elif type_ == 'DepartmentInfo':
        session.query(UDept).filter(UDept.id == data.key).update({UDept.vch_name: data.name})
    elif type_ == 'SpecInfo':
        session.query(DishSpec).filter(DishSpec.id == data.key).update({DishSpec.vch_name: data.name,
                                                                        DishSpec.num_price: float(data.price)})
    elif type_ == 'StyleInfo':
        session.query(DishStyle).filter(DishStyle.id == data.key).\
            update({DishStyle.vch_name: data.name,
                    DishStyle.num_priceadd: float(data.price_add),
                    DishStyle.ch_mountadd: data.amount_add})
    elif type_ == 'MinExpenseInfo':
        session.query(TableInfoMinexpense).filter(TableInfoMinexpense.id == data.key) \
            .update({TableInfoMinexpense.vch_name: data.name, TableInfoMinexpense.num_amount: float(data.price)})
    elif type_ == 'SchemeTypeInfo':
        session.query(PrinterSchemeType).filter(PrinterSchemeType.id == data.key) \
            .update({PrinterSchemeType.vch_name: data.name})
    elif type_ == 'TableTypeInfo':
        session.query(TableInfoType).filter(TableInfoType.id == data.key).\
            update({TableInfoType.vch_name: data.name})
    elif type_ == 'UnitInfo':
        session.query(Unit).filter(Unit.id == data.key).update({Unit.vch_name: data.name})
    elif type_ == 'PermList':
        session.query(UPermList).filter(UPermList.id == data.key) \
            .update({UPermList.vch_code: data.code,
                     UPermList.vch_pcode: data.p_code,
                     UPermList.vch_name: data.name})
    elif type_ == 'DishInfo':
        session.query(DishPublish).filter(DishPublish.id == data.key) \
            .update({DishPublish.vch_code: data.code,
                     DishPublish.vch_name: data.name,
                     DishPublish.vch_spell: data.spell,
                     DishPublish.num_category: data.category,
                     DishPublish.num_unit: data.unit,
                     DishPublish.num_ticheng: data.commission,
                     DishPublish.num_discount: data.discount,
                     DishPublish.ch_disabled: data.stop,
                     DishPublish.vch_picname: data.image_url})
    elif type_ == 'PrintSchemeInfo':
        session.query(PrinterScheme).filter(PrinterScheme.id == data.key).\
            update({PrinterScheme.vch_name: data.name,
                    PrinterScheme.num_valid: data.valid,
                    PrinterScheme.num_scheme_type: data.scheme_type,
                    PrinterScheme.num_print_count: data.print_count})
    elif type_ == 'TableInfo':
        session.query(TableInfo).filter(TableInfo.id == data.key) \
            .update({TableInfo.vch_name: data.name,
                     TableInfo.num_type: data.table_type,
                     TableInfo.num_area: data.area,
                     TableInfo.num_people_amount: data.people_num,
                     TableInfo.num_minexpense_id: data.min_type})

    session.flush()
    session.commit()


def update_print_scheme(data):
    if not data:
        return

    session = SqlManager.get_instance().session
    session.query(DishPublish).filter(DishPublish.id == data.key) \
        .update({DishPublish.num_printer_scheme_id: data.printer_scheme,
                 DishPublish.ch_is_print: data.is_print})
    session.flush()
    session.commit()


def is_has_spec(spec_id):
    session = SqlManager.get_instance().session
    session.flush()
    session.commit()
    result = session.query(DishSpec).filter(DishSpec.id == spec_id).all()
    if len(result) == 0:
        return False
    return True


def get_spec_by_dish_code(dish_code):
    session = SqlManager.get_instance().session
    session.flush()
    session.commit()

    data = list()
    result = session.query(DishSpec).filter(DishSpec.vch_dish_code == dish_code).all()
    for item in result:
            data.append(ModeDishSpec(item))

    return data


def delete_spec_by_dish_code(dish_code):
    session = SqlManager.get_instance().session
    session.query(DishSpec).filter(DishSpec.vch_dish_code == dish_code).delete()

    session.flush()
    session.commit()


def is_has_style(style_id):
    session = SqlManager.get_instance().session
    session.flush()
    session.commit()
    result = session.query(DishStyle).filter(DishStyle.id == style_id).all()
    if len(result) == 0:
        return False
    return True


def get_style_by_dish_code(dish_code):
    session = SqlManager.get_instance().session
    session.flush()
    session.commit()

    data = list()
    result = session.query(DishStyle).filter(DishStyle.vch_dish_code == dish_code).all()
    for item in result:
            data.append(ModeDishStyle(item))

    return data


def delete_style_by_dish_code(dish_code):
    session = SqlManager.get_instance().session
    session.query(DishStyle).filter(DishStyle.vch_dish_code == dish_code).delete()

    session.flush()
    session.commit()


def add_role_info(data, li_perm_list):
    session = SqlManager.get_instance().session
    perm_group = UPermGroup()
    perm_group.vch_type = data.type
    perm_group.vch_name = data.name
    perm_group.vch_desc = data.desc

    for perm in li_perm_list:
        if perm.selected:
            perm_list = session.query(UPermList).filter(UPermList.id == perm.key).one()
            perm_group.u_perm_lists.append(perm_list)

    session.add(perm_group)
    session.flush()
    session.commit()


def update_role_info(data, li_perm_list):
    session = SqlManager.get_instance().session
    perm_group = session.query(UPermGroup).filter(UPermGroup.id == data.key).one()
    #perm_group.vch_type = data.type
    perm_group.vch_name = data.name
    perm_group.vch_desc = data.desc

    for perm in li_perm_list:
        if perm.selected:
            perm_list = session.query(UPermList).filter(UPermList.id == perm.key).one()
            perm_group.u_perm_lists.append(perm_list)

    session.add(perm_group)
    session.flush()
    session.commit()


def get_perm_by_group(group):
    session = SqlManager.get_instance().session
    li_perm = session.query(UPermList).all()
    result = session.query(UPermGroup).filter(UPermGroup.id == group.key).one()
    data = list()
    for perm in li_perm:
        item = ModeUPermList(perm)
        if perm in result.u_perm_lists:
            item.selected = True
        data.append(item)

    return data


def add_user_info(data, li_perm_group):
    session = SqlManager.get_instance().session
    details = UUserdetail()
    details.vch_realname = data.name
    details.vch_englishname = ''
    details.dt_birthday = data.birthday
    details.num_dept_id = data.department
    details.num_gender = data.sex
    details.vch_phone = data.telephone
    details.vch_idcard = data.id_card
    details.num_status = data.state
    details.vch_address = data.address
    details.vch_email = data.email
    details.vch_memo = data.note

    session.add(details)
    session.flush()
    session.commit()

    user_info = UUserinfo()
    user_info.vch_name = data.code
    user_info.vch_psw = "0000"
    li_id_item = session.query(UUserdetail.id).all()
    li_id = list()
    for id_item in li_id_item:
        li_id.append(id_item[0])
    user_info.num_userdetails_id = int(max(li_id))

    for group in li_perm_group:
        if group.selected:
            perm_group = session.query(UPermGroup).filter(UPermGroup.id == group.key).one()
            user_info.u_perm_lists.append(perm_group)

    session.add(user_info)
    session.flush()
    session.commit()


def update_user_info(data, li_perm_group):
    session = SqlManager.get_instance().session
    session.query(UUserinfo).filter(UUserinfo.id == data.key).update({UUserinfo.vch_name: data.code})

    detail_id = session.query(UUserinfo.num_userdetails_id).filter(UUserinfo.id == data.key).all()
    session.query(UUserdetail).filter(UUserdetail.id == int(detail_id[0][0])) \
        .update({UUserdetail.vch_realname: data.name,
                 UUserdetail.dt_birthday: data.birthday,
                 UUserdetail.num_dept_id: data.department,
                 UUserdetail.num_gender: data.sex,
                 UUserdetail.vch_phone: data.telephone,
                 UUserdetail.vch_idcard: data.id_card,
                 UUserdetail.num_status: data.state,
                 UUserdetail.vch_address: data.address,
                 UUserdetail.vch_email: data.email,
                 UUserdetail.vch_memo: data.note})

    session.flush()
    session.commit()

    user_info = session.query(UUserinfo).filter(UUserinfo.id == data.key).one()
    for group in li_perm_group:
        if group.selected:
            perm_group = session.query(UPermGroup).filter(UPermGroup.id == group.key).one()
            user_info.u_perm_groups.append(perm_group)

    session.add(user_info)
    session.flush()
    session.commit()


def get_group_by_user(user):
    session = SqlManager.get_instance().session
    li_group = session.query(UPermGroup).all()
    result = session.query(UUserinfo).filter(UUserinfo.id == user.key).one()
    data = list()
    for group in li_group:
        item = ModeUPermGroup(group)
        if group in result.u_perm_groups:
            item.selected = True
        data.append(item)

    return data


def get_password_by_user_name(user_name):
    session = SqlManager.get_instance().session
    pass_word = session.query(UUserinfo.vch_psw).filter(UUserinfo.vch_name == user_name).one()

    return pass_word[0]

