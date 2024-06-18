from faker import Faker
from PIL import Image, ImageDraw, ImageFont
import os
import sys

class VoterCardData:
    applicant_name: ""
    applicant_name_hi: ""
    husband_name: ""
    husband_name_hi: ""
    votercard_value: ""
    dob: ""
    gender: ""
    gender_hi: ""


fake = Faker()
faker_hi = Faker("hi_IN")
font = ImageFont.truetype("arial.ttf", 80)
font_bd = ImageFont.truetype("arialbd.ttf", 80)
font_bd_1 = ImageFont.truetype("arialbd.ttf", 90)
font_2 = ImageFont.truetype("arial.ttf", 70)
font_hi = ImageFont.truetype("C:/Users/meets/OneDrive/Desktop/MS Thesis Work/Code/Nirmala.ttf", 80)
font_hi_2 = ImageFont.truetype("C:/Users/meets/OneDrive/Desktop/MS Thesis Work/Code/Nirmala.ttf", 70)
args = sys.argv
max_votercard = int(args[1])
votercard_data = 1
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
    newpath = r'../generated_documents/images/votercard_v1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata'
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    newpath = r'../generated_documents/metadata/votercard_v1'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def generate_votercard(temp):
    votercard = ""
    for c in range(10):
        a = int(temp % 10)
        temp /= 10
        if c < 7:
            votercard = str(a) + votercard
        else:
            votercard = alphabets[a] + votercard
    return votercard


def get_votercard_metadata(temp):
    p = VoterCardData()
    p.applicant_name = fake.name()
    p.applicant_name_hi = faker_hi.name()
    p.husband_name = fake.name()
    p.husband_name_hi = faker_hi.name()
    p.votercard_value = generate_votercard(temp)
    date = fake.date().split("-")
    p.dob = date[2] + "-" + date[1] + "-" + date[0]
    if (temp <= max_votercard * 0.4) or (max_votercard * 0.8 < temp <= max_votercard * 0.9):
        p.gender_hi = "पुरुष"
        p.gender = "Male"
    else:
        p.gender_hi = "महिला"
        p.gender = "Female"
    return p


createDatasetFolders()
for i in range(max_votercard):
    votercard = get_votercard_metadata(votercard_data)
    image = Image.open("../base_documents/VOTERCARD_V1.jpg")
    draw = ImageDraw.Draw(image)
    draw.text((260, 620), votercard.votercard_value, font=font_bd, fill=(0, 0, 0))
    draw.text((1290, 760), votercard.applicant_name_hi, font=font_hi, fill=(0, 0, 0))
    draw.text((1410, 870), votercard.applicant_name, font=font_bd_1, fill=(0, 0, 0))
    draw.text((1600, 1000), votercard.husband_name_hi, font=font_hi, fill=(0, 0, 0))
    draw.text((1950, 1120), votercard.husband_name, font=font_bd_1, fill=(0, 0, 0))
    draw.text((1720, 1240), votercard.gender_hi + " / " + votercard.gender, font=font_hi, fill=(0, 0, 0))
    draw.text((1940, 1540), votercard.dob, font=font, fill=(0, 0, 0))
    image.save("../generated_documents/images/votercard_v1/votercard_v1_" + str(votercard_data) + ".jpg")
    file1 = open("../generated_documents/metadata/votercard_v1/votercard_v1_" + str(votercard_data) + ".txt", "w")
    L = [votercard.applicant_name + "::" + votercard.husband_name + "::" + votercard.votercard_value + "::" + votercard.dob]
    file1.writelines(L)
    file1.close()
    progress(i + 1, max_votercard, "Passport Generated")
    votercard_data += 1
