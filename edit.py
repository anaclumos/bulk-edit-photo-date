import os

from PIL import Image
import piexif

path = "./photos"


def runFunctionForAllFilesIn(path, functionname):
    if os.path.isdir(path):
        for dirpath, dirname, filenames in os.walk(path):
            for i in filenames:
                functionname(path + "/" + i)


def inferExifFromFilename(filename):
    print(filename)
    year, month, date, hour, minute, second, *number = (
        filename.split("/")[-1]
        .replace(".png", "")
        .replace("Screenshot_", "")
        .split("-")
    )
    date = year + ":" + month + ":" + date + " " + hour + ":" + minute + ":" + second
    exif_ifd = {
        piexif.ExifIFD.DateTimeOriginal: date,
    }
    exif_dict = {
        "Exif": exif_ifd,
    }
    print(exif_dict)
    return exif_dict


def savePngAsJpgWithExif(png, exif_dict):
    src = Image.open(png)
    jpg = src.convert("RGB")
    exif_bytes = piexif.dump(exif_dict)
    jpg.save(png + ".jpg", exif=exif_bytes)


def operation(filename):
    if ".png" not in filename:
        return
    exif_data = inferExifFromFilename(filename)
    savePngAsJpgWithExif(filename, exif_data)
    print("saved: ", filename)
    print()


runFunctionForAllFilesIn("./imgs", operation)
print("end")
