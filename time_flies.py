from datetime import datetime
import tkinter as tk


class MementoClock:

  def __init__(self, root):
    self.root = root
    self.root.title("Counting Down")
    self.root.geometry("420x260")
    self.root.config(bg="#1a1a1a")

    # 讓視窗保持在最上層，隨時看得到
    self.root.attributes("-topmost", True)

    # 標題提醒語
    self.title_label = tk.Label(
        root,
        text="时间正在一秒一秒流逝...",
        font=("Microsoft JhengHei", 13, "bold"),
        fg="#ff6b6b",
        bg="#1a1a1a",
    )
    self.title_label.pack(pady=(20, 5))

    # 大時鐘顯示
    self.time_label = tk.Label(
        root,
        text="",
        font=("Consolas", 38, "bold"),
        fg="#4ecdc4",
        bg="#1a1a1a",
    )
    self.time_label.pack(pady=5)

    # 今日進度百分比文字
    self.progress_label = tk.Label(
        root,
        text="",
        font=("Microsoft JhengHei", 10),
        fg="#aaaaaa",
        bg="#1a1a1a",
    )
    self.progress_label.pack(pady=(5, 5))

    # 進度條畫布
    self.canvas = tk.Canvas(
        root, width=360, height=14, bg="#2d2d2d", highlightthickness=0
    )
    self.canvas.pack(pady=5)

    # 畫出進度條實體
    self.bar = self.canvas.create_rectangle(0, 0, 0, 14, fill="#ff6b6b")

    # 啟動時鐘更新迴圈
    self.update_clock()

  def update_clock(self):
    now = datetime.now()

    # 更新時間字串
    time_str = now.strftime("%H:%M:%S")
    self.time_label.config(text=time_str)

    # 計算今天已經過了多少百分比
    seconds_since_midnight = (
        now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1e6
    )
    total_seconds = 86400  # 一天的總秒數
    percent = (seconds_since_midnight / total_seconds) * 100

    # 更新進度條長度 (總寬度 360)
    bar_width = (seconds_since_midnight / total_seconds) * 360
    self.canvas.coords(self.bar, 0, 0, bar_width, 14)

    # 更新提示文字
    self.progress_label.config(
        text=f"今日进度：已流逝 {percent:.2f}%，请好好把握当下！"
    )

    # 每 100 毫秒更新一次，保持數字流動感
    self.root.after(100, self.update_clock)


if __name__ == "__main__":
  root = tk.Tk()
  app = MementoClock(root)
  root.mainloop()