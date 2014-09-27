# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from service.data_base.SqlManager import SqlManager

Base = SqlManager.base_model
metadata = Base.metadata


class CompanyInfo(Base):
    __tablename__ = 'company_info'

    vch_uid = Column(String(45), primary_key=True)
    vch_name = Column(String(45))
    vch_boss_name = Column(String(45))
    num_boss_phone = Column(Integer)
    vch_email = Column(String(45))
    vch_address = Column(String(45))


class DishCategory(Base):
    __tablename__ = 'dish_category'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class DishPublish(Base):
    __tablename__ = 'dish_publish'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_code = Column(Integer)
    vch_spell = Column(String(45))
    num_default_price = Column(Integer)
    vch_picname = Column(String(45))
    num_style_id = Column(ForeignKey(u'dish_style.num_id'), index=True)
    num_spec_id = Column(ForeignKey(u'dish_spec.num_id'), index=True)
    num_category = Column(ForeignKey(u'dish_category.num_id'), index=True)
    num_unit = Column(ForeignKey(u'unit.num_id'), index=True)
    num_ticheng = Column(Float)
    num_discount = Column(Float)
    num_change_code = Column(Integer)
    num_printer_scheme_id = Column(ForeignKey(u'printer_scheme.num_id'), index=True)

    dish_category = relationship(u'DishCategory')
    num_printer_scheme = relationship(u'PrinterScheme')
    num_spec = relationship(u'DishSpec')
    num_style = relationship(u'DishStyle')
    unit = relationship(u'Unit')


class DishPublishLog(Base):
    __tablename__ = 'dish_publish_log'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_code = Column(Integer)
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


class DishServer(Base):
    __tablename__ = 'dish_server'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_code = Column(Integer)
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


class DishSpec(Base):
    __tablename__ = 'dish_spec'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_price = Column(Integer)


class DishStyle(Base):
    __tablename__ = 'dish_style'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_priceadd = Column(Integer)
    ch_mountadd = Column(String(1))


class MeterialStock(Base):
    __tablename__ = 'meterial_stock'

    num_id = Column(Integer, primary_key=True)
    num_meterial_cat_id = Column(Integer)
    num_meterial_id = Column(Integer)
    num_amount = Column(Integer)
    num_unit_id = Column(ForeignKey(u'unit.num_id'), index=True)
    dt_date = Column(DateTime)

    num_unit = relationship(u'Unit')


class PrinterScheme(Base):
    __tablename__ = 'printer_scheme'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_valid = Column(Integer)
    num_bill_type = Column(ForeignKey(u'printer_scheme_type.num_id'), index=True)
    num_print_count = Column(Integer)
    num_produced_count = Column(Integer)

    printer_scheme_type = relationship(u'PrinterSchemeType')


class PrinterSchemeType(Base):
    __tablename__ = 'printer_scheme_type'

    num_id = Column(Integer, primary_key=True, index=True)
    vch_name = Column(String(45))


class Purchase(Base):
    __tablename__ = 'purchase'

    num_id = Column(Integer, primary_key=True)
    num_userinfo_id = Column(ForeignKey(u'purchase_userinfo.num_id'), index=True)
    num_meterial_id = Column(ForeignKey(u'purchase_meterial.num_id'), index=True)
    num_meterial_price = Column(Integer)
    num_meterial_unit = Column(ForeignKey(u'unit.num_id'), index=True)
    num_meterial_amount = Column(Integer)
    num_pay_status = Column(Integer)
    dt_date = Column(DateTime)

    num_meterial = relationship(u'PurchaseMeterial')
    unit = relationship(u'Unit')
    num_userinfo = relationship(u'PurchaseUserinfo')


class PurchaseMeterial(Base):
    __tablename__ = 'purchase_meterial'

    num_id = Column(Integer, primary_key=True)
    num_cat_id = Column(ForeignKey(u'purchase_meterial_cat.num_id'), index=True)
    vch_name = Column(String(45))

    num_cat = relationship(u'PurchaseMeterialCat')


class PurchaseMeterialCat(Base):
    __tablename__ = 'purchase_meterial_cat'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class PurchaseUserinfo(Base):
    __tablename__ = 'purchase_userinfo'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_phone = Column(Integer)


class TableBook(Base):
    __tablename__ = 'table_book'

    num_bookuid = Column(Integer, primary_key=True)
    num_table_id = Column(ForeignKey(u'table_info.num_id'), index=True)
    ch_openflag = Column(String(1))
    num_consumers = Column(Integer)

    num_table = relationship(u'TableInfo')


t_table_booked_info = Table(
    'table_booked_info', metadata,
    Column('vch_uid', String(45), nullable=False),
    Column('num_price', Integer),
    Column('num_price_add', Integer),
    Column('num_price_fix', Integer),
    Column('vch_print_memo', String(45))
)


class TableDish(Base):
    __tablename__ = 'table_dish'

    num_id = Column(Integer, primary_key=True)
    num_dish_id = Column(ForeignKey(u'dish_publish_log.num_id'), index=True)
    num_dish_num = Column(Integer)

    num_dish = relationship(u'DishPublishLog')


class TableInfo(Base):
    __tablename__ = 'table_info'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_type = Column(ForeignKey(u'table_info_type.num_id'), index=True)
    num_area = Column(ForeignKey(u'table_info_area.num_id'), index=True)
    num_people_amount = Column(Integer)
    num_minexpense_type = Column(ForeignKey(u'table_info_minexpense.num_id'), index=True)

    table_info_area = relationship(u'TableInfoArea')
    table_info_minexpense = relationship(u'TableInfoMinexpense')
    table_info_type = relationship(u'TableInfoType')


class TableInfoArea(Base):
    __tablename__ = 'table_info_area'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class TableInfoMinexpense(Base):
    __tablename__ = 'table_info_minexpense'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_amount = Column(Integer)


class TableInfoType(Base):
    __tablename__ = 'table_info_type'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class TableOrder(Base):
    __tablename__ = 'table_order'

    num_id = Column(Integer, primary_key=True)
    num_table_id = Column(Integer)
    num_price = Column(Integer)
    num_price_add = Column(Integer)
    num_price_fix = Column(Integer)
    vch_print_memo = Column(String(45))
    dt_checkin = Column(DateTime)
    dt_order_food = Column(DateTime)
    dt_checkout = Column(DateTime)
    num_people_amount = Column(Integer)
    num_open_user_id = Column(ForeignKey(u'u_userinfo.num_id'), index=True)
    num_table_book_id = Column(ForeignKey(u'table_book.num_bookuid'), index=True)
    num_table_dish_id = Column(ForeignKey(u'table_dish.num_dish_id'), index=True)

    num_open_user = relationship(u'UUserinfo')
    num_table_book = relationship(u'TableBook')
    num_table_dish = relationship(u'TableDish')


class UDept(Base):
    __tablename__ = 'u_dept'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UDuty(Base):
    __tablename__ = 'u_duty'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UPermList(Base):
    __tablename__ = 'u_perm_list'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UPermListCopy(Base):
    __tablename__ = 'u_perm_list_copy'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UPermission(Base):
    __tablename__ = 'u_permission'

    num_id = Column(Integer, primary_key=True)
    num_perm_code = Column(ForeignKey(u'u_perm_list.num_id'), index=True)
    vch_perm_desc = Column(String(45))

    u_perm_list = relationship(u'UPermList')


class UType(Base):
    __tablename__ = 'u_type'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    num_perm_id = Column(ForeignKey(u'u_permission.num_id'), index=True)

    num_perm = relationship(u'UPermission')


class UUserSchedule(Base):
    __tablename__ = 'u_user_schedule'

    num_id = Column(Integer, primary_key=True)
    num_user_id = Column(ForeignKey(u'u_userinfo.num_id'), index=True)
    dt_onduty = Column(DateTime)
    num_status_id = Column(ForeignKey(u'u_user_schedule_status.num_id'), index=True)

    num_status = relationship(u'UUserScheduleStatu')
    num_user = relationship(u'UUserinfo')


class UUserScheduleStatu(Base):
    __tablename__ = 'u_user_schedule_status'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UUserStatu(Base):
    __tablename__ = 'u_user_status'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))


class UUserdetail(Base):
    __tablename__ = 'u_userdetails'

    num_id = Column(Integer, primary_key=True)
    vch_realname = Column(String(45))
    vch_englishname = Column(String(45))
    vch_email = Column(String(45))
    vch_hobbies = Column(String(45))
    num_dept = Column(ForeignKey(u'u_dept.num_id'), index=True)
    num_duty = Column(ForeignKey(u'u_duty.num_id'), index=True)
    num_phone = Column(Integer)
    num_gender = Column(Integer)
    dt_birthday = Column(DateTime)
    num_status = Column(ForeignKey(u'u_user_status.num_id'), index=True)
    vch_idcard = Column(String(45))
    vch_address = Column(String(45))
    vch_memo = Column(String(45))

    u_dept = relationship(u'UDept')
    u_duty = relationship(u'UDuty')
    u_user_statu = relationship(u'UUserStatu')


class UUserinfo(Base):
    __tablename__ = 'u_userinfo'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    vch_psw = Column(String(45))
    num_user_type = Column(ForeignKey(u'u_type.num_id'), index=True)
    num_userdetails_id = Column(ForeignKey(u'u_userdetails.num_id'), index=True)

    u_type = relationship(u'UType')
    num_userdetails = relationship(u'UUserdetail')


class UVipCard(Base):
    __tablename__ = 'u_vip_card'

    num_id = Column(Integer, primary_key=True)
    ch_type = Column(String(1))
    dt_deadline = Column(DateTime)


class Unit(Base):
    __tablename__ = 'unit'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
