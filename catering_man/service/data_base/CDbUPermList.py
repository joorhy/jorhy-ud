from sqlalchemy import Column, Integer, String
from service.CSqlManager import CSqlManager

class CDbUPermList(CSqlManager.base_model):
    __tablename__ = 'u_perm_list'

    num_id = Column(Integer, primary_key=True)
    vch_name = Column(String(45))
    
    def __repr__(self):
        return '%s' % (self.__class__.__name__)
