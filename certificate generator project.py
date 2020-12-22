from PIL import Image,ImageDraw,ImageFont
import pandas  as  pd
df =pd.read_excel("Book.xlsx")
for index,j in df.iterrows():
    img=Image.open('template.jpeg')
    draw=ImageDraw.Draw(img)
    draw.text(xy=(370,350),text='{}'.format(j['Name']),file=(0,137,209),font=ImageFont.truetype('arial.ttf',100))
    draw.text(xy=(290,580),text='{}'.format(j['Project name']),file=(0,0,102),font=ImageFont.truetype('arial.ttf',75))
    draw.text(xy=(140,740),text='{}'.format(j['Mentor name']),file=(102,0,51),font=ImageFont.truetype('arial.ttf',30))
    draw.text(xy=(810,740),text='{}'.format(j['Project manager']),file=(102,0,51),font=ImageFont.truetype('arial.ttf',30))
    draw.text(xy=(650,870),text='{}'.format(j['Certificate number']),file=(0,137,209),font=ImageFont.truetype('arial.ttf',25))
    img.save('Certificates\{}.jpj'.format(j['Name']))
print("success")
