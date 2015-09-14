def growRect(box, dwidth, dheight):
	box.width = box.width + dwidth
	box.height = box.height + dheight


bob=Rectangle()
bob.width = 100.0
bob.height = 200.0
bob.corner = Point()
bob.corner.x = 0.0
bob.corner.y = 0.0
growRect(bob, 50.0 , 100.0)