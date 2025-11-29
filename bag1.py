import tkinter as tk
from tkinter import messagebox

inventory = []
reg_user = ""
reg_pass = ""

cookies = 0.0
cps = 0
upgrade_cost = 20
cookie_clicks = 1.0
click_upgrade = 100

auto_id = None

secret_button = None

global entry


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
    global display_box, secret_button
    display_box.delete(0, tk.END)
    if inventory:
        for item in sorted(set(inventory)):
            display_box.insert(tk.END, f"{inventory.count(item)}x {item}")
    else:
        display_box.insert(tk.END, "Your bag is empty!")

    if any(item.lower() == "cookie" for item in inventory):
        if not secret_button:
            secret_button = tk.Button(
                button_frame, text="Secret", width=10, command=secret)
            secret_button.grid(row=0, column=3, padx=5)
    else:
        if secret_button:
            secret_button.destroy()
            secret_button = None


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


def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()


def back_to_inventory():
    global auto_id
    if auto_id:
        app.after_cancel(auto_id)
        auto_id = None
    clear_screen()
    inventory_gui()


def saved_register():
    global reg_user, reg_pass
    reg_user = saved_reg_name.get()
    reg_pass = saved_reg_pass.get()
    clear_screen()
    inventory_gui()


def secret():
    global user, password
    clear_screen()
    user_name = tk.Label(app, text="Type in the user")
    user_name.pack()

    user = tk.Entry(app, width=20)
    user.pack(pady=5)

    password_text = tk.Label(app, text="Type in the password")
    password_text.pack(pady=5)

    password = tk.Entry(app, width=20)
    password.pack(pady=5)

    login = tk.Button(app, text="Login", command=cookie_clicker)
    login.pack(pady=5)

    back_button = tk.Button(app, text="⬅ Back", command=back_to_inventory)
    back_button.pack(pady=10)


def update_label():
    cookie_label.config(text=f"Cookies: {round(cookies, 2)}")
    cps_label.config(text=f"CPS: {cps}")
    cost_label.config(text=f"Upgrade Cost: {upgrade_cost}")
    click_cost_label.config(text=f"Uppgrade Cost: {click_upgrade}")


def buy_upgrade():
    global cookies, cps, upgrade_cost

    if cookies >= upgrade_cost:
        cookies -= upgrade_cost
        cps += 1
        upgrade_cost = int(upgrade_cost * 1.5)
        update_label()


def buy_click_upgrade():
    global cookies, cookie_clicks, click_upgrade
    if cookies >= click_upgrade:
        cookies -= click_upgrade
        cookie_clicks = round(cookie_clicks * 1.5, 2)
        click_upgrade = int(click_upgrade * 1.5)
        update_label()


def auto_generate():
    global cookies, auto_id
    cookies += cps
    update_label()
    auto_id = app.after(1000, auto_generate)


def cookie_click():
    global cookies
    cookies += cookie_clicks
    update_label()


def cookie_clicker():
    global user, password, cookie_label, cps_label, click_cost_label, cost_label
    if user.get() == reg_user and password.get() == reg_pass:
        clear_screen()
        label = tk.Label(app, text="Cookie Cliker!", font=("Arial", 18))
        label.pack()

        cookie_label = tk.Label(app, text="Cookies: 0", font=("Arial", 14))
        cookie_label.pack(pady=5)

        cps_label = tk.Label(app, text="CPS: 0", font=("Arial", 14))
        cps_label.pack(pady=5)

        cookie = tk.Button(app, text="🍪 Click Me!!", font=(
            "Arial", 10), width=20, height=5, command=cookie_click)
        cookie.pack(pady=10)

        upgrade_frame = tk.Frame(app)
        upgrade_frame.pack(pady=10)

        cost_label = tk.Label(
            upgrade_frame, text="Upgrade Cost: 20", font=("Arial", 12))
        cost_label.grid(row=0, column=0, padx=10, pady=5)

        upgrade_button = tk.Button(
            upgrade_frame, text="Buy (+1 CPS)", font=("Arial", 12), command=buy_upgrade)
        upgrade_button.grid(row=1, column=0, padx=10, pady=5)

        click_cost_label = tk.Label(
            upgrade_frame, text="Upgrade Cost: 100", font=("Arial", 12))
        click_cost_label.grid(row=0, column=1, padx=10, pady=5)

        click_upgrade_button = tk.Button(upgrade_frame, text="Upgrade Click", font=(
            "Arial", 12), command=buy_click_upgrade)
        click_upgrade_button.grid(row=1, column=1, padx=10, pady=5)

        back_button = tk.Button(app, text="⬅ Back", font=(
            "Arial", 12), command=back_to_inventory)
        back_button.pack(pady=10)

        auto_generate()


app = tk.Tk()
app.title("Inventory Bag 🎒")
app.geometry("420x380")
app.resizable(False, False)

reg_name = tk.Label(app, text="Make a username")
reg_name.pack()

saved_reg_name = tk.Entry(app, width=20)
saved_reg_name.pack(pady=5)

reg_password = tk.Label(app, text="Make a Password")
reg_password.pack(pady=5)

saved_reg_pass = tk.Entry(app, width=20)
saved_reg_pass.pack(pady=5)

register = tk.Button(app, text="Register", command=saved_register)
register.pack(pady=5)


def inventory_gui():
    global button_frame
    global entry
    global display_box
    title = tk.Label(app, text="Inventory Manager GUI",
                     font=("Arial", 14, "bold"))
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
