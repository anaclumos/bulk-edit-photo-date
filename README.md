# Bulk Edit Photo Dates

## Problem:
* I had an old pile of PNGs that did not have timestamp metadata.
* Therefore it displayed the imported time when I imported them on any Photo Library.
* I wanted them to be organized to the exact datetime from when they were taken.
* Thankfully the timestamp data was preserved by the title of the file.

## But why:
* I eventually found that PNG did not have EXIF metadata format before like 2017.
* Very little resources and data are open for PNG+EXIFs. I have tried multiple libraries and codeblocks but no luck at all.
* So I have decided to preserve the original files somewhere else and import JPG versions with correct EXIF timestamps to my photo library. 
* Note that converting PNG Screenshots to JPG could have some quality loss. PRs or Emails are welcomed if you know a better way.

## How does it work:
1. Process PNG screenshot title and create EXIF data from it (uses `piexif` library)
2. Create a JPG image from PNG Image and embed EXIF (uses `pillow` library)
3. Repeat that for all files on specific directory

## I wanna know more on EXIFs:
* [EXIF Tags](https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif.html)
* [DateTimeOriginal](https://www.awaresystems.be/imaging/tiff/tifftags/privateifd/exif/datetimeoriginal.html) key for EXIF files is `36867`. Took me long enough to figure this out.
* Eventually the [Piexif docs - `Dump`](https://piexif.readthedocs.io/en/latest/functions.html#dump) saved my day.
