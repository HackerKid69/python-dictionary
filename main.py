import tkinter as tk
from tkinter import messagebox

def get_definition_and_synonyms():
    word = entry.get()
    definition = "Definition for " + word  # Replace this with your actual definition retrieval logic
    synonyms = ["Synonym1", "Synonym2", "Synonym3"]  # Replace this with your actual synonym retrieval logic

    # Display definition
    definition_label.config(text=definition)

    # Display synonyms
    synonyms_label.config(text="Synonyms: " + ", ".join(synonyms))

# Create main window
root = tk.Tk()
root.title("Dictionary and Synonyms")

# Create entry box
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Bind Enter key to get_definition_and_synonyms function
entry.bind("<Return>", lambda event: get_definition_and_synonyms())

# Create labels to display definition and synonyms
definition_label = tk.Label(root, text="", wraplength=300)
definition_label.pack()

synonyms_label = tk.Label(root, text="")
synonyms_label.pack()

# Run the application
root.mainloop()
