import tkinter as tk

def ascii_to_dec():
    text = entry.get()
    result = chr((sum(ord(char) for char in text) % 64) + 64) + "\\r"
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, text + result)

root = tk.Tk()

label_prompt = tk.Label(root, text="Entrez le texte :")
label_prompt.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Calculer", command=ascii_to_dec)
button.pack()

text_result = tk.Text(root, height=2, width=30)
text_result.pack()

root.mainloop()
