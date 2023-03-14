from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
BACKGROUND = "#219F94"

# Window configuration
window = Tk()
window.title("ImageLock")
window.config(padx=350, pady=100, bg=BACKGROUND)


# Watermark Function
def file():
    file_name = filedialog.askopenfilename(title="Select an image file")
    image_text = text_entry.get("1.0", END)
    image_text_num = 0
    if len(image_text) <= 10:
        image_text_num = 8
    else:
        image_text_num = len(image_text) - 4
    try:
        with Image.open(file_name).convert("RGBA") as base:
            txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
            font_size = int(base.size[0] / image_text_num)
            fnt = ImageFont.truetype("arial.ttf", font_size)
            d = ImageDraw.Draw(txt)

            d.text((int(base.size[0] / 2), int(base.size[1] / 2)), f"{image_text}", font=fnt,
                   fill=(255, 255, 255, 220), anchor='ms')
            out = Image.alpha_composite(base, txt)
            out.show()
    except AttributeError:
        messagebox.showinfo(title="No image was selected")
    else:
        to_save = messagebox.askyesno(title="Do you want to save the image")
        if to_save:
            out.save("./out.png")


# Canvas for decorative texts
canvas = Canvas(width=700, height=200, bg='white', highlightthickness=0)
canvas.create_text(400, 80, text="Image Watermarker by ImageLock", font=("Arial", 20, "bold"),
                   justify="center", fill="black")
canvas.create_text(400, 120, text="Copyright your image with any text of your choice", font=("Times New Roman", 16, "italic"),
                   justify="center", fill="black")
canvas.grid(column=0, row=0, columnspan=2, rowspan=2)


# labels and text entry
label = Label(text="Enter the word you'll like on your image: ", bg=BACKGROUND, fg="white")
label.grid(column=0, row=2)
label.config(font=("Arial", 16, "bold"), padx=20, pady=20)
text_entry = Text(width=20, height=2)
text_entry.config(highlightthickness=1, highlightcolor="black")
text_entry.grid(column=1, row=2)
# color_type = Label(text="Do you want the watermark colored or in black and white")
# color_type.grid(column=0, row=3)


#  Select button
button = Button(text="Select Image", font=("Arial", 10, "italic"), bg="white", fg="black", command=file)
button.config(padx=10, pady=10)
button.grid(column=0, columnspan=2, row=3)

window.mainloop()