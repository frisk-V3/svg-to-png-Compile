import tkinter as tk
from tkinter import filedialog, messagebox
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def convert_svg():
    # ファイル選択ダイアログを表示
    file_path = filedialog.askopenfilename(filetypes=[("SVG files", "*.svg")])
    if not file_path:
        return

    try:
        # 保存先を同じフォルダの .png に設定
        output_path = os.path.splitext(file_path)[0] + ".png"
        
        drawing = svg2rlg(file_path)
        renderPM.drawToFile(drawing, output_path, fmt="PNG")
        
        messagebox.showinfo("成功", f"保存完了:\n{output_path}")
    except Exception as e:
        messagebox.showerror("エラー", f"変換に失敗しました:\n{e}")

# GUIの組み立て
root = tk.Tk()
root.title("SVG to PNG Converter")
root.geometry("300x150")

label = tk.Label(root, text="SVGを選択してPNGに変換します", pady=20)
label.pack()

btn = tk.Button(root, text="SVGファイルを選択", command=convert_svg, bg="#0078d4", fg="white", padx=10)
btn.pack()

root.mainloop()
