from PIL import Image



images = [Image.open(f"./images/{n:003}.png") for n in range(361)]
images[0].save("vMap.gif", save_all=True, append_images=images[1:], duration=20, loop=0)