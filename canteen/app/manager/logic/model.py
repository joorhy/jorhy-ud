#!/usr/bin/env python
# -*- coding: utf-8 -*- 
from app.manager.logic.data import *

import wx
import wx.xrc
import wx.dataview


class ModelArea(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        # Return the item which is this item's parent.
        ##self.log.write("GetParent\n")
        
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataArea):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        # We're not allowing edits in column zero (see below) so we just need
        # to deal with Song objects and columns 1 - 5
        node = self.ItemToObject(item)
        if isinstance(node, DataArea):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value


class ModelMinExpense(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
          
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 4

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string',
                  3: 'int'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        if not item:
            return True
            
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        node = self.ItemToObject(item)          
        if isinstance(node, DataMinExpense):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name,
                      3: node.price}
            return mapper[col]
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):    
        node = self.ItemToObject(item)
        if isinstance(node, DataMinExpense):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value
            elif col == 3:
                node.price = value


class ModelTable(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
       
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 7

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string',
                  3: 'string',
                  4: 'string',
                  5: 'int',
                  6: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        if not item:
            return True

        return False   
        
    def GetParent(self, item): 
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
            
        
    def GetValue(self, item, col):
        node = self.ItemToObject(item)          
        if isinstance(node, DataTable):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name,
                      3: node.table_type,
                      4: node.area,
                      5: node.people_num,
                      6: node.min_type}
            return mapper[col]
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataTable):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value
            elif col == 3:
                node.table_type = value
            elif col == 4:
                node.area = value
            elif col == 5:
                node.people_num = value
            elif col == 6:
                node.min_type = value


class ModelType(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
         
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        if not item:
            return True
            
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
 
    def GetValue(self, item, col):
        node = self.ItemToObject(item)          
        if isinstance(node, DataType):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False
  
    def SetValue(self, value, item, col):    
        node = self.ItemToObject(item)
        if isinstance(node, DataType):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value


class ModelCategory(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
      
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        if not item:
            return True

        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        node = self.ItemToObject(item)          
        if isinstance(node, DataCategory):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataCategory):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value


class ModelDishes(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
   
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 10

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string',
                  3: 'string',
                  4: 'string',
                  5: 'int',
                  6: 'string',
                  7: 'string',
                  8: 'int',
                  9: 'int',
                  10: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        if not item:
            return True
        
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
  
    def GetValue(self, item, col):
        node = self.ItemToObject(item)          
        if isinstance(node, DataDishes):
            mapper = {0: node.line,
                      1: node.code,
                      2: node.name,
                      3: node.spell,
                      4: node.category,
                      5: node.unit,
                      6: node.stop,
                      10: node.printer_scheme}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataDishes):
            if col == 0:
                node.line = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value
            elif col == 3:
                node.spell = value
            elif col == 4:
                node.spec = value
            elif col == 5:
                node.style = value
            elif col == 6:
                node.category = value
            elif col == 7:
                node.unit = value
            elif col == 8:
                node.price = value
            elif col == 9:
                node.stop = value
            elif col == 10:
                node.printer_scheme = value


class ModelSpec(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
 
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'string',
                  2: 'float'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataSpec):
            mapper = {0: node.key,
                      1: node.name,
                      2: node.price}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")
        
    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataSpec):
            if col == 0:
                node.code = value
            elif col == 1:
                node.name = value
            elif col == 2:
                node.price = value


class ModelStyle(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
  
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'string',
                  2: 'float',
                  3: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
                   
    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataStyle):
            mapper = {0: node.key,
                      1: node.name,
                      2: node.price_add,
                      3: node.amount_add}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")
        
    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataStyle):
            if col == 0:
                node.code = value
            elif col == 1:
                node.name = value
            elif col == 2:
                node.price_add = value
            elif col == 3:
                node.amount_add = value


class ModelUnit(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
   
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem           
        
    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataUnit):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name}
            return mapper[col]
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataUnit):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value


class ModelDepartment(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
        
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataDepartment):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name}
            return mapper[col]
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataDepartment):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value


class ModelEmployee(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
     
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 9

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'string',
                  2: 'string',
                  3: 'string',
                  4: 'string',
                  5: 'int',
                  6: 'string',
                  7: 'string',
                  8: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
  
    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataEmployee):
            if node.sex == 0:
                str_sex = u"男"
            else:
                str_sex = u"女" 
            
            if node.state == 0:
                str_state = u"在职"
            else:
                str_state = u"离职"
                
            mapper = {0: node.line,
                      1: node.code,
                      2: node.name,
                      3: node.department,
                      4: node.duty,
                      5: node.telephone,
                      6: str_sex,
                      7: node.birthday.strftime("%Y-%m-%d") if node.birthday is not None else "",
                      8: str_state}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataEmployee):
            if value == u"男":
                num_sex = 0
            else:
                num_sex = 1
                
            if value == u"在职":
                num_state = 0
            else:
                num_state = 1
                
            if col == 0:
                node.line = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value
            elif col == 3:
                node.department = value
            elif col == 4:
                node.duty = value
            elif col == 5:
                node.telephone = value
            elif col == 6:
                node.sex = num_sex
            elif col == 7:
                node.birthday = value.GetValue().Format("%Y-%m-%d")
            elif col == 6:
                node.set = num_state


class ModelUserRole(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
          
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 6

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string',
                  3: 'string',
                  4: 'string',
                  5: 'bool'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataUserRole):
            mapper = {0: node.line,
                      1: node.key,
                      2: u"默认组" if node.type == '1' else u"自定义组",
                      3: node.name,
                      4: node.desc,
                      5: node.selected}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataUserRole):
            if col == 0:
                node.line = value
            elif col == 1:
                node.key = value
            elif col == 2:
                node.type = '1' if value == u"默认组" else '0'
            elif col == 3:
                node.name = value
            elif col == 4:
                node.desc = value
            elif col == 5:
                node.selected = value

li_func_type = [u"餐厅设置", u"菜品发布", u"员工管理", u"报表中心", u"打印设置", u"系统设置"]


class ModelPermList(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)

        self.data = data
        self.objmapper.UseWeakRefs(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 4

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string',
                  3: 'bool'}
        return mapper[col]

    def GetChildren(self, parent, children):
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)

        return 0

    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True

        # but everything else (the song objects) are not
        return False

    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)
        if isinstance(node, DataPermList):
            mapper = {0: node.line,
                      1: li_func_type[int(node.p_code) - 1],
                      2: node.name,
                      3: node.selected}
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataPermList):
            if col == 0:
                node.line = value
            elif col == 1:
                node.p_code = value
            elif col == 2:
                node.name = value
            elif col == 3:
                node.selected = value


class ModelPrinterScheme(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
    
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 7

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string',
                  3: 'int',
                  4: 'string',
                  5: 'int',
                  6: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):    
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
 
    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataPrinterScheme):
            mapper = {0: node.line,
                      1: node.code,
                      2: node.name,
                      3: bool(node.valid),
                      4: node.scheme_type,
                      5: node.print_count,
                      6: node.backup}
            return mapper[col]
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataPrinterScheme):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value
            elif col == 3:
                node.valid = value
            elif col == 4:
                node.scheme_type = value
            elif col == 5:
                node.print_count = value
            elif col == 6:
                node.backup = value


class ModelSchemeType(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
        self.objmapper.UseWeakRefs(True)
  
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'string'}
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True
            
        # but everything else (the song objects) are not
        return False   
        
    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem
   
    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, DataSchemeType):
            mapper = {0: node.line,
                      1: node.key,
                      2: node.name}
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataSchemeType):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value


class ModelBusinessInfo(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)

        self.data = data
        self.objmapper.UseWeakRefs(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 8

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'int',
                  3: 'float',
                  4: 'float',
                  5: 'float',
                  6: 'float',
                  7: 'string'}
        return mapper[col]

    def GetChildren(self, parent, children):
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)

        return 0

    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True

        # but everything else (the song objects) are not
        return False

    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)
        if isinstance(node, DataBusinessInfo):
            mapper = {0: self.data.index(node),
                      1: node.table_num,
                      2: node.consumer_num,
                      3: node.consume_money,
                      4: node.free_money,
                      5: node.real_money,
                      6: node.average_money,
                      7: node.consume_time.strftime("%Y-%m-%d")}
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataSchemeType):
            if col == 0:
                node.line = value
            elif col == 1:
                node.table_num = value
            elif col == 2:
                node.consumer_num = value


class ModelSalesInfo(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)

        self.data = data
        self.objmapper.UseWeakRefs(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 8

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'int',
                  2: 'int',
                  3: 'float',
                  4: 'float',
                  5: 'float',
                  6: 'string'}
        return mapper[col]

    def GetChildren(self, parent, children):
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)

        return 0

    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True

        # but everything else (the song objects) are not
        return False

    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)
        if isinstance(node, DataSalesInfo):
            mapper = {0: self.data.index(node),
                      1: node.table_num,
                      2: node.consumer_num,
                      3: node.consume_money,
                      4: node.free_money,
                      5: node.real_money,
                      6: node.consume_time.strftime("%Y-%m-%d %H:%M:%S")}
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataSchemeType):
            if col == 0:
                node.line = value
            elif col == 1:
                node.table_num = value
            elif col == 2:
                node.consumer_num = value


class ModelBillboardInfo(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)

        self.data = data
        self.objmapper.UseWeakRefs(True)

    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 8

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {0: 'int',
                  1: 'string',
                  2: 'string',
                  3: 'string',
                  4: 'string',
                  5: 'float',
                  6: 'int',
                  7: 'float'}
        return mapper[col]

    def GetChildren(self, parent, children):
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)

        return 0

    def IsContainer(self, item):
        # The hidden root is a container
        if not item:
            return True

        # but everything else (the song objects) are not
        return False

    def GetParent(self, item):
        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)
        if isinstance(node, DataBillboardInfo):
            mapper = {0: self.data.index(node),
                      1: node.dishes_name,
                      2: node.brevity_code,
                      3: node.dishes_category,
                      4: node.dishes_unit,
                      5: node.sale_count,
                      6: node.average_count,
                      7: node.total_money}
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        node = self.ItemToObject(item)
        if isinstance(node, DataSchemeType):
            if col == 0:
                node.line = value
            elif col == 1:
                node.dishes_name = value
            elif col == 2:
                node.brevity_code = value