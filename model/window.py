from tkinter import ttk, messagebox
from tkinter import *

from function.main import *

from model.color import Colors
from model.fonts import Fonts

from assets.icon import icon as mylan_icon

from PIL import ImageTk, Image
import clipboard


PADX = 10
PADY = 4

class Window(Tk):
	def __init__(self):
		super().__init__()
		self.title("RFID - Value converter")
		
		photo = PhotoImage( data=mylan_icon )
		self.wm_iconphoto(False, photo)


		self.colors = Colors()
		self.fonts  = Fonts() 

		self.ascii_1 = StringVar()
		self.ascii_1_cat = StringVar()
		self.ascii_1.trace('w', self.ascii_1_on_change)	

		self.ascii_2 = StringVar()
		self.hexa_1  = StringVar()
		self.hexa_2 = StringVar()
		self.hexa_2.trace('w', self.hexa_2_on_change)	



		self.tabbed_view = ttk.Notebook(self)

		self.stylingTableMenu()

		self.tab_1 = Frame( self.tabbed_view )
		self.tab_2 = Frame( self.tabbed_view )

		self.tabbed_view.add( self.tab_1, text="Ascii to Hex" )
		self.tabbed_view.add( self.tab_2, text="Hex to Ascii" )

		self.init_tab_1()
		self.init_tab_2()

		self.tabbed_view.pack( expand = 1, fill=BOTH )		


	def stylingTableMenu(self):
		style = ttk.Style()

		style.theme_create( 
			"tabbed_view", parent="alt", 
			settings={
		        "TNotebook": {
		        	"configure": {
		        		"tabmargins": [2, 5, 2, 0],		        		  
		        		},		        	
		        	},
		        "TNotebook.Tab": {
		            "configure": {
		            	"padding": [15, 1], 
		            	"font": self.fonts.normal,
		            	"background": self.colors.gray,
		            	"borderwidth": 0,		
		            	"focuscolor": self.colors.white,            		            		            		            	
		            	},
		            "map":{
		            	"background": [ ("selected", "#ffffff")],			            	  	
		                } 
		            },
		         "Treeview": {
		         		"configure": {
		         			"background": self.colors.white,
		         			"fieldbackground": self.colors.white,
							"font": self.fonts.small													
		         		}
		         	},
		         "Treeview.Heading": {
		         		"configure":{
		         			"background": self.colors.cyan,
		         			"foreground": self.colors.white,
							"font": self.fonts.small_bold
		         		}
		         	} 
		        } 
		    )
		style.configure("Tab", focuscolor=style.configure(".")["background"])
		style.theme_use("tabbed_view")


	def init_tab_1(self):
		self.label_1 = Label( self.tab_1, text="Unikey có thể sẽ làm phần mềm bị lỗi, vui lòng tắt nó đi trước khi dùng nhé" )
		self.label_1.pack( side=TOP, fill=BOTH, padx=PADX, pady=PADY )
		self.tab_1_ui_init()

	def ascii_1_on_change(self, *args):
		ascii_string = self.ascii_1.get()
		ascii_list = char_to_bin(ascii_string)
		dec_list = [ binaryToDecimal(x) for x in ascii_list ]
		hex_list = [ decToHexa(x) for x in dec_list ]

		self.delete_detail_tree_view_1_children()
		for i in range( len(ascii_list) ):				
			self.detail_tree_view_1.insert(
					parent="", 
					index=i, 
					iid=i, 
					values=( ascii_string[i], ascii_list[i], hex_list[i])
				)

		self.hexa_1.set( ' '.join(hex_list) )
		self.detail_tree_view_1.yview_moveto(1)


	def clipboardHex(self):
		clipboard.copy(self.hexa_1.get())

	def clipboardAscii(self):
		clipboard.copy(self.ascii_2.get())


	def delete_detail_tree_view_1_children(self):
		for item in self.detail_tree_view_1.get_children():
			self.detail_tree_view_1.delete(item)

	def ascii_key_down(self, event):
		return
		

	def tab_1_ui_init(self):
		frame_0_1 = Frame( self.tab_1 )
		Label( frame_0_1, text="ASCII", font=self.fonts.normal).pack( side=LEFT, padx=PADX, pady=PADY )
		frame_0_1.pack( side=TOP, fill=X )

		self.tab_1_ascii_entry = Entry( 
				self.tab_1, 
				textvariable = self.ascii_1, 
				validate = "key",
				font=self.fonts.normal,
			)
		# self.tab_1_ascii_entry.bind("<Key>", self.ascii_key_down)
		self.tab_1_ascii_entry.pack(side=TOP, fill=BOTH, padx=PADX, pady=PADY )

		frame_0_2 = Frame( self.tab_1 )
		Label( frame_0_2, text="HEXA", font=self.fonts.normal).pack( side=LEFT, padx=PADX, pady=PADY )
		frame_0_2.pack( side=TOP, fill=X )

		frame_0_3 = Frame( self.tab_1 )
		self.tab_1_hex_entry = Entry( 
				frame_0_3, 
				textvariable = self.hexa_1, 
				validate = "key",
				font=self.fonts.normal,
				state=DISABLED
			)		
		self.tab_1_hex_entry.pack(side=LEFT, fill=BOTH, expand=True, padx=PADX, pady=PADY )
		Button( frame_0_3, text="Copy", command=self.clipboardHex,
			borderwidth = 0,
			background = self.colors.white,
			font = self.fonts.x_small,
			activebackground = self.colors.white
		).pack( side=LEFT, padx=PADX, pady=PADY, ipadx=15, ipady=4 )
		frame_0_3.pack( side=TOP, fill=X )


		tree_frame = Frame( self.tab_1 )

		self.detail_tree_view_1 = ttk.Treeview( tree_frame, column=(0, 1, 2), height = 10, show="headings",)
		self.detail_tree_view_1.heading(0, text="Ascii", anchor="w")
		self.detail_tree_view_1.column(0, anchor="w")
		self.detail_tree_view_1.heading(1, text="Binary", anchor="w")
		self.detail_tree_view_1.column(1, anchor="w")
		self.detail_tree_view_1.heading(2, text="Hexa", anchor="w")
		self.detail_tree_view_1.column(2, anchor="w")

		verscrlbar = ttk.Scrollbar(tree_frame,
                           orient ="vertical",
                           command = self.detail_tree_view_1.yview)
		verscrlbar.pack( side=RIGHT, fill=Y )
		self.detail_tree_view_1.configure(yscrollcommand=verscrlbar.set)
		self.detail_tree_view_1.pack( side=TOP, fill=BOTH )
		tree_frame.pack( side=TOP, fill=BOTH, padx=PADX, pady=PADY )

	def init_tab_2(self):

		self.label_2 = Label( self.tab_2, text="Những ký tự bên ngoài [1-9][A-Z] và <space/> đều được tính là không hợp lệ" )
		self.label_2.pack( side=TOP, fill=BOTH, padx=PADX, pady=PADY )

		self.tab_2_ui_init()

	def tab_2_ui_init(self):
		frame_0_1 = Frame( self.tab_2 )
		Label( frame_0_1, text="HEXA", font=self.fonts.normal).pack( side=LEFT, padx=PADX, pady=PADY )
		frame_0_1.pack( side=TOP, fill=X )

		self.tab_2_ascii_entry = Entry( 
				self.tab_2, 
				textvariable = self.hexa_2, 
				validate = "key",
				font=self.fonts.normal,
			)
		# self.tab_2_ascii_entry.bind("<Key>", self.ascii_key_down)
		self.tab_2_ascii_entry.pack(side=TOP, fill=BOTH, padx=PADX, pady=PADY )

		frame_0_2 = Frame( self.tab_2 )
		Label( frame_0_2, text="ASCII", font=self.fonts.normal).pack( side=LEFT, padx=PADX, pady=PADY )
		frame_0_2.pack( side=TOP, fill=X )

		frame_0_3 = Frame( self.tab_2 )
		self.tab_2_hex_entry = Entry( 
				frame_0_3, 
				textvariable = self.ascii_2, 
				validate = "key",
				font=self.fonts.normal,
				state=DISABLED
			)		
		self.tab_2_hex_entry.pack(side=LEFT, fill=BOTH, expand=True, padx=PADX, pady=PADY )
		Button( frame_0_3, text="Copy", command=self.clipboardAscii,
			borderwidth = 0,
			background = self.colors.white,
			font = self.fonts.x_small,
			activebackground = self.colors.white
		).pack( side=LEFT, padx=PADX, pady=PADY, ipadx=15, ipady=4 )
		frame_0_3.pack( side=TOP, fill=X )


		tree_frame = Frame( self.tab_2 )

		self.detail_tree_view_2 = ttk.Treeview( tree_frame, column=(0, 1, 2), height = 10, show="headings",)
		self.detail_tree_view_2.heading(0, text="Hexa", anchor="w")
		self.detail_tree_view_2.column(0, anchor="w")
		self.detail_tree_view_2.heading(1, text="Ascii", anchor="w")
		self.detail_tree_view_2.column(1, anchor="w")
		self.detail_tree_view_2.heading(2, text="Binary", anchor="w")
		self.detail_tree_view_2.column(2, anchor="w")
		

		verscrlbar = ttk.Scrollbar(tree_frame,
                           orient ="vertical",
                           command = self.detail_tree_view_2.yview)
		verscrlbar.pack( side=RIGHT, fill=Y )
		self.detail_tree_view_2.configure(yscrollcommand=verscrlbar.set)
		self.detail_tree_view_2.pack( side=TOP, fill=BOTH )
		tree_frame.pack( side=TOP, fill=BOTH, padx=PADX, pady=PADY )


	def hex_validate(self, string):
		hex_chars = [ x for x in "0123456789ABCDEF " ]
		valid = True
		for i in string:
			if not i in hex_chars:
				valid = False
		return valid

	def delete_detail_tree_view_2_children(self):
		for item in self.detail_tree_view_2.get_children():
			self.detail_tree_view_2.delete(item)


	def hexa_2_on_change(self, *args):
		hexa_string = self.hexa_2.get()
		valid = self.hex_validate( hexa_string )
		if valid:
			trim_str = hexa_string.replace(" ", "")
			hex_pair = []
			if len(trim_str ) % 2 == 0:
				for i in range(0, len(trim_str ), 2 ):
					hex_pair.append( trim_str[i]+trim_str[i+1] )
			else:
				for i in range( len(trim_str) - 1, 0, -2 ):
					hex_pair.insert(0, trim_str[i-1]+trim_str[i] )
				hex_pair.insert(0, "0"+trim_str[0])
			
			self.delete_detail_tree_view_2_children()

			int_list = [ int( x, 16 ) for x in hex_pair ]
			char_list = [ chr( x ) for x in int_list ]
			joined_char_list = "".join( char_list )
			bin_list = char_to_bin( joined_char_list )

			for i in range( len( int_list ) ):
				self.detail_tree_view_2.insert( parent ="", index = i, iid=i, 
					values = ( hex_pair[i], char_list[i], bin_list[i] )
				)

			self.ascii_2.set( ''.join(char_list) )
			self.detail_tree_view_2.yview_moveto(1)


		else:
			messagebox.showerror(title = "Lỗi!", message="Một vài ký tự có vẻ không hợp lệ trong bảng mã thập lục phân, hãy kiểm tra lại!")

__all__ = [ 'Window' ]
