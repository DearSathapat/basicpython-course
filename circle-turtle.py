Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> tao = turtle.Pen()
>>> tao.shape('turtle')
>>> tao.color('green')
>>> 
>>> def circle():
	for i in range(10):
		tao.forward(40)
		tao.left(36)
		tao.circle(60)
		tao.left(36)

		
>>> def Go(x,y);
SyntaxError: invalid syntax
>>> def Go(x,y):
	tao.penup()
	tao.goto(x,y)
	tao.pendown()

	
>>> circle()
>>> Go(200,200)
>>> tao.color('blue')
>>> circle()
>>> Go(-200,0)
>>> tao.color('red')
>>> circle()
>>> tao.forward(20)
>>> tao.right(90)
>>> tao.color('black')
>>> tao.forward(100)
>>> tao.color('violet')
>>> circle()
>>> 
