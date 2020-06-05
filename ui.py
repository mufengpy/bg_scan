# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"御剑2020 by 沐风598779784", pos=wx.DefaultPosition,
                          size=wx.Size(714, 548), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetFont(wx.Font(11, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "华文中宋"))

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"域名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)

        bSizer2.Add(self.m_staticText1, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_textCtrl2, 19, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.m_button1 = wx.Button(self, wx.ID_ANY, u"开始扫描", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button1, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self, wx.ID_ANY, u"停止扫描", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button11, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, u"线程：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)

        bSizer3.Add(self.m_staticText11, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_VERTICAL, 5)

        m_choice1Choices = [u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8"]
        self.m_choice1 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice1Choices, 0)
        self.m_choice1.SetSelection(1)
        bSizer3.Add(self.m_choice1, 1, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), 0)
        self.m_staticText7.Wrap(-1)

        bSizer3.Add(self.m_staticText7, 1, wx.ALL, 5)

        self.m_staticText12 = wx.StaticText(self, wx.ID_ANY, u"超时：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText12.Wrap(-1)

        bSizer3.Add(self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP | wx.BOTTOM | wx.EXPAND, 5)

        m_choice11Choices = [u"1", u"2", u"3", u"4", u"5", u"6", u"7", u"8"]
        self.m_choice11 = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice11Choices, 0)
        self.m_choice11.SetSelection(2)
        bSizer3.Add(self.m_choice11, 1, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, u"(秒 超时页面被丢弃)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)

        bSizer3.Add(self.m_staticText4, 3, wx.ALL, 5)

        bSizer1.Add(bSizer3, 0, wx.EXPAND, 5)

        bSizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"DIR:1153", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox1.SetValue(True)
        bSizer4.Add(self.m_checkBox1, 1, wx.ALL, 5)

        self.m_checkBox12 = wx.CheckBox(self, wx.ID_ANY, u"PHP:1066", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox12.SetValue(True)
        bSizer4.Add(self.m_checkBox12, 1, wx.ALL, 5)

        self.m_checkBox11 = wx.CheckBox(self, wx.ID_ANY, u"ASP:1854", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer4.Add(self.m_checkBox11, 1, wx.ALL, 5)

        bSizer1.Add(bSizer4, 0, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox111 = wx.CheckBox(self, wx.ID_ANY, u"MDB:419", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_checkBox111, 1, wx.ALL, 5)

        self.m_checkBox112 = wx.CheckBox(self, wx.ID_ANY, u"JSP:631", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_checkBox112, 1, wx.ALL, 5)

        self.m_checkBox2 = wx.CheckBox(self, wx.ID_ANY, u"ASPX:822", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.m_checkBox2, 1, wx.ALL, 5)

        bSizer1.Add(bSizer5, 0, wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_checkBox3 = wx.CheckBox(self, wx.ID_ANY, u"探测200", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox3.SetValue(True)
        bSizer6.Add(self.m_checkBox3, 1, wx.ALL, 5)

        self.m_checkBox31 = wx.CheckBox(self, wx.ID_ANY, u"探测3XX", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_checkBox31.SetValue(True)
        bSizer6.Add(self.m_checkBox31, 1, wx.ALL, 5)

        self.m_checkBox113 = wx.CheckBox(self, wx.ID_ANY, u"探测4XX", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_checkBox113, 1, wx.ALL, 5)

        bSizer1.Add(bSizer6, 0, wx.EXPAND, 5)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(12, 2)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.SetColSize(0, 511)
        self.m_grid1.SetColSize(1, 64)
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer7.Add(self.m_grid1, 0, wx.ALL | wx.EXPAND, 5)

        bSizer1.Add(bSizer7, 1, wx.ALIGN_CENTER | wx.ALL | wx.EXPAND, 5)

        self.m_gauge1 = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(-1, 30), wx.GA_HORIZONTAL)
        bSizer1.Add(self.m_gauge1, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.OnstartScan)
        self.m_button11.Bind(wx.EVT_BUTTON, self.OnstopScan)

        self.initUI()

    def __del__(self):
        pass
