import tkinter as tk
from tkinter import filedialog, messagebox
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def convert_svg():
    file_path = filedialog.askopenfilename(
        title="SVGファイルを選択",
        filetypes=[("SVG files", "*.svg")]
    )
    if not file_path:
        return

    try:
        # 入力ファイルと同じ場所に .png で保存
        output_path = os.path.splitext(file_path)[0] + ".png"
        
        drawing = svg2rlg(file_path)
        renderPM.drawToFile(drawing, output_path, fmt="PNG")
        
        messagebox.showinfo("完了", f"変換成功！\n{output_path}")
    except Exception as e:
        messagebox.showerror("エラー", f"失敗しました:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("SVG to PNG")
    root.geometry("300x150")

    tk.Label(root, text="SVGをPNGに一発変換", pady=20).pack()
    tk.Button(root, text="ファイルを選択", command=convert_svg, bg="#0078d4", fg="white", width=20).pack()

    root.mainloop()
