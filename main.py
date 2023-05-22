from PIL import Image
from urllib.request import urlopen
url = "https://sun9-52.userapi.com/impg/9LCreE_iiNTUBS9t1dSgv0svtRPyY2TEua6DFQ/BdefCxnSfC0.jpg?size=1179x747&quality=95&sign=33f58fb0c613cb1424c0dcb514936f18&type=album"

image = Image.open(urlopen(url))
image.show()
