#!/usr/bin/env python
#_*_ encoding=utf-8 _*_
from app.front.logic.data import *

import wx
import wx.xrc
import wx.dataview


class ModelFreeTable(wx.dataview.PyDataViewModel):
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
                  5: 'int'}
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
        if isinstance(node, DataTableItem):
            mapper = {0: self.data.index(node) + 1,
                      1: node.table_num,
                      2: node.table_name,
                      3: node.table_type,
                      4: node.table_area,
                      5: node.people_num}
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        # We're not allowing edits in column zero (see below) so we just need
        # to deal with Song objects and columns 1 - 5
        node = self.ItemToObject(item)
        if isinstance(node, DataTableItem):
            if col == 1:
                node.table_num = value
            elif col == 2:
                node.table_name = value
            elif col == 3:
                node.table_type = value
            elif col == 4:
                node.table_area = value
            elif col == 5:
                node.people_num = value


class ModelOrderedDishes(wx.dataview.PyDataViewModel):
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
                  4: 'int',
                  5: 'int',
                  6: 'float',
                  7: 'float',
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
        # Return the item which is this item's parent.
        ##self.log.write("GetParent\n")

        if not item:
            return wx.dataview.NullDataViewItem

        return wx.dataview.NullDataViewItem

    def GetValue(self, item, col):
        # Fetch the data object for this item.
        node = self.ItemToObject(item)
        if isinstance(node, DataOrderedDishesItem):
            mapper = {0: self.data.index(node) + 1,
                      1: node.dishes_name,
                      2: node.dishes_spec,
                      3: node.dishes_unit['vch_name'],
                      4: node.dishes_count,
                      5: node.dishes_retreat_count,
                      6: node.dishes_amount,
                      7: node.dishes_real_amount,
                      8: node.dishes_real_amount - node.dishes_real_amount,
                      9: '',
                      10: node.dishes_code,
                      11: node.dishes_status,
                      12: node.dishes_spec_id,
                      13: node.dishes_style_id,
                      14: node.dishes_spec_discount}
            return mapper[col]

        else:
            raise RuntimeError("unknown node type")

    def GetAttr(self, item, col, attr):
        return False

    def SetValue(self, value, item, col):
        # We're not allowing edits in column zero (see below) so we just need
        # to deal with Song objects and columns 1 - 5
        node = self.ItemToObject(item)
        if isinstance(node, DataOrderedDishesItem):
            if col == 1:
                node.dishes_name = value
            elif col == 2:
                node.dishes_spec = value
            elif col == 3:
                node.dishes_unit = value
            elif col == 4:
                node.dishes_count = value
