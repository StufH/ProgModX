import tkinter as tk
import random

class PongGame:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(master, width=600, height=400, bg="black")
        self.canvas.pack()

        self.ball = self.canvas.create_oval(195, 195, 205, 205, fill="white")

        # Smaller paddles (60 units tall, 20 units wide)
        self.paddle_left = self.canvas.create_rectangle(80, 170, 100, 230, fill="white")  # Left paddle
        self.paddle_right = self.canvas.create_rectangle(480, 170, 500, 230, fill="white")  # Right paddle

        # Increased ball speed
        self.ball_x = random.choice([-6, -5, -4, 4, 5, 6])
        self.ball_y = random.choice([-6, -5, -4, 4, 5, 6])
        self.paddle_left_y = 170
        self.paddle_right_y = 170

        self.score_left = 0
        self.score_right = 0
        self.score_text = self.canvas.create_text(300, 20, font=("Helvetica", 20), fill="white")

        self.paused = False
        self.pressed_keys = set()
        self.bind_keys()
        self.move_ball()
        self.move_paddles()  # Start paddle movement

    def bind_keys(self):
        self.master.bind("<Escape>", lambda event: self.toggle_pause())
        self.canvas.focus_set()

        # Track key presses and releases
        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.bind("<KeyRelease>", self.on_key_release)

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            self.master.title("Pong (Paused)")
        else:
            self.master.title("Pong")
            self.move_ball()

    def on_key_press(self, event):
        """ Track keys that are pressed. """
        self.pressed_keys.add(event.keysym)

    def on_key_release(self, event):
        """ Remove keys that are released. """
        self.pressed_keys.discard(event.keysym)

    def move_paddles(self):
        """ Continuously check for key presses and move paddles accordingly. """
        if not self.paused:
            # Move right paddle
            if "Up" in self.pressed_keys and self.paddle_right_y > 0:  # Right paddle moves up
                self.canvas.move(self.paddle_right, 0, -10)
                self.paddle_right_y -= 10
            if "Down" in self.pressed_keys and self.paddle_right_y < 340:  # Right paddle moves down
                self.canvas.move(self.paddle_right, 0, 10)
                self.paddle_right_y += 10
            if "Left" in self.pressed_keys and self.paddle_right_y > 0:  # Right paddle moves left
                if self.canvas.coords(self.paddle_right)[0] > 0:  # Prevent moving out of bounds
                    self.canvas.move(self.paddle_right, -10, 0)
            if "Right" in self.pressed_keys and self.paddle_right_y < 340:  # Right paddle moves right
                if self.canvas.coords(self.paddle_right)[2] < 600:  # Prevent moving out of bounds
                    self.canvas.move(self.paddle_right, 10, 0)

            # Move left paddle
            if "w" in self.pressed_keys and self.paddle_left_y > 0:  # Left paddle moves up
                self.canvas.move(self.paddle_left, 0, -10)
                self.paddle_left_y -= 10
            if "s" in self.pressed_keys and self.paddle_left_y < 340:  # Left paddle moves down
                self.canvas.move(self.paddle_left, 0, 10)
                self.paddle_left_y += 10
            if "a" in self.pressed_keys and self.paddle_left_y > 0:  # Left paddle moves left
                if self.canvas.coords(self.paddle_left)[0] > 0:  # Prevent moving out of bounds
                    self.canvas.move(self.paddle_left, -10, 0)
            if "d" in self.pressed_keys and self.paddle_left_y < 340:  # Left paddle moves right
                if self.canvas.coords(self.paddle_left)[2] < 600:  # Prevent moving out of bounds
                    self.canvas.move(self.paddle_left, 10, 0)

        # Continuously check the key states
        self.master.after(20, self.move_paddles)  # Update every 20ms

    def move_ball(self):
        if self.paused:
            return

        self.canvas.move(self.ball, self.ball_x, self.ball_y)
        pos = self.canvas.coords(self.ball)

        # Check for collision with the left paddle
        paddle_left_coords = self.canvas.coords(self.paddle_left)
        if (pos[2] >= paddle_left_coords[0] and pos[0] <= paddle_left_coords[2] and
            pos[3] >= paddle_left_coords[1] and pos[1] <= paddle_left_coords[3]):
            # Ball has hit the left paddle
            self.ball_x = abs(self.ball_x)  # Reflect the ball
            overlap_y = (pos[3] + pos[1]) / 2 - (paddle_left_coords[3] + paddle_left_coords[1]) / 2
            self.ball_y += overlap_y * 0.05  # Adjust Y velocity based on where the ball hits
            self.canvas.coords(self.ball, paddle_left_coords[2], pos[1], paddle_left_coords[2] + 10, pos[3])  # Reposition ball

        # Check for collision with the right paddle
        paddle_right_coords = self.canvas.coords(self.paddle_right)
        if (pos[0] <= paddle_right_coords[2] and pos[2] >= paddle_right_coords[0] and
            pos[3] >= paddle_right_coords[1] and pos[1] <= paddle_right_coords[3]):
            # Ball has hit the right paddle
            self.ball_x = -abs(self.ball_x)  # Reflect the ball
            overlap_y = (pos[3] + pos[1]) / 2 - (paddle_right_coords[3] + paddle_right_coords[1]) / 2
            self.ball_y += overlap_y * 0.05  # Adjust Y velocity based on where the ball hits
            self.canvas.coords(self.ball, paddle_right_coords[0] - 10, pos[1], paddle_right_coords[0], pos[3])  # Reposition ball

        # Check for scoring
        if pos[0] <= 0:
            self.score_right += 1
            self.canvas.itemconfig(self.score_text, text=f"{self.score_left} : {self.score_right}")
            self.ball_x = random.choice([-6, -5, -4, 4, 5, 6])
            self.ball_y = random.choice([-6, -5, -4, 4, 5, 6])
            self.canvas.coords(self.ball, 300, 200, 310, 210)
        elif pos[2] >= 600:
            self.score_left += 1
            self.canvas.itemconfig(self.score_text, text=f"{self.score_left} : {self.score_right}")
            self.ball_x = random.choice([-6, -5, -4, 4, 5, 6])
            self.ball_y = random.choice([-6, -5, -4, 4, 5, 6])
            self.canvas.coords(self.ball, 300, 200, 310, 210)

        # Check for wall collisions
        if pos[1] <= 0 or pos[3] >= 400:
            self.ball_y = -self.ball_y

        # Reduced delay for faster movement
        self.master.after(30, self.move_ball)

if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()
