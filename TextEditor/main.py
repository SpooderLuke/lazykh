import tkinter as tk
from tkinter import messagebox

class CustomTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom Text Editor")
        self.root.geometry("600x500")

        custom_font = ("Arial", 14)

        self.text_widget = tk.Text(self.root, wrap="word", bg="#212121", fg="white", font=custom_font)
        self.text_widget.pack(expand=True, fill="both")

        self.templates = ["happy", "angry", "sad", "idle", "annoyed", "smug", "explain", "confused"]

        button_font = ("Arial", 14)

        for template in self.templates:
            add_template_button = tk.Button(self.root, text=template, command=lambda t=template: self.add_template(t),
                                            font=button_font)
            add_template_button.pack(side="left")

        self.text_widget.bind("<Button-1>", self.click_navigation)
        self.text_widget.bind("<Left>", self.navigate_left)
        self.text_widget.bind("<Right>", self.navigate_right)
        self.text_widget.bind("<Key>", self.highlight_bracket_text)

    def add_template(self, text):
        template_text = "<" + text + ">"  # You can customize the template text
        current_position = self.text_widget.index(tk.INSERT)
        self.text_widget.insert(current_position, template_text)
        self.highlight_bracket_text()

    def click_navigation(self):
        index = self.text_widget.index(tk.CURRENT)

    def navigate_left(self):
        current_index = self.text_widget.index(tk.INSERT)
        new_index = self.text_widget.index(f"{current_index} - 1 chars")
        self.text_widget.mark_set(tk.INSERT, new_index)
        return "break"  # To prevent default navigation behavior

    def navigate_right(self):
        current_index = self.text_widget.index(tk.INSERT)
        new_index = self.text_widget.index(f"{current_index} + 1 chars")
        self.text_widget.mark_set(tk.INSERT, new_index)
        return "break"  # To prevent default navigation behavior

    def highlight_bracket_text(self):
        self.tag_bracket_content()

    def tag_bracket_content(self):
        start_index = "1.0"
        end_index = tk.END

        # Remove existing tags
        self.text_widget.tag_remove("bracket_text", start_index, end_index)

        open_bracket = self.text_widget.search("<", start_index, stopindex=end_index)
        close_bracket = self.text_widget.search(">", start_index, stopindex=end_index)

        while open_bracket and close_bracket:
            self.text_widget.tag_configure("bracket_text", foreground="yellow")  # Change the color as needed
            self.text_widget.tag_add("bracket_text", open_bracket + "+1c", close_bracket)
            start_index = close_bracket + "+1c"
            open_bracket = self.text_widget.search("<", start_index, stopindex=end_index)
            close_bracket = self.text_widget.search(">", start_index, stopindex=end_index)

if __name__ == "__main__":
    root = tk.Tk()
    editor = CustomTextEditor(root)
    root.mainloop()
