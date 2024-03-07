from PIL import Image
from PIL.ExifTags import TAGS

imagename = "image.jpg"

# read the image data using PIL
def getData(img):
    # image = Image.open("20221106_123656.jpg")
    image = Image.open(img)

    info_dict = {
        "Filename": image.filename,
        "Image Size": image.size,
        "Image Height": image.height,
        "Image Width": image.width,
        "Image Format": image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated", False),
        "Frames in Image": getattr(image, "n_frames", 1)
    }
    lis=[]
    for label,value in info_dict.items():
        # lis.append([{label:25},{value}])
        # lis.append(f"{label:25}: {value}")
        lis.append([label,value])
        # print(f"{label:25}: {value}")
    exifdata = image.getexif()
    for tag_id in exifdata:
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        # lis.append([{tag:25},{data}])
        # lis.append(f"{tag:25}: {data}")
        lis.append([tag,data])

        # print(f"{tag:25}: {data}")

    return(lis)
print(getData("20221106_123656.jpg"))