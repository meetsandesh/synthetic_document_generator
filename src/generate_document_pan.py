from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import os
import sys

class PanData:
    applicant_name: ""
    father_name: ""
    pan_value: ""
    dob: ""


fake = Faker()
font = ImageFont.truetype("arialbd.ttf", 105)
font_sign = ImageFont.truetype("segoesc.ttf", 100)
args = sys.argv
max_pan = int(args[1])
pan_data = 1
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']


def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s/%s ...%s\r' % (bar, str(count), str(total), suffix))
    sys.stdout.flush()


def createDatasetFolders():
    newpath = r'../generated_documents'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/images'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/images/pan_v1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata/pan_v1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def generate_pan(temp):
    pan = ""
    for c in range(9):
        a = int(temp % 10)
        temp /= 10
        if 0 < c < 5:
            pan = str(a) + pan
        else:
            pan = alphabets[a] + pan
    return pan


def get_pan_metadata(temp):
    p = PanData()
    p.applicant_name = fake.name()
    p.father_name = fake.name()
    p.pan_value = generate_pan(temp)
    date = fake.date().split("-")
    p.dob = date[2] + "/" + date[1] + "/" + date[0]
    return p


createDatasetFolders()
for i in range(max_pan):
    pan = get_pan_metadata(pan_data)
    image = Image.open("../base_documents/PAN_V1.jpg")
    draw = ImageDraw.Draw(image)
    draw.text((120, 570), pan.applicant_name.upper(), font=font, fill=(0, 0, 0))
    draw.text((120, 810), pan.father_name.upper(), font=font, fill=(0, 0, 0))
    draw.text((120, 1090), pan.dob, font=font, fill=(0, 0, 0))
    draw.text((120, 1370), pan.pan_value, font=font, fill=(0, 0, 0))
    draw.text((120, 1700), pan.applicant_name.split(" ")[0], font=font_sign, fill=(0, 0, 0))
    image.save("../generated_documents/images/pan_v1/pan_v1_" + str(pan_data) + ".jpg")
    file1 = open("../generated_documents/metadata/pan_v1/pan_v1_" + str(pan_data) + ".txt", "w")
    L = [pan.applicant_name + "::" + pan.father_name + "::" + pan.pan_value + "::" + pan.dob]
    file1.writelines(L)
    file1.close()
    progress(i + 1, max_pan, "PAN Generated")
    pan_data += 1
