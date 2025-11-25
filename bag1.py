import tkinter as tk
from tkinter import messagebox

inventory = []


def parse_item_input(raw_text):
    raw_text = raw_text.strip().lower()
    parts = raw_text.split()

    if parts and parts[0].isdigit():
        qty = int(parts[0])
        name = " ".join(parts[1:]).replace("x", "").strip()
        return qty, name

    if parts and parts[0].endswith("x") and parts[0][:-1].isdigit():
        qty = int(parts[0][:-1])
        name = " ".join(parts[1:]).strip()
        return qty, name

    return 1, raw_text


def add_item_from_text(raw_text):
    qty, name = parse_item_input(raw_text)
    if qty > 0 and name:
        inventory.extend([name] * qty)
    inventory.sort()
    update_display()


def update_display():
    display_box.delete(0, tk.END)
    if inventory:
        for item in sorted(set(inventory)):
            display_box.insert(tk.END, f"{inventory.count(item)}x {item}")
    else:
        display_box.insert(tk.END, "Your bag is empty!")


def add_items():
    raw = entry.get()
    if raw.strip():
        items = [i.strip() for i in raw.split(",") if i.strip()]
        for i in items:
            add_item_from_text(i)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter an item first!")


def remove_items():
    raw = entry.get().strip().lower()
    if not raw:
        return messagebox.showwarning("Warning", "Enter an item to remove!")

    qty, name = parse_item_input(raw)
    removed = 0

    for _ in range(qty):
        try:
            inventory.remove(name)
            removed += 1
        except ValueError:
            break

    inventory.sort()
    entry.delete(0, tk.END)

    if removed > 0:
        messagebox.showinfo("Removed", f"Removed {removed}x {name}")
    else:
        messagebox.showerror("Not Found", f"{name} not found!")

    update_display()


def search_items():
    raw = entry.get().strip().lower()
    if not raw:
        return messagebox.showwarning("Warning", "Enter something to search!")

    results = []
    for item in [i.strip() for i in raw.split(",") if i.strip()]:
        count = inventory.count(item)
        if count > 0:
            results.append(f"{count}x {item}")
        else:
            results.append(f"{item} not found")

    messagebox.showinfo("Search Results", "\n".join(results))
    entry.delete(0, tk.END)


app = tk.Tk()
app.title("Inventory Bag 🎒")
app.geometry("420x380")
app.resizable(False, False)

title = tk.Label(app, text="Inventory Manager GUI", font=("Arial", 14, "bold"))
title.pack(pady=10)

entry = tk.Entry(app, width=40)
entry.pack(pady=5)

button_frame = tk.Frame(app)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add", width=10,
          command=add_items).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Remove", width=10,
          command=remove_items).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Search", width=10,
          command=search_items).grid(row=0, column=2, padx=5)

display_box = tk.Listbox(app, width=40, height=12)
display_box.pack(pady=15)

update_display()

app.mainloop()
