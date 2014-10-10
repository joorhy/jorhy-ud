# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from service.data_base.SqlManager import SqlManager

Base = SqlManager.base_model
metadata = Base.metadata


class CompanyInfo(Base):
    __tablename__ = 'company_info'

    id = Column(Integer, primary_key=True)
    vch_uid = Column(String(45), nullable=False)
    vch_name = Column(String(45))
    vch_boss_name = Column(String(45))
    num_boss_phone = Column(Integer)
    vch_email = Column(String(45))
    vch_address = Column(String(45))


class DeprecatedUUserScheduleStatu(Base):
    __tablename__ = 'deprecated_u_user_schedule_status'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class DeprecatedUUserStatu(Base):
    __tablename__ = 'deprecated_u_user_status'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class DeviceRegistration(Base):
    __tablename__ = 'device_registration'

    id = Column(Integer, primary_key=True)
    vch_device_mac = Column(String(45))
    vch_device_name = Column(String(45))


class DishCategory(Base):
    __tablename__ = 'dish_category'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class DishPublish(Base):
    __tablename__ = 'dish_publish'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    vch_code = Column(String(45), nullable=False)
    vch_spell = Column(String(45))
    num_default_price = Column(Integer)
    vch_picname = Column(String(45))
    num_style_id = Column(ForeignKey(u'dish_style.id'), index=True)
    num_spec_id = Column(ForeignKey(u'dish_spec.id'), index=True)
    num_category = Column(ForeignKey(u'dish_category.id'), index=True)
    num_unit = Column(ForeignKey(u'unit.id'), index=True)
    num_ticheng = Column(Float)
    num_discount = Column(Float)
    num_change_code = Column(Integer)
    num_printer_scheme_id = Column(ForeignKey(u'printer_scheme.id'), index=True)
    num_recommend = Column(Integer)
    ch_disabled = Column(String(1))
    ch_is_print = Column(String(1))

    dish_category = relationship(u'DishCategory')
    num_printer_scheme = relationship(u'PrinterScheme')
    num_spec = relationship(u'DishSpec')
    num_style = relationship(u'DishStyle')
    unit = relationship(u'Unit')


class DishPublishLog(Base):
    __tablename__ = 'dish_publish_log'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    vch_code = Column(String(45), nullable=False)
    vch_spell = Column(String(45))
    num_default_price = Column(Float)
    vch_picname = Column(String(45))
    num_style_id = Column(Integer)
    num_spec_id = Column(Integer)
    num_category = Column(Integer)
    num_unit = Column(Integer)
    num_ticheng = Column(Float)
    num_discount = Column(Float)
    num_change_code = Column(Integer)
    num_printer_scheme_id = Column(Integer)
    num_recommend = Column(Integer)
    vch_customized_style = Column(String(100))
    num_dish_withdraw_id = Column(ForeignKey(u'dish_publish_log_withdraw.id'), index=True)

    num_dish_withdraw = relationship(u'DishPublishLogWithdraw')


class DishPublishLogWithdraw(Base):
    __tablename__ = 'dish_publish_log_withdraw'

    id = Column(Integer, primary_key=True)
    vch_desc = Column(String(45))


class DishServer(Base):
    __tablename__ = 'dish_server'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_code = Column(Integer, nullable=False)
    vch_spell = Column(String(45))
    num_default_price = Column(Integer)
    vch_picname = Column(String(45))
    num_style_id = Column(Integer)
    num_spec_id = Column(Integer)
    num_category = Column(Integer)
    num_unit = Column(Integer)
    num_ticheng = Column(Float)
    num_discount = Column(Float)
    num_change_code = Column(Integer)
    num_printer_scheme_id = Column(Integer)
    num_recommend = Column(Integer)
    ch_disabled = Column(String(1))
    ch_is_print = Column(String(1))


class DishSpec(Base):
    __tablename__ = 'dish_spec'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_price = Column(Float)
    vch_dish_code = Column(String(45))


class DishStyle(Base):
    __tablename__ = 'dish_style'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_priceadd = Column(Float)
    ch_mountadd = Column(String(1))
    vch_dish_code = Column(String(45))


class MeterialStock(Base):
    __tablename__ = 'meterial_stock'

    id = Column(Integer, primary_key=True)
    num_meterial_cat_id = Column(Integer)
    num_meterial_id = Column(Integer)
    num_amount = Column(Integer)
    num_unit_id = Column(ForeignKey(u'unit.id'), index=True)
    dt_date = Column(DateTime)

    num_unit = relationship(u'Unit')


class PrinterScheme(Base):
    __tablename__ = 'printer_scheme'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_valid = Column(Integer)
    num_scheme_type = Column(ForeignKey(u'printer_scheme_type.id'), index=True)
    num_print_count = Column(Integer)
    num_backup_scheme_id = Column(Integer)
    num_produced_count = Column(Integer, server_default=text("'1'"))
    vch_code = Column(String(45))

    printer_scheme_type = relationship(u'PrinterSchemeType')


class PrinterSchemeType(Base):
    __tablename__ = 'printer_scheme_type'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True)
    num_userinfo_id = Column(ForeignKey(u'purchase_userinfo.id'), index=True)
    num_meterial_id = Column(ForeignKey(u'purchase_meterial.id'), index=True)
    num_meterial_price = Column(Integer)
    num_meterial_unit = Column(ForeignKey(u'unit.id'), index=True)
    num_meterial_amount = Column(Integer)
    num_pay_status = Column(Integer)
    dt_date = Column(DateTime)

    num_meterial = relationship(u'PurchaseMeterial')
    unit = relationship(u'Unit')
    num_userinfo = relationship(u'PurchaseUserinfo')


class PurchaseMeterial(Base):
    __tablename__ = 'purchase_meterial'

    id = Column(Integer, primary_key=True)
    num_cat_id = Column(ForeignKey(u'purchase_meterial_cat.id'), index=True)
    vch_name = Column(String(45))

    num_cat = relationship(u'PurchaseMeterialCat')


class PurchaseMeterialCat(Base):
    __tablename__ = 'purchase_meterial_cat'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class PurchaseUserinfo(Base):
    __tablename__ = 'purchase_userinfo'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_phone = Column(Integer)


class TableBook(Base):
    __tablename__ = 'table_book'

    id = Column(Integer, primary_key=True)
    num_table_id = Column(ForeignKey(u'table_info.id'), index=True)
    ch_openflag = Column(String(1))
    num_consumers = Column(Integer)

    num_table = relationship(u'TableInfo')


class TableBookedInfo(Base):
    __tablename__ = 'table_booked_info'

    id = Column(Integer, primary_key=True)
    vch_uid = Column(String(45), nullable=False)
    num_price = Column(Integer)
    num_price_add = Column(Integer)
    num_price_fix = Column(Integer)
    vch_print_memo = Column(String(45))


class TableDish(Base):
    __tablename__ = 'table_dish'

    id = Column(Integer, primary_key=True)
    num_batch_id = Column(Integer, nullable=False, index=True)
    num_dish_publish_log_id = Column(ForeignKey(u'dish_publish_log.id'), index=True)
    num_dish_num = Column(Integer)

    num_dish_publish_log = relationship(u'DishPublishLog')


class TableInfo(Base):
    __tablename__ = 'table_info'

    id = Column(Integer, primary_key=True)
    vch_code = Column(String(45))
    vch_name = Column(String(45))
    num_type = Column(ForeignKey(u'table_info_type.id'), index=True)
    num_area = Column(ForeignKey(u'table_info_area.id'), index=True)
    num_people_amount = Column(Integer)
    num_minexpense_id = Column(ForeignKey(u'table_info_minexpense.id'), index=True)

    table_info_area = relationship(u'TableInfoArea')
    num_minexpense = relationship(u'TableInfoMinexpense')
    table_info_type = relationship(u'TableInfoType')


class TableInfoArea(Base):
    __tablename__ = 'table_info_area'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class TableInfoMinexpense(Base):
    __tablename__ = 'table_info_minexpense'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_amount = Column(Float)


class TableInfoType(Base):
    __tablename__ = 'table_info_type'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class TableOrder(Base):
    __tablename__ = 'table_order'

    id = Column(Integer, primary_key=True)
    num_table_id = Column(Integer)
    num_price = Column(Float)
    num_price_add = Column(Float)
    num_price_fix = Column(Float)
    vch_print_memo = Column(String(45))
    dt_checkin_start = Column(DateTime)
    dt_checkin_end = Column(DateTime)
    dt_checkout = Column(DateTime)
    num_people_amount = Column(Integer)
    num_open_user_id = Column(ForeignKey(u'u_userinfo.id'), index=True)
    num_table_book_id = Column(ForeignKey(u'table_book.id'), index=True)
    num_table_dish_batch_id = Column(Integer)

    num_open_user = relationship(u'UUserinfo')
    num_table_book = relationship(u'TableBook')


class UDept(Base):
    __tablename__ = 'u_dept'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UPermGroup(Base):
    __tablename__ = 'u_perm_group'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    vch_type = Column(String(1))
    vch_perm_desc = Column(String(45))

    u_perm_lists = relationship(u'UPermList', secondary='u_perm_group_has_u_perm_list')


t_u_perm_group_has_u_perm_list = Table(
    'u_perm_group_has_u_perm_list', metadata,
    Column('u_perm_group_id', ForeignKey(u'u_perm_group.id', ondelete=u'CASCADE'), primary_key=True, nullable=False, index=True),
    Column('u_perm_list_id', ForeignKey(u'u_perm_list.id'), primary_key=True, nullable=False, index=True)
)


class UPermList(Base):
    __tablename__ = 'u_perm_list'

    id = Column(Integer, primary_key=True)
    vch_code = Column(String(45))
    vch_pcode = Column(String(45))
    vch_name = Column(String(45))


class UScheduleOndutyType(Base):
    __tablename__ = 'u_schedule_onduty_type'

    id = Column(Integer, primary_key=True)
    num_name = Column(String(45))


class UType(Base):
    __tablename__ = 'u_type'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UUserLeave(Base):
    __tablename__ = 'u_user_leave'

    id = Column(Integer, primary_key=True)
    num_leave_user_id = Column(ForeignKey(u'u_userinfo.id'), index=True)
    dt_leave = Column(DateTime)

    num_leave_user = relationship(u'UUserinfo')


class UUserSchedule(Base):
    __tablename__ = 'u_user_schedule'

    id = Column(Integer, primary_key=True)
    num_user_id = Column(ForeignKey(u'u_userinfo.id'), index=True)
    dt_onduty = Column(DateTime)
    num_status_id = Column(Integer)
    num_onduty_type_id = Column(ForeignKey(u'u_schedule_onduty_type.id'), index=True)

    num_onduty_type = relationship(u'UScheduleOndutyType')
    num_user = relationship(u'UUserinfo')


class UUserdetail(Base):
    __tablename__ = 'u_userdetails'

    id = Column(Integer, primary_key=True)
    vch_realname = Column(String(45))
    vch_englishname = Column(String(45))
    vch_email = Column(String(45))
    num_dept_id = Column(ForeignKey(u'u_dept.id'), index=True)
    vch_duty = Column(String(45))
    num_userdetails_type_id = Column(ForeignKey(u'u_userdetails_type.id'), index=True)
    vch_phone = Column(String(45))
    num_gender = Column(Integer)
    dt_birthday = Column(DateTime)
    num_status = Column(Integer)
    vch_idcard = Column(String(45))
    vch_address = Column(String(45))
    vch_memo = Column(String(45))

    num_dept = relationship(u'UDept')
    num_userdetails_type = relationship(u'UUserdetailsType')


class UUserdetailsType(Base):
    __tablename__ = 'u_userdetails_type'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UUserinfo(Base):
    __tablename__ = 'u_userinfo'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45), nullable=False)
    vch_psw = Column(String(45))
    num_user_type = Column(Integer)
    num_userdetails_id = Column(ForeignKey(u'u_userdetails.id'), index=True)

    u_perm_groups = relationship(u'UPermGroup', secondary='u_userinfo_has_u_perm_group')
    num_userdetails = relationship(u'UUserdetail')


t_u_userinfo_has_u_perm_group = Table(
    'u_userinfo_has_u_perm_group', metadata,
    Column('u_userinfo_id', ForeignKey(u'u_userinfo.id'), primary_key=True, nullable=False, index=True),
    Column('u_perm_group_id', ForeignKey(u'u_perm_group.id'), primary_key=True, nullable=False, index=True)
)


class UVipCard(Base):
    __tablename__ = 'u_vip_card'

    id = Column(Integer, primary_key=True)
    ch_type = Column(String(1))
    dt_deadline = Column(DateTime)


class Unit(Base):
    __tablename__ = 'unit'

    id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
