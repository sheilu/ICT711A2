import gi
gi.require_version('Gtk', '3.0')
gi.require_version('GtkSource', '3.0')
from gi.repository import Gtk, GtkSource

class GeditView(Gtk.Window):
    def __init__(self):
        super().__init__(title="Simple Gedit Functionality")
        
        # Create a source view (similar to GtkSourceView in gedit)
        self.source_view = GtkSource.View.new()

        # Set up the buffer (text buffer that handles text storage)
        self.source_buffer = self.source_view.get_buffer()
        
        # Enable syntax highlighting
        self.language_manager = GtkSource.LanguageManager.get_default()
        language = self.language_manager.get_language("python")
        self.source_buffer.set_language(language)

        # Syntax highlight
        self.source_view.set_highlight_syntax(True)

        # Add a scroll window
        scroll_window = Gtk.ScrolledWindow()
        scroll_window.set_vexpand(True)
        scroll_window.add(self.source_view)

        # Pack everything into the window
        self.add(scroll_window)
        
        # Set window size
        self.set_default_size(600, 400)

    # This would represent a simple method that gedit might have, like highlighting syntax
    def highlight_syntax(self, text):
        # Insert some text into the buffer (view)
        self.source_buffer.set_text(text)
        print("Text loaded and syntax highlighted")

# Run the GTK application
if __name__ == "__main__":
    win = GeditView()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
