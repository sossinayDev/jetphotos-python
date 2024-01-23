# jetphotos-python
Access jetphoto images with python. Made by sossinay
## get_picture_links(url, lenlimit)
Used to get the links of the image-pages from an url.
### Parameters:
url: The url to access. For example: "https://www.jetphotos.com/new"
lenlimit: The amount of full pictures being loaded before the script stops (If you want the 5 newest images, you won't have to

### Output:
Array containing urls to the full pictures. 
Example:
```
get_picture_links("https://jetphotos.com/new",3)
>>> ['https://cdn.jetphotos.com/full/5/1755315_1704727568.jpg', 'https://cdn.jetphotos.com/full/5/808520_1704727553.jpg', 'https://cdn.jetphotos.com/full/6/1436774_1704727507.jpg']
```
## get_pictures(url, sort, count)
Used to get a certain amount of images, sorted by criteria.

### Parameters:
url: The url to access. For example: "https://www.jetphotos.com/new"
sort: Way to sort. Either "newest", "oldest" or "random".
count: Amount of images. Type: int

### Output
