import tkinter as tk
from tkinter import filedialog, messagebox
import os
import cairosvg

def convert_svg():
    # ファイル選択ダイアログ
    file_path = filedialog.askopenfilename(
        title="SVGファイルを選択",
        filetypes=[("SVG files", "*.svg"), ("All files", "*.*")]
    )
    if not file_path:
        return

    try:
        # 出力パスの作成 (元のファイル名.png)
        base, _ = os.path.splitext(file_path)
        output_path = f"{base}.png"
        
        # 変換実行
        # url: 入力ファイルパス, write_to: 出力ファイルパス
        cairosvg.svg2png(url=file_path, write_to=output_path)
        
        messagebox.showinfo("成功", f"変換が完了しました！\n保存先: {output_path}")
    except Exception as e:
        # エラーの詳細を表示
        messagebox.showerror("エラー", f"変換に失敗しました:\n{str(e)}")

def main():
    root = tk.Tk()
    root.title("SVG to PNG Converter")
    root.geometry("400x200")
    
    label = tk.Label(root, text="SVGを高品質なPNGに変換します", font=("Arial", 11), pady=30)
    label.pack()

    btn = tk.Button(
        root, text="SVGファイルを選択して変換", 
        command=convert_svg, 
        width=30, height=2, 
        bg="#0078d4", fg="white",
        font=("Arial", 10, "bold")
    )
    btn.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
