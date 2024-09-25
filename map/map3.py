# -*- coding: utf-8 -*-
import sys
import PyQt5
from PyQt5 import *
from PyQt5 import QtCore   #不加此行要报错，上行不是全导入了嘛，没懂
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from turtle import *   #本示例没有使用turtle库无需导入
import time
import math
import copy 
import random
 
#定义主窗口类(继承自QMainWindow)
class MypaintWindow(QMainWindow):  
    def __init__(self):
        super().__init__()
        #self.setGeometry(300, 300, 300, 200)
        self.resize(1600, 905)
        self.setMaximumSize(1428,905)
        self.setWindowTitle('PYQT简易画板')
        self.initUi()
    def initUi(self):
        # 创建状态栏
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('准备')
 
        #创建标签画板(本类要重载继承QLabel)，在窗体右侧，作为画板区域)
        self.label_Draw =  MyLabel(self)
        # 设置label的尺寸
        self.label_Draw.setMaximumSize(600,800)
        self.label_Draw.setGeometry(5, 76, 600, 800)
        #创建标签画板DEMO(本类要重载继承QLabel,在窗体右侧，演示绘画动画）
        self.label_Demo =  MyLabelDemo(self)
        self.label_Demo.setMaximumSize(800,800)
        self.label_Demo.setGeometry(620, 76, 800, 800)
 
        # 把pix_img传递给label
        #self.label_Draw.setPixmap(self.pix)
        # 设置pix_img填充满Label
       # self.label_Draw.label_DrawsetScaledContents(True)
        self.label_Draw.setScaledContents(True)
        self.label_Demo.setScaledContents(True)
        #self.label_Draw.setPixmap(QPixmap("1.jpg"))   #此语句无效，标签同画板绑定后，不会加载外部图像了
        #创建工具栏各按纽控件（并绑定信号到槽函数上）
        toolBar1_Line = QAction(QIcon('t01.png'), '画直线', self)   #工具栏上的按纽用图标文件，是随意的几个，博客中的代码复制到编绎器后，将对应的图形文件copy到PY同目录中并更改此代码中的文件名即可
        toolBar1_Line.setShortcut('Ctrl+L')
        toolBar1_Line.triggered.connect(self.draw_Line)
        toolBar2_Rect = QAction(QIcon('t02.png'), '画矩形', self)
        toolBar2_Rect.setShortcut('Ctrl+R')
        toolBar2_Rect.triggered.connect(self.draw_Rect)
        toolBar3_FillRect = QAction(QIcon('t03.png'), '画填充矩形', self)
        toolBar3_FillRect.setShortcut('Ctrl+I')
        toolBar3_FillRect.triggered.connect(self.draw_FillRect)        
        toolBar4_Circle = QAction(QIcon('t04.png'), '画圆', self)
        toolBar4_Circle.setShortcut('Ctrl+C')
        toolBar4_Circle.triggered.connect(self.draw_Circle)
        toolBar5_Ellptic = QAction(QIcon('t05.png'), '画椭圆', self)
        toolBar5_Ellptic.setShortcut('Ctrl+E')
        toolBar5_Ellptic.triggered.connect(self.draw_Ellptic)
        toolBar6_FreeDraw = QAction(QIcon('t06.png'), '随手画', self)
        toolBar6_FreeDraw.setShortcut('Ctrl+F')
        toolBar6_FreeDraw.triggered.connect(self.FreeDraw)
        toolBar7_Text = QAction(QIcon('t07.png'), '画文本', self)
        toolBar7_Text.setShortcut('Ctrl+T')
        toolBar7_Text.triggered.connect(self.draw_Text)
        toolBar8_Exit = QAction(QIcon('t08.png'), '退出绘图模式', self)
        toolBar8_Exit.setShortcut('Ctrl+Q')
        toolBar8_Exit.triggered.connect(self.draw_Quit)
 
        # 和上面的菜单栏差不多，这里使用了一个行为对象，
        # 这个对象绑定了一个标签，一个图标和一个快捷键。
        # 这些行为被触发的时候，会调用QtGui.QMainWindow的quit方法退出应用。
        self.toolbar = self.addToolBar('画直线')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar1_Line)
 
        self.toolbar = self.addToolBar('画矩形')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar2_Rect)
 
        self.toolbar = self.addToolBar('画填充矩形')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar3_FillRect)
        
        self.toolbar = self.addToolBar('画圆')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar4_Circle)
 
        self.toolbar = self.addToolBar('画椭圆')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar5_Ellptic)
 
        self.toolbar = self.addToolBar('随手画')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar6_FreeDraw)
 
        self.toolbar = self.addToolBar('画文本')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar7_Text)
 
        self.toolbar = self.addToolBar('退出绘图模式')
        self.toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(toolBar8_Exit)
 
        #同时定义一菜单对象
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('文件')
        menu_New = QAction('保存画板', self)
        menu_New.setStatusTip('在状态栏上显示内容:将当前画板中的图像保存到文件')
        fileMenu.addAction(menu_New)
        menu_Load = QMenu('导入', self)
        subMenu_LoadImg= QAction('导入图像', self)
        subMenu_LoadImg.setStatusTip('在状态栏上显示内容:导入一外部图形文件到画板')
        menu_Load.addAction(subMenu_LoadImg)
        fileMenu.addMenu(menu_Load)
 
        mnu_Exit = QAction(QIcon("t08.png"),'退出程序',self)
        mnu_Exit.setShortcut("ctrl+Q")  
        mnu_Exit.setStatusTip('在状态栏上显示内容:退出程序')
        mnu_Exit.triggered.connect(qApp.quit)
        fileMenu.addAction(mnu_Exit)
        sta = self.statusBar()       
 
        # 本例创建了一个行为菜单。这个行为／动作能切换状态栏显示或者隐藏。
        menu_View = menubar.addMenu('选项')
        viewStatAct = QAction('显示/隐藏状态栏', self, checkable=True)
        viewStatAct.setStatusTip('在状态栏上显示内容:视图菜单->显示/隐藏状态栏')        # 用checkable选项创建一个能选中的菜单。
        viewStatAct.setChecked(True)        # 默认设置为选中状态
        viewStatAct.triggered.connect(self.toggleMenu)
        menu_View.addAction(viewStatAct)
    ##############################################################
        self.threadMaxCount=2     #本程序最大可开多线程的数量   
        self.demoClickNum=0   #DEMO标签控件被单击的次数，超出threadMaxCount归0循环（0值即线程全停）
        #定义槽函数，标签DEMO被单击的次数决定启动线程的数量
        #定义线程数组
        self.thread={}
        self.threadOpen=[]   #0索引起用，0对应首个线程
        for i in range(self.threadMaxCount):
            self.threadOpen.append(False)      #定义n个线程打开的状况,供计时器函数中取线程值时使用
            self.thread[i] = ThreadClass(parent=None,index=i)
            self.threadOpen[i]=False   #设置线程暂不打开，单击标签画板后打开
            #self.thread[i].start()
            self.setThreadObj(i,self.label_Demo)  #向线程中传入标签控件实例对象
            self.thread[i].signal_ID.connect(self.my_function)      #将线程1中的自定义信号signal_ID绑定槽函数self.my_function
        self.label_Demo.signal_clicked.connect(self.labDemoClick)         #将自定义的DEMO标签类信号
    #DEMO绘图标签被点击时       
    def labDemoClick(self):
        """if(self.demoClickNum>=self.threadMaxCount):
            self.demoClickNum=0
            for n in range(self.threadMaxCount):
                self.threadOpen[n]=False
                self.thread[n].stop()   #关闭全部线程,原线程发送的信号，对应槽函数未必已经处理完毕,可能还在接收信号
                time.sleep(1)
        for i in range(self.threadMaxCount):
            if(i <= (self.demoClickNum)):
                if(self.threadOpen[i]==False):  #对应线程还没打开，打开此序号线程
                    self.threadOpen[i]=True
                    print(f'单击标签画板：打开线程{i}')
                    self.thread[i].start()
        self.demoClickNum = self.demoClickNum + 1  #DEMO标签控件单击次数+1，好同线程打开数量对应"""
         #上面的行功能没法实现，故又回到只运行一个线程来看绘图演示，多个线程不能实现同时绘图？
        self.thread[0].start()    #线程0中画同心圆DEMO示例
        self.threadOpen[0]=True
        #self.thread[1].start()     #线程1中画彩色文本DEMO示例（只能在一个多线程中依次画，同时用两个及以上线程作画没成功？？）
        #self.threadOpen[1]=True
    #将标签控件画板对象传入线程中
    def setThreadObj(self,index,obj):
        self.thread[index].setObj(obj)
    #绑定线程类中的signal_ID信号对应的槽函数,得到各线程中的变量ID的值(仅示例线程同窗体数据交互，同本示例无关)
    def my_function(self,counter):
        ID = counter
        index = self.sender().index   #在槽函数中被调用，用于获取发出信号的对象，的索引号
        print(f'主窗体接收线程槽函数:{index} 返回整数值{ID}')
        if index == 0:
            pass       
        elif index == 1:
            pass
        elif index == 2:
            pass
        #......
    #在菜单事件中：定义一右键菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        act_New = cmenu.addAction("新建")   #仅示例，新建时不对已画图形作保存等处理，直接清空画板,余同
        print(act_New)
        act_Open = cmenu.addAction("打开")
        print(act_Open)
        act_Quit = cmenu.addAction("退出")
        print(act_Quit)
 
        #关联菜单信号对象
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        #处理对应菜单的响应函数
        if action == act_Quit:
            qApp.quit()            #仅示例，退出时不对是否保存图像作细化处理
        elif action == act_Open:
            print('打开')           #仅示例，没有具体功能代码，自行完善
            value = self.getSet('线型')
            print(value)
        elif action == act_New:
            print('新建')
            self.label_Draw.pix.fill(Qt.white)
            self.label_Draw.repaint()   #清空标签画板上的图形
 
    #对应主菜单：视图-->显示/隐藏状态栏的信号槽函数
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()
    
###################################################################################
    #槽函数：画直线
    def draw_Line(self):
        print('画直线')
        self.label_Draw.draw_Type=1
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
 
    #槽函数：画矩形
    def draw_Rect(self):
        print('画矩形') 
        self.label_Draw.draw_Type=2
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
 
    #槽函数：画矩形
    def draw_FillRect(self):
        print('画填充矩形')   
        self.label_Draw.draw_Type=3
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
 
    #槽函数：画园
    def draw_Circle(self):
        print('画圆')    
        self.label_Draw.draw_Type=4
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
 
    #槽函数：画椭圆
    def draw_Ellptic(self):
        print('画椭圆') 
        self.label_Draw.draw_Type=5
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
 
    #槽函数：随手画
    def FreeDraw(self): 
        print('随手画') 
        self.label_Draw.draw_Type=6
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
 
    #槽函数：画文本
    def draw_Text(self): 
        print('画文本') 
        self.label_Draw.draw_Type=7
        cursor = QCursor(Qt.CrossCursor)
        self.setCursor(cursor)
        #打开文本录入子窗口
        self.subTxtWindow = MyDrawTextWindow()                  #定义的子窗体必须有self，否则会一闪而过
        #tx,ty=self.label_Draw.getTxtEdtPos()
        #self.subTxtWindow.setGeometry(tx,ty,500,250)
        self.subTxtWindow.sig_ToMian.connect(self.getDrawTXT)   #同时定义对应子窗体发送的自定义信号'sig_ToMian'，以便接收子窗体传来的数据
        self.subTxtWindow.exec_()                               #会模态化显示对话框，直至关闭它
        self.update()                             
        #self.subTxtWindow.show()
 
    #槽函数：退出绘图模式    
    def draw_Quit(self): 
        print('退出绘图模式') 
        self.label_Draw.draw_Type=0
        cursor = QCursor(Qt.ArrowCursor)
        self.setCursor(cursor)
        bDrawOK=True           
 
    #自定义槽函数，用于接收画文本内容的子窗口发送信号sig_ToMian和接收传来的数据
    def getDrawTXT(self,dic_data):
        print(f'主窗体接收到sig_ToMian信号和字典变量值:{dic_data}')
        #将数值传给子窗体self.label，以便进行绘画文本
        self.label_Draw.bDrawOK=True
        self.label_Draw.setDrawTXT(dic_data)
####################################################################################################################
#重载标签类1，把标签区域作为画板区域(主窗体左绘画区域)        
class MyLabel(QLabel):
    #鼠标起点，鼠标终点
    lastPoint = QPoint()    #在类函数体外可以不加self前缀，但在函数体名类对象引用时，必须要加self的前缀
    endPoint = QPoint()
    bDrawOK=True           #处理因重载绘图事件过快，可能会多画一此不可预料的杂图,初始化应True，让画布画白底一次
    #初始化
    def __init__(self, text=''):
        super(MyLabel, self).__init__(text)        
        self.setFont(QFont('宋体', 16))  # 设置字体和大小
        self.bLeftMouseKey=False   #定义只鼠标左键才能进行绘画
         #定义绘图的设置（字典数据方式）
        self.dic_Set={'线型':'SolidLine',               #SolidLine=实线   DashLine=虚线  DotLine=点线   DashDotLine=点划线  DashDotDotLine=双点划线  CustomDashLine=自定义线
                '线宽':2,
                '线颜色':'black',                   #black=黑色   red=红色  blue=蓝色.......
                '画刷类型':'SolidPattern',        #SolidPattern=纯色填充  Dense1Pattern=密度样式1   Dense2Pattern=密度样式2... HorPattern=水平线样式 VerPattern=垂直线样式  CrossPattern=交通叉线样式   DiagCrossPattern=倾斜交叉线样式      BDiagPattern=反斜线样式     FDiagPattern倾斜样式 
                '填充色':'blue',
                '文本':'示例文本内容',
                '字体名称':'宋体',
                '字号':16,
                '粗体':False,
                '斜体':False,
                '下划线':False,
                '删除线':False,
                '字体颜色':'red',
                '其他设置自行扩展':''
                }
        #定义文本绘图的设置（字典数据方式）
        self.dic_txt={'文本':'示例文本内容',
                    '字体名称':'宋体',
                    '字号':16,
                    '粗体':False,
                    '斜体':False,
                    '下划线':False,
                    '删除线':False,
                    '字体颜色':'red',
                    '其他设置自行扩展':''
                    }
        self.edtCtlPosX=0   #保存画文本图形时，调出对话框或编辑框控件的左上角位置 
        self.edtCtrlPosY=0
        self.lst_LineType=['实线','虚线','点线','点划线','双点划线','自定义线']
        self.lst_Col=["black", "red", "green", "blue", "purple", "orange", "MediumSlateBlue", "CornflowerBlue",
        "DodgerBlue", "DeepskyBlue", "LightSkyBlue", "SkyBlue", "LightBlue","请自行增加..."]
        self.lst_FillType=['纯色','密度样式1','密度样式2','密度样式3','密度样式4','密度样式5','密度样式6','密度样式7','水平线样式','垂直线样式','交叉线样式','倾斜交叉线样式','反斜线样式','倾斜样式']
        cursor = QCursor(Qt.CrossCursor)  #光标类型
        #定义当前绘画类型
        self.draw_Type=0      #PY中没有枚举，这里采用数字方式比对 0=非绘画模式   1=画线模式 2=画矩形模式 3=画填充矩形模式 4=画圆模式 5=画椭圆模式 6=随手画模式 7=画文本模式
        #在窗体上设置一区域为画布，画布大小为600*600，背景为白色
        self.pix = QPixmap(600, 800)    #实例化QPixmap类
        self.pix.fill(Qt.white)
        # 把pix_img传递给label
        self.setPixmap(self.pix)
        self.noPatter =  QPainter(self.pix).brush()
    #得到画线类型
    def getLineType(self,typeTxt='实线'):   
        linetype=Qt.SolidLine
        if(typeTxt==self.lst_LineType[0]):linetype=Qt.SolidLine
        elif(typeTxt==self.lst_LineType[1]):linetype=Qt.DashLine
        elif(typeTxt==self.lst_LineType[2]):linetype=Qt.DotLine
        elif(typeTxt==self.lst_LineType[3]):linetype=Qt.DashDotLine
        elif(typeTxt==self.lst_LineType[4]):linetype=Qt.DashDotLine
        elif(typeTxt==self.lst_LineType[5]):linetype=Qt.DashDotDotLine
        else: linetype=Qt.SolidLine
        return linetype
    
    #得到填充类型
    def getFillType(self,typeTxt='纯色'):   
        filltype=Qt.SolidPattern
        if(typeTxt==self.lst_FillType[0]):filltype=Qt.SolidPattern
        elif(typeTxt==self.lst_FillType[1]):filltype=Qt.Dense1Pattern
        elif(typeTxt==self.lst_FillType[2]):filltype=Qt.Dense2Pattern
        elif(typeTxt==self.lst_FillType[3]):filltype=Qt.Dense3Pattern
        elif(typeTxt==self.lst_FillType[4]):filltype=Qt.Dense4Pattern
        elif(typeTxt==self.lst_FillType[5]):filltype=Qt.Dense5Pattern
        elif(typeTxt==self.lst_FillType[6]):filltype=Qt.Dense6Pattern
        elif(typeTxt==self.lst_FillType[7]):filltype=Qt.Dense7Pattern
        elif(typeTxt==self.lst_FillType[8]):filltype=Qt.HorPattern
        elif(typeTxt==self.lst_FillType[9]):filltype=Qt.VerPattern
        elif(typeTxt==self.lst_FillType[10]):filltype=Qt.CrossPattern
        elif(typeTxt==self.lst_FillType[11]):filltype=Qt.DiagCrossPattern
        elif(typeTxt==self.lst_FillType[12]):filltype=Qt.BDiagPattern
        elif(typeTxt==self.lst_FillType[13]):filltype=Qt.FDiagPattern 
        else: filltype=Qt.SolidPatter
        return filltype
 
    #设置要绘画的文本内容
    def setDrawTXT(self,dic_data):
        print(f'设置到标签画板类的相绘制的文本数据为:{dic_data}')
        self.dic_txt = dic_data
        for key in dic_data.keys():    #将从子窗体得到的数据更新到设置字典中
            print(dic_data[key])
            self.SetValue(key,dic_data[key])
 
     #得到设置
    def getSet(self,setName):
        if(setName=='线型'): defValue='SolidLine'
        elif(setName=='线宽'): defValue=2
        elif(setName=='线颜色'): defValue='black'
        elif(setName=='画刷类型'): defValue='SolidPattern'
        elif(setName=='填充色'): defValue='blue'
        elif(setName=='文本'): defValue='示例文本内容'
        elif(setName=='字体名称'): defValue='宋体'
        elif(setName=='字号'): defValue=16
        elif(setName=='粗体'): defValue=False
        elif(setName=='斜体'): defValue=False
        elif(setName=='下划线'): defValue=False
        elif(setName=='删除线'): defValue=False
        elif(setName=='字体颜色'): defValue='red'
        else: print('无此设置项')
        value = str(self.dic_Set.get(setName, defValue))
        return value
    
    #运行中设置配置值，此函数没有对异常的处理，可能运行中有BUG
    def SetValue(self,setName,value):
        self.dic_Set[setName]=value
    def setBackgroundColor(self, color):
        pal = self.palette()
        pal.setColor(self.backgroundRole(), QColor(color))
        self.setPalette(pal)
 
    #重载绘图函数：根据选择设置，画不同的图形  #0=非绘画模式   1=画线模式 2=画矩形模式 3=画填充矩形模式 4=画圆模式 5=画椭圆模式 6=随手画模式 7=画文本模式
    def paintEvent(self, event):
        pen = QPen()                     # 创建画笔对象
        brush = QBrush()                # 创建画刷对象
        pp = QPainter(self.pix)
        if(self.draw_Type==6):  #随手画模式:固定画笔，不用随机模式用设置值
            pencol = QColor(self.getSet('线颜色'))
            pen.setWidth(2)   
            pp.setPen(pen)                  # 设置画笔                 
        else:    
            lineType = self.getLineType(self.lst_LineType[random.randrange(0,5)])      #画线类型，随机选一种
            fillType = self.getFillType(self.lst_FillType[random.randrange(0,13)])     #填充类型：随机选一种
            #pencol = QColor(self.getSet('线颜色')) #不用设置色，用随机色
            pencol = QColor(self.lst_Col[random.randrange(0,12)])                      #画笔颜色：随机选一种
            pen.setColor(pencol)                 # 设置画笔颜色为红色
            pen.setStyle(lineType)               # 设置画笔类型
            pen.setWidth(random.randrange(1,8)) # 设置画笔宽度
            #pp.setBrush(QColor(self.getSet('填充色')))  #不用设置的初始值
            brush.setColor(QColor(self.lst_Col[random.randrange(0,12)]))              #画刷颜色为随机选一种
            brush.setStyle(fillType)   
            pp.setPen(pen)                  #设置画笔
            pp.setBrush(brush)              #设置画刷
                  
        x1 = self.lastPoint.x()
        y1 = self.lastPoint.y()
        x2 = self.endPoint.x()
        y2 = self.endPoint.y()
        point1=QPoint(x1,y1)
        point2=QPoint(x2,y2)
        if(self.bDrawOK==False):  #此绘画开关没打开前，避免误画图形
            return
        if(self.draw_Type==1):  #画直线模式
            pp.drawLine(point1, point2)
        elif(self.draw_Type==2):  #画矩形模式
            pp.setBrush(self.noPatter)   #画非填充矩形时:暂没找到透明画刷的得到方法，用的保存了一初始画刷没有加载颜色等时的值
            if(x1<=x2):  #从上往下拖
                pp.drawRect(x1,y1,abs(x2-x1),abs(y2-y1))  
            else:  #从下往上拖
                pp.drawRect(x2,y2,abs(x1-x2),abs(y1-y2)) 
        elif(self.draw_Type==3):  #画填充矩形模式
            if(x1<=x2):  #从上往下拖
                pp.drawRect(x1,y1,abs(x2-x1),abs(y2-y1)) 
            else:  #从下往上拖
                pp.drawRect(x2,y2,abs(x1-x2),abs(y1-y2)) 
        elif(self.draw_Type==4):  #画圆模式
            pp.setBrush(self.noPatter)   #画非填充圆时
            #计算出圆半径，并更改结束点坐标已满足最大圆
            D=min(abs(x2-x1),abs(y2-y1))
            if(x1<=x2):
                x2 = x1+D
                y2 = y1+D
            else:
                x2 = x1 - D
                y2 = y1 - D
            if(x1<=x2):  #从上往下拖
                pp.drawEllipse(x1,y1,abs(x2-x1),abs(y2-y1))  
            else:  #从下往上拖
                pp.drawEllipse(x2,y2,abs(x1-x2),abs(y1-y2)) 
 
        elif(self.draw_Type==5):  #椭圆模式
            pp.setBrush(self.noPatter)   #画非填充圆时
            if(x1<=x2):  #从上往下拖
                pp.drawEllipse(x1,y1,abs(x2-x1),abs(y2-y1))  
            else:  #从下往上拖
                pp.drawEllipse(x2,y2,abs(x1-x2),abs(y1-y2))       
        elif(self.draw_Type==6):  #随手画模式
            # 根据鼠标指针前后两个位置绘制直线
            self.bDrawOK=True
            pp.drawLine(self.lastPoint, self.endPoint)
            # 让前一个坐标值等于后一个坐标值，这样就能实现画出连续的线
            self.lastPoint = self.endPoint
        elif(self.draw_Type==7):  #画文本模式
            #打开一个自定义子窗体，初始化录入文本,也可采用类似CAD方式，在鼠标按下位置创建一编辑框控件实时进行编辑
            print('开始画文本')
            pp.setPen(QColor(self.lst_Col[random.randrange(0,12)]))   # 设置笔的颜色: 随机选一种
            # 设置字体
            pp.setFont( QFont(self.getSet('字体名称'), int(self.getSet('字号'))))   #按设置值
            if(x1<=x2):  #从上往下拖从X1,Y1开始画文本
                #画出文本
                pp.drawText(QRect(x1,y1,abs(x2-x1),abs(y2-y1)), Qt.AlignLeft, self.getSet('文本'))
            else:  #从下往上拖，从X2,Y2开始画文本
                pp.drawText(QRect(x2,y2,abs(x2-x1),abs(y2-y1)), Qt.AlignLeft, self.getSet('文本'))
 
        painter = QPainter(self)
        #绘制画布到窗口指定位置处
        painter.drawPixmap(0, 0, self.pix)
        if(self.draw_Type!=6 or self.draw_Type!=7):
            self.bDrawOK=False
 
    #鼠标按下事件重载   
    def mousePressEvent(self, event):
        if(self.draw_Type!=6  or self.draw_Type!=7):
           self.bDrawOK=False   #关闭重绘事件
        print(f'当前坐标：x={event.pos().x()},y={event.pos().y()}')
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.bLeftMouseKey=True
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
            self.edtCtlPosX = event.pos().x()
            self.edtCtlPosY = event.pos().y()+30  #没对超出屏幕时作坐标处理。。。
        else:
            self.bLeftMouseKey=False
 
    #鼠标移动事件重载          
    def mouseMoveEvent(self, event):  
        print(f'当前坐标：x={event.pos().x()},y={event.pos().y()}')
        if event.buttons() and self.bLeftMouseKey:
            if(self.draw_Type==6):  #仅随手画时要实时得到坐标位置并画出
                self.endPoint = event.pos()
                # 进行重新绘制
                self.bDrawOK=True   #打开重绘事件
                self.update()
            else:
                pass
                #print('非随手画模式请自行增加代码来画一临时虚框显示绘图过程，但不真正绘会出来')
    # 鼠标左键释放        
    def mouseReleaseEvent(self, event):
        print(f'当前坐标：x={event.pos().x()},y={event.pos().y()}')
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            print(f'当前坐标：x={event.pos().x()},y={event.pos().y()}')
            # 进行重新绘制
            self.bDrawOK=True
            self.update()
    #画文本时，返回新建窗体或编辑框控件左上角坐标
    def getTxtEdtPos(self):
        return self.edtCtlPosX,self.edtCtrlPosY
 #########################################################################################################################
#定义一个录入画文本的子窗口
class MyDrawTextWindow(QDialog):
    sig_ToMian = pyqtSignal(object)   #窗体间数据通讯用自定义信号
    def __init__(self):
        #定义绘图的设置（字典数据方式）
        self.dic_txt={'文本':'示例文本内容',
                    '字体名称':'宋体',
                    '字号':16,
                    '粗体':False,
                    '斜体':False,
                    '下划线':False,
                    '删除线':False,
                    '字体颜色':'red',
                    '其他设置自行扩展':''
                    }
        super().__init__()
        self.setWindowTitle('设置要在画板中绘制文本的属性')
        self.resize(500,200)
        layout = QVBoxLayout()
        layout = QFormLayout()
        self.edt_drawTxt = QLineEdit()
        self.edt_drawTxt.setText('示例文本内容')
        self.edt_drawTxt.resize(200,50)
        self.edt_fontname = QLineEdit()
        self.edt_fontname.setText('宋体')
        self.edt_fontname.resize(200,50)
        self.edt_fontsize = QLineEdit()
        self.edt_fontsize.setText('16')
        self.edt_fontsize.resize(200,50)
        self.btn_OK = QPushButton()
        self.btn_OK.setText("确定")
        layout.addRow("请输入所绘文本的内容->",self.edt_drawTxt)
        layout.addRow("请输入所绘文本的字体名称->",self.edt_fontname)
        layout.addRow("请输入所绘文本的字号(整数)->", self.edt_fontsize)
        layout.addRow("仅为示例其他属性设置没有设置对应控件，请自行完善增加->", None)
        layout.addRow("", self.btn_OK)
        self.btn_OK.clicked.connect(self.btnok)
        #仅为示例，其他参数，不再增加控件了，看示例的可自行增加相应控件和对应的变量关联向主窗口中传递即可。。。。。。。。。。。。。。
        self.setLayout(layout)
 
    #得到字典中的值
    def getValue(self,setName):
        if(setName=='文本'): defValue='示例文本内容'
        elif(setName=='字体名称'): defValue='宋体'
        elif(setName=='字号'): defValue=16
        elif(setName=='粗体'): defValue=False
        elif(setName=='斜体'): defValue=False
        elif(setName=='下划线'): defValue=False
        elif(setName=='删除线'): defValue=False
        elif(setName=='字体颜色'): defValue='red'
        else: print('无此字典数据项')
        value = str(self.dic_txt.get(setName, defValue))
        return value    
        
    #运行中设置配置值，此函数没有对异常的处理，可能运行中有BUG
    def SetValue(self,setName,value):
        self.dic_txt[setName]=value
 
     #窗体事件重载
    def event(self, event):
        if event.type() == QEvent.Type.Close:
            print("窗体关闭事件被触发:自动发信号给主窗体接收当前窗体中的变量值")
            self.SetValue('文本',self.edt_drawTxt.text())
            self.SetValue('字体名称',self.edt_fontname.text())
            self.SetValue('字号',self.edt_fontsize.text())
            self.sig_ToMian.emit(self.dic_txt)   #发出信号及数据，等待主窗口的槽函数接收数据
            event.accept()        
        else:
            pass
        return super().event(event)
    
    #单击OK按纽时，关闭窗体,自然触发窗体关闭事件，在关闭事件中发送数据给主窗口接收
    def btnok(self):
       self.close()
#################################################################################################################
##重载标签类2，把标签区域作为画板区域(主窗体右绘画区域),此区域作为画板DEMO示例多线程绘画展示区域        
class MyLabelDemo(QLabel):
     #鼠标起点，鼠标终点
    lastPoint = QPoint(0,0)    #在类函数体外可以不加self前缀，但在函数体名类对象引用时，必须要加self的前缀
    endPoint = QPoint(0,0)
    bDrawOK=True           #处理因重载绘图事件过快，可能会多画一此不可预料的杂图
    signal_clicked = QtCore.pyqtSignal(str)    #自定标签类的信号，即标签被单击时发出(传回参数为标签文本)
    #线条或文本的颜色：实际可在界面用颜色选择框来选择
    lst_col = ["black", "red", "green", "blue", "purple", "orange", "MediumSlateBlue", "CornflowerBlue",
        "DodgerBlue", "DeepskyBlue", "LightSkyBlue", "SkyBlue", "LightBlue"]
    #字体名称：实际可在界面中用字体选择框来选择
    lst_fontname=['宋体','仿宋','黑体','楷体','方正行楷简体','微软雅黑','其他字体...']    #初始化
    def __init__(self, text=''):
        super(MyLabelDemo, self).__init__(text)        
        cursor = QCursor(Qt.CrossCursor)  #光标类型
        self.MyDrawText="本示例为在画板（标签控件）画直线、圆、椭圆、矩形、填充矩形等图形的画板PYTHON+PQ5示例,另一标签控件画板采用多线程上画出复杂同心圆及多彩文字，近期我正在作透明图片在另一画板(底图)可控制操作的移动示例，可能是类似于游戏上的底图为一画板，操作上面的透明小图片进行移动等形成游戏的画面吧。 敬请关注我哦！！！"
        self.lst_drawText=[[]]   #将 MyDrawText文本分解此列表中，每个列表对象中的数据仍是列表，格式为['多','宋体',16,'red',True......][.......]  示例只使用了部份属性功能
        self.splitDrawText(self.MyDrawText)  #调用函数分解字符
        #定义当前绘画类型
        self.pix = QPixmap(800,800)    #实例化QPixmap类
        self.pix.fill(Qt.white)
        self.setPixmap(self.pix)     # 把pix_img传递给label
        pp0 = QPainter(self.pix)
        pp0.drawText(QRect(0,0,500,35),0,'多线程画同心圆和彩色文本的示例,请单击标签画板绘图区域打开多线程查看演示。') 
        self.noPatter =  QPainter(self.pix).brush()        
 
    #重载绘图函数：根据选择设置，画不同的图形  #0=非绘画模式   1=画线模式 2=画矩形模式 3=画填充矩形模式 4=画圆模式 5=画椭圆模式 6=随手画模式 7=画文本模式
    def paintEvent(self, event):
        if(self.bDrawOK==False):  #处理因此函数调用过于频凡造成多画的现象
            return
        x1 = self.lastPoint.x()
        y1 = self.lastPoint.y()
        x2 = self.endPoint.x()
        y2 = self.endPoint.y()
        point1=QPoint(x1,y1)
        point2=QPoint(x2,y2)
        #以下语句运行正常，修改成全局变量
        bPaint=True  #窗体要执行以下代码，线程中暂时规避对painter操作
        painter0 = QPainter(self)   #此QPainter只能有paintEvent中定义，不能定义成类的self成员对象，也不能在其地方(如其他窗口，线程中)定义，否则没有绘画功能显示
        #绘制画布到窗口指定位置处
        #painter0.begin(self)
        pp0 = QPainter(self.pix)
        painter0.drawPixmap(0, 0, self.pix)
        #painter0.end()
        bPaint=False
    #鼠标按下事件重载   
    def mousePressEvent(self, event):
        bDrawOK=True
        print(f'当前鼠标压下坐标：x={event.pos().x()},y={event.pos().y()}')
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint
        self.signal_clicked.emit(self.text())   #在DEMO标签上按下鼠标键后，发送此信号出去，主窗体接收此信号，调用对应定义的槽函数响应
        print(' MyLabelDemo标签类的鼠标被按下，发出信号signal_clicked')
    # 鼠标左键释放        
    def mouseReleaseEvent(self, event):
        print(f'当前鼠标释放坐标：x={event.pos().x()},y={event.pos().y()}')
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 进行重新绘制
            self.update()
        bDrawOK=True
    #分解要画出的文本到列表中
    def splitDrawText(self,drawStr):
        count = len(drawStr)
        x=5   #文字绘制起始点坐标        
        y=30
        row=0  #文字当前行数
        rowMaxY=10 #本行文字中最大的字高
        sumposX=x  #绘制文本累计已占用当前行位置像素 
        sumposY=y
        spaceX=3  #文字间横向间隔
        spaceY=6 #文字竖向间隔
        dpi=96
        #        内容     字号  颜色 加粗 倾斜 下划线 删除线,文字矩形左上角x,y,文字矩形宽度,高度,对齐方式.....
        #         0   1    2   3     4   5    6     7  8 9 10 11  12...            
        lst_one=['','宋体',16,'red',True,True,True,True,0,0,0,0,'AlignLeft']
        if count>0:
            self.lst_drawText.clear()
            lst_str = list(drawStr)  #按单字分解字符串到列表对象
            for i in range(count):
                lst_one[0]=lst_str[i]
                lst_one[1]=self.lst_fontname[random.randint(0, 5)]  #随机得到字体名称
                #仅示例：对字体的x,y,w,h进行处理
                lst_one[2]=random.randint(15, 24)  #随机得到字号
                lst_one[8]=sumposX
                lst_one[9]=sumposY
                lst_one[10]=self.points_to_pixels(lst_one[2],dpi)+spaceX    #没有详细分析字号同屏幕像素及DPI的关系。。。
                lst_one[11]=lst_one[10]
                if(rowMaxY<lst_one[11]):
                    rowMaxY = lst_one[11]
                lst_one[12]='AlignLeft'
                sumposX=sumposX+lst_one[2]+spaceX
                if(sumposX>770): #本画布宽度是800，故设成790换行，
                    row=row+1
                    sumposX=0
                    x=5
                    y=row*40+spaceY
                    sumposY=sumposY+rowMaxY+spaceY
                
                if(i==2 or(i>=8 and i<=11)):  #这几个是数字要处理
                    pass
                elif(i>=4 and i<=7):          #这几个是bool值要处理
                   pass 
                else:
                    pass
                self.lst_drawText.append(copy.deepcopy(lst_one))  #必须用深度copy防止列表中的内容都是最后一个字的内容现象
            print(self.lst_drawText)
    #字号同像素点的转换
    def points_to_pixels(self,points, dpi):
        return points * dpi / 72.0
    def pixels_to_points(self,pixels, dpi):
        return pixels * 72.0 / dpi
 
#########################################################################################################################
#自定义线程类(继承QT的多线程类QtCore.QThread，不是PYTHON的线程类)
class ThreadClass(QtCore.QThread):
    signal_ID = QtCore.pyqtSignal(int) #自定义线程中的信号，名称为signal_ID
    ID=0
    x0=400
    y0=400
    bRealseAll=False
    def __init__(self,parent=None,index=0):
        super(ThreadClass,self).__init__(parent)
        self.index = index
        self.is_running = True
        self.ID=0
    #重载开始线程对应的run函数:本例根据鼠标点击画板（标签控件）的次数来决定运行几个多线程DEMO
    def run(self):
        self.obj.bDrawOK=True
        print(f'开始线程...:线程索引号：{self.index}')
        self.is_running = True
        while(True):   #线程重复不断的循环来
            if self.ID>99: self.ID=0   #ID对本代码无用，仅为信号槽传回整数作示例
            self.signal_ID.emit(self.ID)   #将本线程中的ID值(0-99)通过信号signal_ID槽发送，接收端通过
            if(self.index==0):      #线程0画以下DEM0代码 
                self.dem1_drawText()         #画彩色文本
                self.dem0_drawCircle()   #画同心圆
                self.dem1_RealseText(QColor(255,255,255))  #用白色画笔擦除彩色文本(擦除不是太干净待优化)
                time.sleep(3)
                self.obj.pix.fill(Qt.white)  #全部擦除画板
            elif(self.index==1):            #线程1画以下DEM0代码，只能在一个线程中依次画，两个及以上线程同时画没成功？？)
                time.sleep(1)  
            elif(self.index==2):            #线程2画以下DEM0代码
                time.sleep(1)                
            #自行扩展对各线程的响应代码......
            else:
                time.sleep(1)                 #1000毫秒间隔
    #多线程绘画DEMO1:参数bRealseAll表示调用前是否擦除全部画布内容
    def dem0_drawCircle(self):
        print('多线程0绘画DEM0：绘制同心圆') 
        #painter = QPainter(self.obj)  #paniter对象只能在重绘事件中，在多线程中不会作用
        pp = QPainter(self.obj.pix)
        pencol = QColor(255,0,255)
        pp.setPen(pencol)
        pLeft=0
        pRight=0
        cx0=0
        cy0=0
        #绘制画布到窗口指定位置处:以下为在序号为0的线程中绘制一复杂图像代码
        #先擦除窗口上的图(本例擦除全部)
        #self.obj.pix = QPixmap(800,800) 
        R=30  #绘圆半径   
        count = 60  #第一圈绘60个，以后每圈翻倍
        for j in range(12):     #绘制的圈数
            pencol=QColor(self.obj.lst_col[j])
            pp.setPen(pencol)
            for i in range(count*(j+1)):   #每圈绘制的圆个数
                time.sleep(0.01)   #画每个圆的时间间隔为10毫秒
                #计算每个圆的矩形左上角位置
                dx0,dy0=self.getRectPoint(R*j,i,count*(j+1),R)
                pp.drawEllipse(dx0,dy0,2*R,2*R)
                self.ID+=self.ID    #本线程绘的图形计数
                self.obj.update()       #刷新调用画板的重绘事件函数
            self.obj.update()       #刷新调用画板的重绘事件函数
    #多线程绘画DEM1
    def dem1_drawText(self):
        print('多线程1绘画DEM1:绘制彩色文本')    
        #绘制画布到窗口指定位置处:以下为在序号为0的线程中绘制一复杂图像代码
        #先擦除窗口上的图(本例擦除全部)
        #self.obj.pix = QPixmap(800,800) 
        pp = QPainter(self.obj.pix)
        pencol = QColor(255,0,255)
        pp.setPen(pencol)
        pLeft=0
        pRight=0
        cx0=0
        cy0=0
        self.ID=0
        #self.obj.pix.fill(Qt.white)
        for j in range(len(self.obj.lst_drawText)):     #绘制的文字个数
            time.sleep(0.2)
            pencol=QColor(self.obj.lst_col[random.randint(0,12)])  #颜色随机并没有用字的列表中的属性，请自行完善
            pp.setFont(QFont(self.obj.lst_drawText[j][1], int(self.obj.lst_drawText[j][2])))
            pp.setPen(pencol)
            #pp.drawText(self.obj.lst_drawText[j][0])
            pp.drawText(QRect(self.obj.lst_drawText[j][8],self.obj.lst_drawText[j][9],self.obj.lst_drawText[j][10],self.obj.lst_drawText[j][11]), Qt.AlignLeft, self.obj.lst_drawText[j][0])
            self.obj.update()       #刷新调用画板的重绘事件函数
            self.ID+=self.ID    #本线程绘的图形计数
        self.obj.update()       #刷新调用画板的重绘事件函数
    #将dem1_drawText画的文本擦除(默认采用白色擦除，即擦除色同画板背景色一致)，擦除的不是太干净未处理。。。
    def dem1_RealseText(self,pencol=QColor(255,255,255)):
        print('多线程1绘画DEM1:绘制彩色文本')    
        #绘制画布到窗口指定位置处:以下为在序号为0的线程中绘制一复杂图像代码
        #先擦除窗口上的图(本例擦除全部)
        #self.obj.pix = QPixmap(800,800) 
        pp = QPainter(self.obj.pix)
        pp.setPen(pencol)
        pLeft=0
        pRight=0
        cx0=0
        cy0=0
        self.ID=0
        #self.obj.pix.fill(Qt.white)
        for j in range(len(self.obj.lst_drawText)):     #绘制的文字个数
            time.sleep(0.01) 
            pp.setFont(QFont(self.obj.lst_drawText[j][1], int(self.obj.lst_drawText[j][2])))
            #pp.drawText(self.obj.lst_drawText[j][0])
            pp.drawText(QRect(self.obj.lst_drawText[j][8],self.obj.lst_drawText[j][9],self.obj.lst_drawText[j][10],self.obj.lst_drawText[j][11]), Qt.AlignLeft, self.obj.lst_drawText[j][0])
            self.ID+=self.ID    #本线程绘的图形计数
            self.obj.update()       #刷新调用画板的重绘事件函数
        self.obj.update()       #刷新调用画板的重绘事件函数
    #停止指定线程
    def stop(self):
        self.is_running=False
        print('停止线程...',self.index)
        self.terminate()
 
    #根据圆心轨迹半径，序号，圆数量,圆半径计算矩形左上角坐标
    def getRectPoint(sef,dR,index,count,r):
        a=float(360/count)
        ang1=math.radians(360/count)
        curAng=ang1*index
        rectLeft=0
        rectTop=0
        L=float(dR*math.sin(curAng))
        H=float(dR*math.cos(curAng))
        cx0=400+L
        cy0=400-H
        rectLeft=cx0-r
        rectTop=cy0-r
        return rectLeft,rectTop   #返回画圆的左角坐标点
 
    #线程中自定义函数供外部调用线程中的变量值
    def getID(self):
        return self.index,self.ID
    #在线程中导入需要操作的对象
    def setObj(self,frmobj):
        self.obj = frmobj
 
#########################################################################################################################
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MypaintWindow()
    form.show()
    sys.exit(app.exec())
 