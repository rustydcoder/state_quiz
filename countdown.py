import math


class Countdown:
    def __init__(self, label, frame, status, close_dialog):
        self.label = label
        self.status = status
        self.frame = frame
        self.timer = ""
        self.close_dialog = close_dialog

    def start_counting(self, count):
        minute = math.floor(count / 60)
        seconds = count % 60
        minute = f"0{minute}" if minute < 10 else minute
        seconds = f"0{seconds}" if seconds < 10 else seconds
        if count >= 0:
            self.label.config(text=f"{minute}:{seconds}")
            self.status.config(text=f"Status: Playing")
            self.timer = self.frame.after(1000, self.start_counting, count - 1)
        else:
            self.stop_counting()

    def stop_counting(self):
        if len(self.timer) > 0:
            self.frame.after_cancel(self.timer)
            self.status.config(text="Status: Game Over")
            self.close_dialog.destroy()
