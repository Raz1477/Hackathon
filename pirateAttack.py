import tkinter as tk 
import pirateProbability
from PIL import Image, ImageTk

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt

# Basic window setup 
window = tk.Tk()
window.title("Pirate Probability")
window.geometry("600x600")
window.wm_resizable(False, False)
window.configure(bg = "beige")

# Global Font Preferences
font_tuple = ("Javanese Text", 20, "bold")

# Stats Label Declaration
labelStats = tk.Label()

# Plots coordinate on a map with labeled point
def plotMap(longitude, latitude, prob):
    plt.figure(figsize =(16, 8))
    ax = plt.axes(projection = ccrs.PlateCarree())
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.OCEAN, facecolor='#CCFEFF')
    ax.add_feature(cfeature.LAKES, facecolor='#CCFEFF')
    ax.add_feature(cfeature.RIVERS, edgecolor='#CCFEFF')
    ax.add_feature(cfeature.LAND, facecolor='#FFE9B5')
    gl = ax.gridlines(
        crs=ccrs.PlateCarree(), 
        draw_labels=True, 
        linewidth=1, 
        color='gray', 
        alpha=0.5, 
        linestyle='--'
    )
    gl.top_labels = False
    gl.left_labels = False
    ax.set_extent([-180, 180, -90, 90])
    plt.plot(
        latitude, 
        longitude, 
        marker = "o", 
        markersize = 10, 
        markeredgecolor = "black", 
        markerfacecolor = "red"
    )
    plt.text(
        latitude + 17, 
        longitude - 17,
        'Latitude: ' + str(latitude) + '°\nLongitude: ' + str(longitude) + '°\nProbability: ' + str(round(prob[2], 3)) + '%',
        horizontalalignment = 'right',
        transform = ccrs.PlateCarree(),
        color = "red",
        font = "Arial",
        fontweight = "bold",
        backgroundcolor = 'white',
        alpha = .5,
    )
    plt.show()

# Function for grabbing user entry
def getCords():

    labelStats.configure(
            fg = "brown",
            bg = "beige",
            width = "40",
            height = "3",
            font = font_tuple
    )

    try:
        longitude = float(longitudeEntry.get())
        latitude = float(latitudeEntry.get())

        if latitude > 56 or latitude < -34 or longitude > 160 or longitude < - 164:
            labelStats.configure(text = "Not supported\n -34 < lat. < 56 | -164 < long. < 160")
        else:
            prob = pirateProbability.prob(latitude, longitude)
            labelStats.configure(text = f"The probability of being attacked \n at ({round(latitude, 3)}, {round(longitude, 3)}) is {str(round(prob[2], 3))}%")
            plotMap(longitude, latitude, prob)
    except ValueError as error:
        print(error)
        labelStats.configure(text = "Please enter a number!")

    longitudeEntry.delete(first = 0, last = 100)
    latitudeEntry.delete(first = 0, last = 100)

# Main title Label
label = tk.Label(
    text = "Will you be attacked by Pirates?\nEnter your coords to find out!",
    fg = "beige",
    bg = "brown",
    width = "10000",
    height = "3",
    font = font_tuple,
    pady = "1"
)

font_tuple = ("Javanese Text", 14, "bold")

# Latitude Label
labelLat = tk.Label(
    text = "Latitude",
    fg = "brown",
    bg = "beige",
    width = "25",
    height = "1",
    font = font_tuple
)

# Latitude Entry Box
latitudeEntry = tk.Entry(
    fg = "brown",
    bg = "white",
    width = "40"
)

# Longitude Label
labelLong = tk.Label(
    text = "Longitude",
    fg = "brown",
    bg = "beige",
    width = "25",
    height = "1",
    font = font_tuple
)

# Longitude Entry Box
longitudeEntry = tk.Entry(
    fg = "brown",
    bg = "white",
    width = "40"
)

font_tuple = ("Javanese Text", 12, "bold")

# Button to enter statistics
button = tk.Button(
    window, 
    bg = "brown",
    fg = "beige",
    text = "Enter",
    width = "9",
    height = "1",
    command = getCords,
    font = font_tuple
)

# Adding the Cutlass
image = Image.open("Images/cutlass.png")
image = image.resize((110, 242), Image.Resampling.LANCZOS)
image = image.rotate(-15)
test = ImageTk.PhotoImage(image)
labelPic = tk.Label(image = test, bg = "beige")
labelPic.image = test
labelPic.place(x = 460, y = 230)

# Adding the second Cutlass
image = Image.open("Images/cutlassflipped.png")
image = image.resize((110, 242), Image.Resampling.LANCZOS)
image = image.rotate(15)
test = ImageTk.PhotoImage(image)
labelPic = tk.Label(image = test, bg = "beige")
labelPic.image = test
labelPic.place(x = 25, y = 230)


# Adding all the different things to the window
label.pack(
    pady = (0, 30)
)
labelLat.pack()
latitudeEntry.pack()
labelLong.pack(
    pady = (30, 0)
)
longitudeEntry.pack()
button.pack(
    pady = (25, 0)
)
labelStats.pack(
    pady = 30
)
window.mainloop()