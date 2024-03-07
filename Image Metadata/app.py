from flask import Flask, render_template, request
import os
from PIL import Image
from PIL.ExifTags import TAGS


app = Flask(__name__)

def getData(img):
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


@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        f = request.files['file']
        file_name = f.filename
        f.save(file_name)
        metadata = getData(file_name)
        print(metadata)
        os.remove(file_name)
  
        return render_template("index.html", metadataLis = metadata)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8000")


