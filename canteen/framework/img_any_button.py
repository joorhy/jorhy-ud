#_*_ encoding=utf-8 _*_
#!/usr/bin/env python
import wx
import sys


class ImgAnyButton(wx.Button):
    def __init__(self, parent):
        wx.Button.__init__(self, parent, style=wx.NO_BORDER)
        self.normal_img = None
        self.select_img = None
        self.SetBackgroundColour(wx.Colour(0xff, 0xe9, 0xad))

        self.Bind(wx.EVT_SIZE, self.on_size)

    def on_size(self, event):
        x, y = self.GetClientSize()
        try:
            if self.normal_img is not None and self.select_img is not None:
                self.normal_img.Scale(x, y)
                self.SetBitmap(self.normal_img.ConvertToBitmap())

                self.select_img.Scale(x, y)
                self.SetBitmapPressed(self.select_img)
        except:
            pass

    def set_label(self, normal_img, select_img):
        x, y = self.GetClientSize()
        img_path = sys.path[0] + "\\..\\image\\"
        self.normal_img = wx.Image(img_path + normal_img, wx.BITMAP_TYPE_PNG)
        self.select_img = wx.Image(img_path + select_img, wx.BITMAP_TYPE_PNG)
        self.normal_img.Scale(x, y)
        self.select_img.Scale(x, y)
        self.SetBitmap(self.normal_img.ConvertToBitmap())
        self.SetBitmapPressed(self.select_img.ConvertToBitmap())