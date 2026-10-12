
import tkinter as tk

root = tk.Tk()
root.title("Vertical Ball Animation")
root.geometry("600x350")
root.resizable(False, False)

# Create the canvas
canvas = tk.Canvas(
    root,
    width=600,
    height=350,
    bg="skyblue"
)
canvas.pack()

# Draw the ground
ground_y = 320

canvas.create_rectangle(
    0, ground_y, 600, 350,
    fill="green",
    outline=""
)

# Create the ball
ball = canvas.create_oval(
    275, 50, 325, 100,
    fill="orange",
    outline="darkorange",
    width=2
)

# Ball movement settings
dy = 0
gravity = 0.5
bounce_strength = -0.8
bounce_count = 0
max_bounces = 6

def animate():
    global dy, bounce_count

    # Get the ball's position
    x1, y1, x2, y2 = canvas.coords(ball)

    # Apply gravity
    dy += gravity

    # Move the ball vertically
    canvas.move(ball, 0, dy)

    # Check if the ball touches the ground
    x1, y1, x2, y2 = canvas.coords(ball)

    if y2 >= ground_y:
        # Keep the ball on the ground
        canvas.move(ball, 0, ground_y - y2)

        # Bounce upward
        if bounce_count < max_bounces and abs(dy) > 2:
            dy *= bounce_strength
            bounce_count += 1
        else:
            dy = 0
            return

    # Continue animation
    root.after(16, animate)

# Start animation
animate()

root.mainloop()
