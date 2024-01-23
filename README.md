# jetphotos
Access jetphoto images with python. Made by sossinay
## get_picture_links(url, lenlimit)
Used to get the links of the image-pages from an url.
### Parameters:
url: The url to access. For example: "https://www.jetphotos.com/new"<br />
lenlimit: The amount of pictures being loaded before the script stops (If you want the 5 newest images, you won't have to

### Output:
Array containing urls to the picture page (Including author, like, album etc.)
Example:
``` Python
get_picture_links("https://jetphotos.com/new",3)
#>>> ['https://www.jetphotos.com/photo/11202812', 'https://www.jetphotos.com/photo/11202811', 'https://www.jetphotos.com/photo/11202810']
```
## get_pictures(url, sort, count)
Used to get a certain amount of images, sorted by criteria.

### Parameters:
url: The url to access. For example: "https://www.jetphotos.com/new"<br />
sort: Way to sort. Either "newest", "oldest" or "random".<br />
count: Amount of images. Type: int

###  Output
Array containing urls to the full pictures.
Example:
``` Python
get_pictures("https://jetphotos.com/new","random",4)
#>>> ['https://cdn.jetphotos.com/full/6/581667_1704736418.jpg', 'https://cdn.jetphotos.com/full/6/2102927_1704736184.jpg', 'https://cdn.jetphotos.com/full/6/1334877_1704736946.jpg', 'https://cdn.jetphotos.com/full/6/1545021_1704736104.jpg']
```

## get_picture(url, sort)

Basically get_pictures(url, sort, 1)[0]

### Output:
String. Full Image URL

## Download image(url, path)
Downloads an image from a link and writes it to a file

### Parameters:
url: Url of an online image<br />
path: Absolute or relative path to a file (doesn't have to exist)

### Output:

Example:
``` Python
download_image(get_picture("https://www.jetphotos.com/new","random"), "image.jpg")
```
![image](https://github.com/sossinayDev/jetphotos-python/assets/125735344/629cda92-bb06-431f-a80e-feda790080af)

## get_full_image(url)
Gets the image location on cdn.jetphotos.com (Full image, ready to download)
### Parameters:
url: Url of the picture page (For example: "https://www.jetphotos.com/photo/11202798")
### Output
Url as a string.<br />
Example:<br />
``` Python
get_full_image("https://www.jetphotos.com/photo/11202798")
#>>> https://cdn.jetphotos.com/full/6/1001879_1706005967.jpg
```
