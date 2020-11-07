def encode_enc(newimg,data):
	w=newimg.size[0]
	(x,y)=(0,0)

	for pixel in modPix(newimg.getdata(),data):
		newimg.putpixel((x,y),pixel)
		if(x==w-1):
			x=0
			y+=1
		else:
			x+=1