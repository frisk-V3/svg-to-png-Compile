import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

def convert_svg():
    file_path = filedialog.askopenfilename(
        title="SVGファイルを選択",
        filetypes=[("SVG files", "*.svg"), ("All files", "*.*")]
    )
    if not file_path:
        return

    try:
        # 出力パスの生成（OSに依存しないパス操作）
        base_path = os.path.splitext(file_path)[0]
        output_path = f"{base_path}.png"
        
        # 変換処理
        drawing = svg2rlg(file_path)
        renderPM.drawToFile(drawing, output_path, fmt="PNG")
        
        messagebox.showinfo("成功", f"PNGに変換しました！\n保存先: {output_path}")
    except Exception as e:
        messagebox.showerror("エラー", f"変換に失敗しました:\n{str(e)}")

def main():
    root = tk.Tk()
    root.title("SVG to PNG Converter")
    root.geometry("400x200")
    
    # 画面中央に配置
    label = tk.Label(root, text="SVGをPNGに変換するツール", font=("Arial", 12), pady=30)
    label.pack()

    btn = tk.Button(
        root, text="ファイルを選択して変換", 
        command=convert_svg, 
        width=25, height=2, 
        bg="#2196F3", fg="white"
    )
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
