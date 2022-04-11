#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import gi
import os.path

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import GLib, Gio, Gtk
from MainWindow import MainWindow

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="tr.org.daft-8.debpakir",
                         flags=Gio.ApplicationFlags.HANDLES_OPEN | Gio.ApplicationFlags.NON_UNIQUE, **kwargs)
        self.window = None
        self.emptyfile = None

    def do_activate(self):
        self.window = MainWindow(self, self.emptyfile)

    def do_open(self, files, filecount, hint):
        if filecount == 1:
            file = files[0]
            if os.path.exists(file.get_path()):
                fileFormat = file.get_basename().split(".")[-1]
                if fileFormat == "deb":
                    self.window = MainWindow(self, file)
                else:
                    print("Only .deb files.")
            else:
                print("File not exists : " + file.get_path())
        else:
            print("Only one file.")


if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)
