När det kommer till layouten så har jag använt både grid och pack samt använt frame.

PS när du har skrivit in user och password och registrerat skriv in cookie i inventoryt och adda det .

Programet sparas med hjälp av en lista alltså inventory = []. 
Listan håller reda på i vilken ordning saker lades till vilket kan vara ganska användbart.
Du kan ha flera “cookie” i listan, tex ["cookie", "cookie", "sword"].
Du kan lägga till (append() eller extend()), ta bort (remove()), räkna (count()), sortera (sort()), söka (in) osv.

När användaren skriver in saker i entry-fältet → vi läser texten → använder parse_item_input() → lägger till i listan:
inventory.extend([name] * qty)

När vi tar bort något:
inventory.remove(name)

Kontroller = grafiska komponenter som användaren kan interagera med. Exempel: tex Button, Entry, Label, Listbox.

Exempel: lägga till en knapp

def say_hello():
    print("Hello!")

button = tk.Button(app, text="Click me", command=say_hello)
button.pack()

tk.Button → skapar knappen.
text="Click me" → texten som syns på knappen.
command=say_hello → funktionen som körs när användaren klickar på knappen.
pack() → placerar knappen i fönstret.

vad behövs för att knappen ska synsa / fungera?

Ett Tkinter-fönster (app = tk.Tk()).
En funktion eller metod som knappen ska anropa.
Knappen måste placeras med pack(), grid() eller place().

Detta är några andra kontroller i tkinter:

Entry → textfält där användaren skriver saker. .get() används för att läsa innehållet.
Label → visar text, t.ex. antal cookies.
Listbox → visar inventorylistan.
Button → för att lägga till, ta bort, söka och secret-knappen.

Skillnader mellan Tkinter och terminalversion: 

Skillnaden:
Terminalprogram körs linjärt: programmet frågar användaren, får input, gör något, sedan nästa steg.

Tkinter är event-driven: programmet väntar på händelser (t.ex. knapptryck) och svarar när de sker. Detta gör det möjligt att ha flera knappar, timers och uppdateringar utan att blockera programmet.

Jämförelse av strukturen:

Terminalversion:

Kör en loop:

while True:
    command = input("Enter command: ")

add, remove, search etc.

Programmet “drivs” av loop + input().
Användaren styr flödet med textkommandon.

Tkinter-version:
Programmet “drivs” av mainloop():

app = tk.Tk()
app.mainloop()

Alla funktioner kopplas till händelser (knappar, entrys).
Ingen explicit loop behövs, Tkinter hanterar loop och väntan på input.

Sammanfattning:

Inventory sparas i en lista → flexibel, kan innehålla flera objekt, lätt att manipulera.
Kontroller i Tkinter → widgets som knappar, textfält och labels. Kräver fönster och eventkoppling (command).
Terminal vs Tkinter → terminalen är linjär och textbaserad, Tkinter är grafisk och event-driven.
Programstrukturen → terminalversion drivs av while-loop och input(), Tkinter drivs av mainloop() och event-hantering.


Detta tog lite tid men som du ser i koden har jag lagt till saker som är mer än bara ett inventory så snälla skriv in cookie i inventoryt så du får se den fina hemliga knappen, men du måste komma ihåg ditt user och passeord för den hemliga saken.

Samt så använder jag messagebox import i denna tkinter appen.