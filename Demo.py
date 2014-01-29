#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2014, gamesun
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#     * Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above
# copyright notice, this list of conditions and the following disclaimer
# in the documentation and/or other materials provided with the
# distribution.
#     * Neither the name of gamesun nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY GAMESUN "AS IS" AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL GAMESUN BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#

#
# This is an example of using the popupColorSelector.
#


import wx
import PopupColorSelector


import wx

class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.btnSelectColor = wx.Button(self.panel_1, wx.ID_ANY, "Select Color")
        self.txtCtlLog = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.HSCROLL | wx.VSCROLL | wx.TE_LINEWRAP | wx.TE_WORDWRAP)

        self.__set_properties()
        self.__do_layout()

    def __set_properties(self):
        self.SetTitle("PopupColorSelector Demo")
        self.panel_1.SetMinSize((400,80))
        self.txtCtlLog.SetMinSize((400, 200))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(self.btnSelectColor, 0, wx.ALL, 20)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 0, wx.EXPAND, 0)
        sizer_1.Add(self.txtCtlLog, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()

class App(wx.App):
    def __init__(self):
        wx.App.__init__(self, redirect=False)

    def OnInit(self):
        self.frame = MyFrame(None)

        self.frame.btnSelectColor.Bind(wx.EVT_BUTTON, self.OnBtnSelectColor)
        self.frame.Bind(PopupColorSelector.EVT_COLOR_SELECT, self.OnColorSelect)

        self.frame.Center()
        self.frame.Show(True)

        return True

    def OnBtnSelectColor(self, evt):
        win = PopupColorSelector.PopupColorSelector(self.frame)
        pos = wx.GetMousePosition()
        win.Position(pos, (0, 0))
        win.Popup()

    def OnColorSelect(self, evt):
        color = evt.color
        str = "You selected:(%d, %d, %d)\n" % (color.Red(),color.Green(),color.Blue())
        print str,
        self.frame.txtCtlLog.AppendText(str)

if __name__ == '__main__':
    app = App()
    app.MainLoop()
