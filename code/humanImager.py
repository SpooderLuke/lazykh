import argparse
import os.path
import numpy as np
import math
import shutil
import random
import argparse
import torch
from PIL import Image
print(torch.cuda.is_available())
from diffusers import StableDiffusionPipeline
from utils import removeTags, getFilenameOfLine, getTopic, capitalize

def renderTextCenteredAt(text):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))     
        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)


    for i in range(len(lines)):
        prompt = getTopic(lines[i])
        num_images = 1
        if prompt != None:
            images = pipe(prompt) 
            images.images[0]
            images.images[0].save(B_FOLDER + "/"+getFilenameOfLine(lines[i])+".png")
            switchLines(False)



parser = argparse.ArgumentParser(description='blah')
parser.add_argument('--input_file', type=str,  help='the script')
args = parser.parse_args()
INPUT_FILE = args.input_file
B_FOLDER = INPUT_FILE+"_billboards"

f = open(INPUT_FILE+".txt","r+")
lines = list(filter(None, f.read().split("\n"))) # Filter out empty lines, since those won't need drawings.
lines = list(filter(lambda line: "(" not in line,lines))
f.close()

pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)
pipe = pipe.to("cuda")

LINE_ON = 0

def switchLines(first):
    global LINE_ON
    global lastLineSwitchTime
    global texty
    global canvassy


    if not os.path.isdir(B_FOLDER):
        os.mkdir(B_FOLDER)
    while LINE_ON < len(lines) and os.path.exists(B_FOLDER + "/"+getFilenameOfLine(lines[LINE_ON])+".png"): # If you've already drawn that image, skip it and move on to the next one.
        LINE_ON += 1
        print(getFilenameOfLine(lines[LINE_ON]))

    print(B_FOLDER + "/"+getFilenameOfLine(lines[0])+".png")
    print(getFilenameOfLine(lines[0]))
    print(os.path.exists(B_FOLDER + "/"+getFilenameOfLine(lines[0])+".png"))

    renderTextCenteredAt(lines[LINE_ON])

switchLines(False)