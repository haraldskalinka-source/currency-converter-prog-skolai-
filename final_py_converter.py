import tkinter as tk
from tkinter import messagebox
import requests

# Valūtas kursu API
def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            raise Exception("API pieprasījums neizdevās.")
        return data["rates"]
    except Exception as e:
        messagebox.showerror("Kļūda", f"Neizdevās iegūt valūtas kursus: {str(e)}")
        return None

# Funkcija valūtas pārveidošanai
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from_currency.get()
        to_currency = combo_to_currency.get()

        # Iegūst valūtas kursus
        rates = get_exchange_rate()
        if rates is None:
            return
        
        # Pārveidošanas aprēķins
        from_rate = rates.get(from_currency, 1)
        to_rate = rates.get(to_currency, 1)
        result = amount * (to_rate / from_rate)
        
        # Parāda rezultātu
        result_label.config(text=f"Rezultāts: {result:.2f} {to_currency}")
    
    except ValueError:
        messagebox.showerror("Stulbs esi?", "Ievadi derīgu skaitli.")
    except Exception as e:
        messagebox.showerror("Stulbs esi?", f"Radās kļūda: {str(e)}")

# GUI uzstādījumi
root = tk.Tk()
root.title("Valūtas kalkulators")
root.geometry("400x300")

# Izvēlnes
currencies = ["EUR", "USD", "CNY", "INR"]
combo_from_currency = tk.StringVar(root)
combo_from_currency.set("EUR")
combo_from_currency_menu = tk.OptionMenu(root, combo_from_currency, *currencies)
combo_from_currency_menu.pack(pady=10)

combo_to_currency = tk.StringVar(root)
combo_to_currency.set("USD")
combo_to_currency_menu = tk.OptionMenu(root, combo_to_currency, *currencies)
combo_to_currency_menu.pack(pady=10)

# Teksta ievades lauks
label_amount = tk.Label(root, text="Ievadiet summu:")
label_amount.pack(pady=5)

entry_amount = tk.Entry(root)
entry_amount.pack(pady=5)

# Poga datu apstrādei
convert_button = tk.Button(root, text="Pārveidot", command=convert_currency)
convert_button.pack(pady=10)

# Rezultāta parādīšana
result_label = tk.Label(root, text="Rezultāts: ")
result_label.pack(pady=10)

# Galvenā cilpa
root.mainloop()