from ursina import *
from panda3d.core import Fog

app = Ursina()

r = 8
for i in range(1, r):
    t = i/r
    s = 4*i
    print(s)
    grid = Entity(model=Grid(s,s), scale=s, color=color.color(0,0,.8,lerp(.8,0,t)), rotation_x=90, position=(-s/2, i/1000, -s/2))
    subgrid = duplicate(grid)
    subgrid.model = Grid(s*4, s*4)
    subgrid.color = color.color(0,0,.4,lerp(.8,0,t))
    model = Entity(model="Block01", collider="mesh", texture="white_cube", position=(-100, 0, 0))

    EditorCamera()

    # config # 

model1 = "Block05"
model2 = "Block01"
#seperation between Columns:
sepm = 60
# Seperation between Rows:
sepb = 30
#X/Y Position of block:
x = -35
y = -120
#Rotation of ALL models:
z = 0
#Shader
#shader = lit_with_shadows_shader
#shader2 = lit_with_shadows_shader
#shader3= normals_shader

#	#	#

def spawnblock(x=None, y=None, z=None, m=None, t=None):
	#x = xpos, y = ypos, z = rotation, m = model, t = texture
	if m == None:
		rnt1 = random.randint(1,2)
		if rnt1 == 1:
			m = model1
		if rnt1 == 2:
			m = model2
	else: m = m
	if t == None:
		rnt2 = random.randint(1,2)
		if rnt2 == 1:
			t = "Brick"
		if rnt2 == 2:
			t = "white_cube"
	else: t = t

	if x==None:x==None
	else:x==x
	if y==None:y==None
	else:y==y
	if z==None:z==None
	else:z==z

	block = Entity(model=m, collider="mesh", texture=t, texture_scale=(100, 100), position=(x, 0, y), rotation=(0,z,0), shader=shader)




def spawnblock7(sepm=None, z=None, m=None, t=None):
	#sepm = seperation between rows, z = Rotation
	if m==None:m==None
	else:m==m
	if t==None:t==None
	else:t==t
	### Random Rotation needs fixing (z):
	i = [z,z,z,z,z,z,z]
	if z==None:
		for i in i:
			temp = random.randint(1,4)
			if temp == 1:
				z = 0
			if temp ==2:
				z = 90
			if temp == 3:
				z = 180
			if temp == 4:
				z = 270
	else:
		z=z

	if sepm==None:sepm=sepm
	else:sepm=sepm

	sb = [ 	
	spawnblock(x+sepm, y + sepb*-1*3, z, m, t),
	spawnblock(x+sepm, y + sepb*-1*2, z, m, t),
	spawnblock(x+sepm, y + sepb*-1, z, m, t),
	spawnblock(x+sepm, y, z, m, t),
	spawnblock(x+sepm, y + sepb, z, m, t),
	spawnblock(x+sepm, y + sepb*2, z, m, t),
	spawnblock(x+sepm, y + sepb*3, z, m, t),
	]


### Main ###
#Enter 
#spawnblock(NUMBER OF HOUSES IN ROW, sb BETWEEN ROWS, ROTATION OF ROW MODELS, MODEL, TEXTURE)

spawnblock7(sepm, z+180, model1)
spawnblock7(0, z+0, model1)
spawnblock7(sepm+45, z+90, model2)
spawnblock7(-45, z+-90, model2)

app.run()