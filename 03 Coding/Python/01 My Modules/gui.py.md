---
id: guipy
aliases: []
tags:
  - coding
  - python
  - my_modules
Date: 15-06-2025
dg-publish: true
---
# gui.py

```python
def create_servo_slider(frame, servo_id, initial_value,slider_label):
    def on_move(val):
        set_servo(servo_id, int(float(val)))
    slider = tk.Scale(
        frame,
        from_=0,
        to=180,
        orient=tk.HORIZONTAL,
        label=f"Servo: {slider_label} ",
        command=on_move,
    )
    slider.set(initial_value) 
    return slider

```

- It creates a slider 
- **requires**: `frame` , `servo_id`, `initial_value`, `slider_label` 
- `initial_value` is scraped from [here](https://github.com/AI-Robot-GCEK/robo-initial-positions/blob/main/src/initial-positions.h) 

```python

def gui_main(SERVO_COUNT, initial_angles,servo_values,servo_names):
    global ip_entry  
    root = tk.Tk()
    root.title("AI-Robot-PFv0.1")
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # IP entry
    ip_label = tk.Label(frame, text="Server IP:")
    ip_label.grid(row=0, column=0, padx=5)
    ip_entry = tk.Entry(frame)
    ip_entry.grid(row=0, column=1, padx=5)
    ip_button = tk.Button(frame, text="Set IP", command=lambda: update_ip(ip_entry.get()))
    ip_button.grid(row=0, column=2, padx=5)

    # Name entry and save button
    name_label = tk.Label(frame, text="Name:")
    name_label.grid(row=1, column=0, padx=5)
    name_entry = tk.Entry(frame)
    name_entry.grid(row=1, column=1, padx=5)
    save_button = tk.Button(
        frame, 
        text="Save values", 
        command=lambda: save_to_json(name_entry.get(),servo_values)  
    )
    save_button.grid(row=1, column=2, padx=5)

    sliders_frame = tk.Frame(root)
    sliders_frame.pack(padx=10, pady=10)

    # Arrange sliders in a 4x4 grid
    sliders = []
    for id in range(SERVO_COUNT):
        slider = create_servo_slider(sliders_frame, id, initial_angles[id],servo_names[id])
        sliders.append(slider)
        row, col = divmod(id, 4)  # Calculate row and column for 4x4 grid
        slider.grid(row=row, column=col, padx=5, pady=5)  # Use grid for layout
    root.mainloop()

```