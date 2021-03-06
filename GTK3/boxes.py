from gi.repository import Gtk

class MainWindow(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self,title="")
    #Box
    self.box = Gtk.Box(spacing = 10)
    self.add(self.box)

    #Bacon Button
    self.bacon_button = Gtk.Button(label = "Bacon")
    self.bacon_button.connect("clicked",self.bacon_clicked)
    self.box.pack_start(self.bacon_button,True,True,0)

    #Tuna Button
    self.tuna_button = Gtk.Button(label = "Tuna")
    self.tuna_button.connect("clicked",self.tuna_clicked)
    self.box.pack_start(self.tuna_button,True,True,0)

  def tuna_clicked(self,widget):
    print('Tuna is clicked')

  def bacon_clicked(self,widget):
    print('You Clicked Bacon!')

window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()
