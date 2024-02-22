import tkinter as tk
from views.vacuum_app import VacuumApp

def main():
    root = tk.Tk()
    app = VacuumApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
