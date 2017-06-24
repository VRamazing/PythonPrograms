from gi.repository import Gtk

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ListBoxes")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)

        #checkbox
        row1 = Gtk.ListBoxRow()
        box1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row1.add(box1)
        label = Gtk.Label("Check if you love cheeseburgers")
        check = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check, True, True, 0)
        listbox.add(row1)

        # Toggle Button
        row2 = Gtk.ListBoxRow()
        box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=100)
        row2.add(box2)
        label2 = Gtk.Label("Oregano")
        switch = Gtk.Switch()
        box2.pack_start(label2, True, True, 0)
        box2.pack_start(switch, True, True, 0)
        listbox.add(row2)


window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()