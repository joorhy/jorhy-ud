#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import wx
import wx.xrc
import wx.dataview
from app.logic.dining_room.CDataType import CDataType

class CModelType(wx.dataview.PyDataViewModel):
    def __init__(self, data):
        wx.dataview.PyDataViewModel.__init__(self)
        
        self.data = data
       
        # The objmapper is an instance of DataViewItemObjectMapper and is used
        # to help associate Python objects with DataViewItem objects. Normally
        # a dictionary is used so any Python object can be used as data nodes.
        # If the data nodes are weak-referencable then the objmapper can use a
        # WeakValueDictionary instead. Each PyDataViewModel automagically has
        # an instance of DataViewItemObjectMapper preassigned. This
        # self.objmapper is used by the self.ObjectToItem and
        # self.ItemToObject methods used below.
        self.objmapper.UseWeakRefs(True)

                
    # Report how many columns this model provides data for.
    def GetColumnCount(self):
        return 3

    # Map the data column numbers to the data type
    def GetColumnType(self, col):
        mapper = {  0 : 'int',
                    1 : 'int',
                    2 : 'string',
                 }
        return mapper[col]
        
    def GetChildren(self, parent, children):  
        # The view calls this method to find the children of any node in the
        # control. There is an implicit hidden root node, and the top level
        # item(s) should be reported as children of this node. A List view
        # simply provides all items as children of this hidden root. A Tree
        # view adds additional items as children of the other items, as needed,
        # to provide the tree hierachy.
        ##self.log.write("GetChildren\n")
        
        # If the parent item is invalid then it represents the hidden root
        # item, so we'll use the genre objects as its children and they will
        # end up being the collection of visible roots in our tree.
        if not parent:
            for genre in self.data:
                children.append(self.ObjectToItem(genre))
            return len(self.data)
        
        return 0
        
    def IsContainer(self, item):
        # Return True if the item has children, False otherwise.
        ##self.log.write("IsContainer\n")
        
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
        # Return the value to be displayed for this item and column. For this
        # example we'll just pull the values from the data objects we
        # associated with the items in GetChildren.
        
        # Fetch the data object for this item.
        node = self.ItemToObject(item)          
        if isinstance(node, CDataType):
            mapper = {  0 : node.id,
                        1 : node.code,
                        2 : node.name,
                     }
            return mapper[col]
        
        else:
            raise RuntimeError("unknown node type")
        


    def GetAttr(self, item, col, attr):
        ##self.log.write('GetAttr')
        return False
    
    
    def SetValue(self, value, item, col):
        # We're not allowing edits in column zero (see below) so we just need
        # to deal with Song objects and cols 1 - 5
        
        node = self.ItemToObject(item)
        if isinstance(node, CDataType):
            if col == 0:
                node.id = value
            elif col == 1:
                node.code = value
            elif col == 2:
                node.name = value

