import os
import wx
class MyFrame(wx.Frame):
	def __init__(self,parent,title):
		wx.Frame.__init__(self,parent,title=title,size=(500,500))
		wx.control=wx.TextCtrl(self,style=wx.TE_MULTILINE)
	#	self.CreateStatusBar()
		fileMenu=wx.Menu()
		menuAbout=fileMenu.Append(wx.ID_ABOUT,"&about")
		fileMenu.AppendSeparator()
		menuKuchBhi=fileMenu.Append(wx.ID_OPEN,"&Kuch Bhi",'',wx.ITEM_CHECK)
		fileMenu.AppendSeparator()
		menuSaveAs=fileMenu.Append(wx.ID_ANY,"&SaveAs")
		fileMenu.AppendSeparator()
		menuSave=fileMenu.Append(wx.ID_ANY,"&Save")
		fileMenu.AppendSeparator()
		menuExit=fileMenu.Append(wx.ID_EXIT,"&Exit")
		menuBar= wx.MenuBar()
		menuBar.Append(fileMenu,"&File")	
		menuBar.SetBackgroundColour("green")
	#	menuBar2=wx.MenuBar()
		#vbox = wx.BoxSizer(wx.VERTICAL)
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU, self.OnAbout,menuAbout)
		self.Bind(wx.EVT_MENU, self.OnExit,menuExit)
		self.Bind(wx.EVT_MENU, self.OnOpen,menuKuchBhi)
		self.Bind(wx.EVT_MENU, self.OnSaveAs,menuSaveAs)
		self.Bind(wx.EVT_MENU, self.OnSave,menuSave)		
		self.Show(True)
	#toolbar experiments
		toolBar=self.CreateToolBar()
		ntool=toolBar.AddLabelTool(1,'New',wx.Bitmap('stock_new.png'))
		stool=toolBar.AddLabelTool(2,'Save',wx.Bitmap('stock_save.png'))
		toolBar.Realize()
		self.Bind(wx.EVT_TOOL,self.OnSave,stool)
		self.Bind(wx.EVT_TOOL,self.OnNew,ntool)
	#status bar
		self.statusBar=self.CreateStatusBar() 
	#	self.statusBar.SetStatusText()
	def OnNew(self,e):
		nfile=open("noname.txt","w+")
		self.filename='noname.txt'
		wx.control.SetValue(nfile.read())
		nfile.close()
		self.statusBar.SetStatusText('New File')
	def OnSaveAs(self,e):
		dlg=wx.FileDialog(self,style=wx.SAVE)
		dlg.ShowModal()
		self.dirname=dlg.GetDirectory()
		self.filename=dlg.GetFilename()
	#	self.SetTitle()	           
		dlg.Destroy()      
 		textfile = open(os.path.join(self.dirname, self.filename), 'w')
        	textfile.write(wx.control.GetValue())
        	textfile.close()
		self.statusBar.SetStatusText('Saving File')
	def OnSave(self,e):
		t=open(os.path.join(self.dirname,self.filename),'w')
		t.write(wx.control.GetValue())
		t.close()
		self.statusBar.SetStatusText('Saving File')
	def OnAbout(self, e):
		dlg=wx.MessageDialog(self,"mera khud ka editor h bc!!","editor k bare me",wx.CANCEL)
		dlg.ShowModal()
		dlg.Destroy()
	def OnExit(self,e):	
		self.Close(True)
	def OnOpen(self,e):
             """ Open a file"""
   	     self.dirname = ''
   	     dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
   	     if dlg.ShowModal() == wx.ID_OK:
   	         self.filename = dlg.GetFilename()
   	         self.dirname = dlg.GetDirectory()
   	         f = open(os.path.join(self.dirname, self.filename), 'r')
   	         wx.control.SetValue(f.read())
   	         f.close()
   	     dlg.Destroy()
	     self.statusBar.SetStatusText('reading file')	
app=wx.App(False)
frame=MyFrame(None , 'MeraEditor2')
app.MainLoop()		
