import wx
import sys


class ImgButton(wx.Button):
    def __init__(self, parent, normal_img, select_img, disable_img="", back_ground=wx.Colour(208, 77, 40)):
        wx.Button.__init__(self, parent, style=wx.NO_BORDER | wx.TRANSPARENT_WINDOW)
        img_path = sys.path[0] + "\\..\\image\\"
        self.normal_img = wx.Image(img_path + normal_img, wx.BITMAP_TYPE_PNG)
        self.select_img = wx.Image(img_path + select_img, wx.BITMAP_TYPE_PNG)

        self.disable_img = None
        if disable_img != "":
            self.disable_img = wx.Image(img_path + disable_img, wx.BITMAP_TYPE_PNG)

        if back_ground is not None:
            self.SetBackgroundColour(back_ground)

        self.Bind(wx.EVT_SIZE, self.on_size)
        #self.Bind(wx.EVT_PAINT, self.on_paint)

    def on_size(self, event):
        event.Skip()
        x, y = self.GetClientSize()
        try:
            self.normal_img.Scale(x, y)
            self.select_img.Scale(x, y)

            self.SetBitmap(self.normal_img.ConvertToBitmap())
            self.SetBitmapPressed(self.select_img.ConvertToBitmap())
            if self.disable_img is not None:
                self.SetBitmapDisabled(self.disable_img.ConvertToBitmap())
            else:
                self.SetBitmapDisabled(self.normal_img.ConvertToBitmap())
        except Exception, ex:
            print Exception, ":", ex

    def on_paint(self, event):
        event.Skip()
        dc = wx.ClientDC(self)
        dc.Clear()

        sz = self.GetClientSize()
        bg_img = wx.Image(sys.path[0] + "\\..\\image\\top_bg.png", wx.BITMAP_TYPE_PNG).Scale(sz.x, 82)
        bg_bmp = bg_img.ConvertToBitmap()

        mem_dc = wx.MemoryDC()
        mem_dc.SelectObject(bg_bmp)
        dc.Blit(0, 0,
                bg_bmp.GetWidth(), bg_bmp.GetHeight(),
                mem_dc, 0, 0, wx.COPY, True)