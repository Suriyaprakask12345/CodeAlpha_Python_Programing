import tkinter as tk
from tkinter import ttk
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StockPortfolioTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Portfolio Tracker")

        # Portfolio Data
        self.portfolio = {}

        # Stock Symbol Entry
        self.symbol_label = ttk.Label(root, text="Stock Symbol:")
        self.symbol_label.grid(row=0, column=0, padx=10, pady=10)
        self.symbol_entry = ttk.Entry(root)
        self.symbol_entry.grid(row=0, column=1, padx=10, pady=10)

        # Add Stock Button
        self.add_button = ttk.Button(root, text="Add Stock", command=self.add_stock)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Portfolio Listbox
        self.portfolio_listbox = tk.Listbox(root, height=10, width=30)
        self.portfolio_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Remove Stock Button
        self.remove_button = ttk.Button(root, text="Remove Stock", command=self.remove_stock)
        self.remove_button.grid(row=2, column=0, padx=10, pady=10)

        # Plot Portfolio Button
        self.plot_button = ttk.Button(root, text="Plot Portfolio", command=self.plot_portfolio)
        self.plot_button.grid(row=2, column=1, padx=10, pady=10)

    def add_stock(self):
        symbol = self.symbol_entry.get().upper()
        if symbol:
            try:
                stock_data = yf.download(symbol, start="2021-01-01", end=pd.to_datetime('today').strftime('%Y-%m-%d'))
                self.portfolio[symbol] = stock_data
                self.portfolio_listbox.insert(tk.END, symbol)
            except Exception as e:
                tk.messagebox.showerror("Error", f"Error adding stock: {e}")

    def remove_stock(self):
        selected_stock = self.portfolio_listbox.get(tk.ACTIVE)
        if selected_stock:
            del self.portfolio[selected_stock]
            self.portfolio_listbox.delete(tk.ACTIVE)

    def plot_portfolio(self):
        if self.portfolio:
            plt.figure(figsize=(10, 5))
            for symbol, data in self.portfolio.items():
                plt.plot(data['Close'], label=symbol)
            plt.title('Portfolio Performance')
            plt.xlabel('Date')
            plt.ylabel('Stock Price (USD)')
            plt.legend()
            plt.tight_layout()

            # Display the plot in the GUI
            canvas = FigureCanvasTkAgg(plt.gcf(), master=self.root)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, columnspan=3, padx=10, pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = StockPortfolioTracker(root)
    root.mainloop()
