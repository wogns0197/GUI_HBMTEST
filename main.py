import sys,os,shutil,time
import readme
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI import Ui_MainWindow,Ui_PopupWindow,Ui_Analyzing



class Main(QMainWindow,Ui_MainWindow,Ui_PopupWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.label.resize(500,300)
		self.pixmap = QPixmap("images/SINGLE_SELECT.png")
		self.pixmap = self.pixmap.scaled(500,300)
		self.label.setPixmap(QPixmap(self.pixmap))
		self.pushButton_5.setDisabled(True)
		self.modebutton = 0
		self.isSingle = True
		self.blist = [self.pushButton,self.pushButton_2,self.pushButton_3,self.pushButton_4,self.pushButton_5]
		self.tblist = [self.textBrowser,self.textBrowser_2,self.textBrowser_3,self.textBrowser_4,self.textBrowser_5,self.textBrowser_6]
		self.checkBoxlist = [self.checkBox,self.checkBox2,self.checkBox3,self.checkBox4,self.checkBox5,self.checkBox6,self.checkBox7]
		self.ischecked_list = [False for i in range(7)]
		self.checkbox_limit=0	
		self.clock = 0
		self.time = 0
		self.current_clock = 0
		self.clock2 = 0
		self.time2 = 0
		self.current_clock2 = 0
		self.filename = ""
		self.filename2 = ""
		self.file_len = 0
		self.file_len2 = 0
		
	
	# Select test mode {default: SINGLE}
	def pbclicked1(self):
		self.clear_all()
		if (self.label_3.text() == "PARALLEL"):
			self.pixmap = QPixmap("images/SINGLE.png")
			self.label.setPixmap(QPixmap(self.pixmap))
			self.pixmap = self.pixmap.scaled(500,300)
			self.label.repaint()
			self.label_3.setText("SINGLE")
			self.label_3.repaint()
			self.isSingle = True
			
		else:
			self.pixmap = QPixmap("images/PARALLEL.png")
			self.label.setPixmap(QPixmap(self.pixmap))
			self.label.repaint()
			self.label_3.setText("PARALLEL")
			self.label_3.repaint()
			self.isSingle = False
		
	# Run DRAM + Base die Logic
	def pbclicked2(self):
		self.clear_all()
		self.but_pressed(2)

		self.pixmap = QPixmap("images/WHOLE.png")
		self.label.setPixmap(QPixmap(self.pixmap))
		self.label.repaint()

	# Run Base die Logic
	def pbclicked3(self):
		self.clear_all()
		self.but_pressed(3)
	
		self.pixmap = QPixmap("images/BASE.png")
		self.label.setPixmap(QPixmap(self.pixmap))
		self.label.repaint()

	# Run DRAM
	def pbclicked4(self):
		self.clear_all()
		self.but_pressed(4)

		self.pixmap = QPixmap("images/DRAM.png")
		self.label.setPixmap(QPixmap(self.pixmap))
		self.label.repaint()

	def pbclicked5(self):
		self.disable_all()
		self.ing = 0
		self.ing2 = 0
		self.clock = 0
		self.clock2= 0
		self.time = 0.200701065
		self.time2 = 0.200701065

		if(os.path.isdir('./log') == 0):
			os.mkdir('log')
		if(os.path.isdir('./log/single') == 0):
			os.mkdir('log/single')
		if(os.path.isdir('./log/parallel') == 0):
			os.mkdir('log/parallel')

		#Mode log path select & set Path sting-----
		self.filename = "./log"
		self.filename2 = "./log"
		if(self.isSingle):
			self.filename += "/single"
			if(self.modebutton==2):
				self.filename += "/wholechip.txt"
			elif(self.modebutton==3):
				self.filename += "/basedie.txt"
			else:
				self.filename += "/DRAM.txt"

		else:
			self.filename += "/parallel"
			self.filename2 += "/parallel"
			if(self.modebutton==2):
				self.filename += "/wholechip.txt"
				self.filename2 += "/wholechip2.txt"
			elif(self.modebutton==3):
				self.filename += "/basedie.txt"
				self.filename2 += "/basedie2.txt"
			else:
				self.filename += "/DRAM.txt"
				self.filename2 += "/DRAM2.txt"

		with open(self.filename) as file_object:
			self.file_contents = file_object.readlines()
			self.file_len = len(self.file_contents)

		if(not self.isSingle):
			with open(self.filename2) as file_object:
				self.file_contents2 = file_object.readlines()
				self.file_len2 = len(self.file_contents2)

		self.progressBar.setRange(0,self.file_len-1) #set pgbar max
		
		while(self.ing < self.file_len or self.ing2 < self.file_len2):			
			self.progressBar.setValue(max(self.ing, self.ing2))
			self.progressBar.repaint()
			QApplication.processEvents() 					
			# ------------------Main print------------------	
			if(self.ing < self.file_len-1):
				self.current_clock = self.inst(self.file_contents[self.ing])		
				self.clock += self.current_clock
				self.time += self.current_clock * 0.00000002
			if(self.ing2 < self.file_len2-1):
				self.current_clock2 = self.inst(self.file_contents2[self.ing2])		
				self.clock2 += self.current_clock2
				self.time2 += self.current_clock2 * 0.00000002
			
			try:
				self.textBrowser.append(self.file_contents[self.ing])
				self.textBrowser.repaint()
				self.textBrowser_3.setPlainText(str(self.clock)) #INTEST,EXTEST,MBIST
				self.textBrowser_3.repaint()				
				self.textBrowser_4.setPlainText( str(self.time *1000 ));
				self.textBrowser_4.repaint()

				if(self.label_3.text() == "PARALLEL"):
					self.textBrowser_2.append(self.file_contents2[self.ing2])
					self.textBrowser.repaint()
					self.textBrowser_5.setPlainText(str(self.clock2))
					self.textBrowser_5.repaint()
					self.textBrowser_6.setPlainText( str(self.time2 *1000 ));
					self.textBrowser_6.repaint()
				
			except IndexError:
				pass
			self.ing +=1
			self.ing2 +=1

			# -----------------------------------------------

		self.progressBar.setValue(max(self.file_len-1, self.file_len2-1))	
		
		if(self.modebutton ==2 or self.modebutton ==4):
			if(self.isSingle):
				self.pop = Popup()
				self.pop.textBrowser_pop_2.setStyleSheet("font-size : 20px;")
				self.tmp = []
				for i in range(7):
					if(self.ischecked_list[i]):
						self.tmp.append(i)
				self.pop.textBrowser_pop_2.setPlainText("chip "+str(self.tmp[0]))							
				self.pop.textBrowser_pop.setPlainText("\n clock : "+
					str(self.clock) + "\n time : "+str(self.time*1000)+" ms")
				self.pop.show()
			else:
				self.pop2 = Popup2()
				self.pop2.textBrowser_pop_2.setStyleSheet("font-size : 20px;")
				self.tmp = []
				for i in range(7):
					if(self.ischecked_list[i]):
						self.tmp.append(i)
				self.pop2.textBrowser_pop_2.setPlainText("chip "+str(self.tmp[0]))							
				self.pop2.textBrowser_pop.setPlainText("\n clock : "+
					str(self.clock) + "\n time : "+str(self.time*1000)+" ms")
				self.pop2.show()

				if(self.label_3.text() == "PARALLEL"):
					self.pop2_2 = Popup2_2()
					self.pop2_2.textBrowser_pop_2.setStyleSheet("font-size : 20px;")
					self.pop2_2.textBrowser_pop_2.setPlainText("chip "+str(self.tmp[1]))		
					self.pop2_2.textBrowser_pop.setPlainText("\n clock : "+
					str(self.clock) + "\n time : "+str(self.time*1000)+" ms")
					self.pop2_2.show()
		else:
			if(self.isSingle):
				self.pop = Popup_logic()
				self.pop.nextButton.setText("Quit")
				self.pop.textBrowser_pop_2.setStyleSheet("font-size : 20px;")
				self.tmp = []
				for i in range(7):
					if(self.ischecked_list[i]):
						self.tmp.append(i)
				self.pop.textBrowser_pop_2.setPlainText("chip "+str(self.tmp[0]))							
				self.pop.textBrowser_pop.setPlainText("\n clock : "+
					str(self.clock) + "\n time : "+str(self.time*1000)+" ms")
				self.pop.show()
			else:
				self.pop2 = Popup_logic()
				self.pop2.nextButton.setText("Quit")
				self.pop2.textBrowser_pop_2.setStyleSheet("font-size : 20px;")
				self.tmp = []
				for i in range(7):
					if(self.ischecked_list[i]):
						self.tmp.append(i)
				self.pop2.textBrowser_pop_2.setPlainText("chip "+str(self.tmp[0]))							
				self.pop2.textBrowser_pop.setPlainText("\n clock : "+
					str(self.clock) + "\n time : "+str(self.time*1000)+" ms")
				self.pop2.show()

				if(self.label_3.text() == "PARALLEL"):
					self.pop2_2 = Popup_logic()
					self.pop2_2.setGeometry(858,100,358,400)
					self.pop2_2.nextButton.setText("Quit")
					self.pop2_2.textBrowser_pop_2.setStyleSheet("font-size : 20px;")
					self.pop2_2.textBrowser_pop_2.setPlainText("chip "+str(self.tmp[1]))		
					self.pop2_2.textBrowser_pop.setPlainText("\n clock : "+
					str(self.clock) + "\n time : "+str(self.time*1000)+" ms")
					self.pop2_2.show()


		self.able_all()

	def inst(self, line):
    
		self.decode = line.split(" ")		
		if(self.decode[3] == "INTEST,"):
			return(28 + len(self.decode[4]))
		elif(self.decode[3] == "EXTEST,"):
			return(88 + 4*(len(self.decode[4]) +1) )
		elif(self.decode[2] == "MBIST,"):
			if(self.decode[3] == "MBIST,"):
				return( 8*(3878 + 2*(len(self.decode[4])+1 ) ) )
		return 0


	def checkbox_select(self):	
		self.ischecked_list = [False for i in range(7)]
		self.checkbox_limit=0	
		for i in range(7):
			if(self.checkBoxlist[i].isChecked()):				
				self.checkbox_limit+=1
				self.ischecked_list[i]=True	
		if(self.checkbox_limit==2):
			for i in self.checkBoxlist:
				if(not i.isChecked()):
					i.setDisabled(True)
		if(self.checkbox_limit<2):
			for i in self.checkBoxlist:
				if(not i.isChecked()):
					i.setDisabled(False)

	def closeEvent(self,event):
		readme.close()

	def accept(self):
		pass
		
	# 클릭버튼 및 그 외 색변경
	def but_pressed(self,butnum):
		self.pushButton_2.setStyleSheet("color : none")
		self.pushButton_3.setStyleSheet("color : none")
		self.pushButton_4.setStyleSheet("color : none")
		self.pushButton_5.setDisabled(False)
		
		if(butnum==2):
			self.modebutton = 2
			self.pushButton_2.setStyleSheet("color : #8A0808")
			
		elif(butnum==3):
			self.modebutton = 3
			self.pushButton_3.setStyleSheet("color : #8A0808")
			
		else:
			self.modebutton = 4
			self.pushButton_4.setStyleSheet("color : #8A0808")
			
	
		
	# button 변경 시 clear
	def clear_all(self):
		for i in range(6):
			self.tblist[i].clear()
		
	def disable_all(self):
		for i in range(5):
			self.blist[i].setDisabled(True)
			self.blist[i].repaint()
	def able_all(self):
		for i in range(5):
			self.blist[i].setDisabled(False)
			self.blist[i].repaint()
	
#------------------------------------------------------
# 결과창 popup, Main 상속안돼서 single,parallel 경우의 팝업 따로 만듬
#------------------------------------------------------
class Popup(QMainWindow,Ui_PopupWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.nxtnum = 0
		self.setGeometry(500,100,358,400)		
		
	def nbclicked(self): #this is for popup					
		with open("./log/single/scene_singlemem.txt") as file_object:
				self.scentxt = file_object.readlines()	
		if(self.nxtnum ==0):
			self.setWindowTitle("Memory Info")
			self.textBrowser_pop.clear()			
			for i in range(1,12): #파일을 줄별로 읽어오는거라 형식이 정해져있어야함
				self.textBrowser_pop.append(self.scentxt[i])
			self.nextButton.setText("Repair")
			self.nxtnum+=1
		elif(self.nxtnum ==1):		
			self.an = Analyzing()
			self.textBrowser_pop.clear()			
			self.setWindowTitle("Result")
			for i in range(13,len(self.scentxt)):#파일을 줄별로 읽어오는거라 형식이 정해져있어야함
				self.textBrowser_pop.append(self.scentxt[i])
			self.nxtnum+=1
			self.nextButton.setText("Quit")
		else:
			self.close()		

class Popup2(QMainWindow,Ui_PopupWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.nxtnum = 0
		self.setGeometry(500,100,358,400)
				
	def nbclicked(self): #this is for popup					
		with open("./log/multi/scene_multi_repairable.txt") as file_object:
			self.r_scentxt = file_object.readlines()
		if(self.nxtnum ==0):
			self.setWindowTitle("Memory Info")
			self.textBrowser_pop.clear()			
			for i in range(1,23):
				self.textBrowser_pop.append(self.r_scentxt[i])
			self.nextButton.setText("Repair")
			self.nxtnum+=1
		elif(self.nxtnum ==1):		
			self.an = Analyzing()
			self.textBrowser_pop.clear()			
			self.setWindowTitle("Result")
			for i in range(24,len(self.r_scentxt)):
				self.textBrowser_pop.append(self.r_scentxt[i])
			self.nxtnum+=1
			self.nextButton.setText("Quit")
		else:
			self.close()

class Popup2_2(QMainWindow,Ui_PopupWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.nxtnum = 0
		self.setGeometry(858,100,358,400)
	def nbclicked(self): #this is for popup	
		with open("./log/multi/scene_multi_irrepairable.txt") as file_object:
			self.ir_scentxt = file_object.readlines()	
		if(self.nxtnum ==0):
			self.setWindowTitle("Memory Info")
			self.textBrowser_pop.clear()			
			for i in range(1,23):
				self.textBrowser_pop.append(self.ir_scentxt[i])
			self.nextButton.setText("Repair")
			self.nxtnum+=1
		elif(self.nxtnum ==1):		
			self.an = Analyzing()
			self.textBrowser_pop.clear()			
			self.setWindowTitle("Result")
			for i in range(24,len(self.ir_scentxt)):
				self.textBrowser_pop.append(self.ir_scentxt[i])
			self.nxtnum+=1
			self.nextButton.setText("Quit")
		else:
			self.close()
class Popup_logic(QMainWindow,Ui_PopupWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.nxtnum = 0
		self.setGeometry(500,100,358,400)			
	def nbclicked(self): 		
			self.close()		
#------------------------------------------------------
# Analyzing RA... popup
class Analyzing(QMainWindow,Ui_Analyzing):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()
		self.setGeometry(558,100,360,147)
		for i in range(4):
			self.progressBar_an.setValue(i)
			QApplication.processEvents() 
			self.progressBar_an.repaint()
			time.sleep(1)
		self.close()

if __name__ == "__main__" :
	app = QApplication(sys.argv)
	readme = readme.ReadMe()
	readme.show()

	ex = Main()
	ex.show()
	app.exec_()
