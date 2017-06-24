from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Button Clicker 2.0")

        #Button
        self.button = Gtk.Button(label="Click Here")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)

    #user clicks button
    def button_clicked(self, widget):
        print("Game Time")




window = MainWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()