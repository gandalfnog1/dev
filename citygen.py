from ursina import *
from random import uniform
import random
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
# (normals_shader, noise_fog_shader)


app=Ursina()
#e = Entity(shader=noise_fog_shader)

Sky(color=color.light_gray)


player=FirstPersonController(y=2, origin_y=-.5)
#player.speed = 35
#player.jump_height = 35
#player.jump_duration = 0.5
player.cursor = None
player.fov = 100
mapscale = 800
ground=Entity(model='plane', scale=(mapscale, 1, mapscale), color=(color.dark_gray), texture="Brick",
	texture_scale=(mapscale, mapscale), collider='box', shader=shader
)
#e = Entity(shader=normals_shader)

def input(key):
	if key == 'shift': 
		player.speed=15
		player.jump_height = 4
		player.jump_duration = 0.5

	if key == 'tab': 
		player.speed=5
		player.jump_height = 2
		player.jump_duration = 0.5

#Generating City

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
shader = lit_with_shadows_shader
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
#spawnblock(x, y, z+180)
app.run()
run()