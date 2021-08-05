#Projeto De um Dado que gira e mostra uma das faces de modo aleatório.
#As teclas A,S,D,W são utlizadas para modever o dado no plano, já as teclas c,v são utilizados para movimentar(da impressão de profundidade) no plano.

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import random

luz = False
lado = 0
altura = 0
prof = 10
I = 0
run = False
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0
id_textures = []

def create_gl_texture(width, height, pbits):
    id_texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, id_texture)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, pbits)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glGenerateMipmap(GL_TEXTURE_2D)
    return id_texture

def load_texture(filename):
    image = Image.open(filename)
    ix = image.size[0]
    iy = image.size[1]
    pbits = image.convert("RGBA").tobytes("raw", "RGBA")
    id_texture = create_gl_texture(ix, iy, pbits)
    return id_texture

def init_gl(Width, Height):
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width) / float(Height), 0.1, 500.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_TEXTURE_2D)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    #glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    #glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)

#BINDANDO A TECLA
def tecla(key, x, y):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global X_AXIS, Y_AXIS, Z_AXIS, run, I, prof, lado, altura, luz
    if key == b" ":
        if run == True:
            run = False
        else:
            run = True
    if key == b"l":
        if luz == True:
            luz = False
        else:
            luz = True
            glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        
    if key == b"1":
        X_AXIS = 0
        Y_AXIS = 0
        Z_AXIS = 0
    if key == b"2":
        X_AXIS = 180
        Y_AXIS = 0
        Z_AXIS = 0
    if key == b"3":
        X_AXIS = 90
        Y_AXIS = 0
        Z_AXIS = 0
    if key == b"4":
        X_AXIS = 270
        Y_AXIS = 0
        Z_AXIS = 0
    if key == b"5":
        X_AXIS = 0
        Y_AXIS = 270
        Z_AXIS = 0
    if key == b"6":
        X_AXIS = 0
        Y_AXIS = 90
        Z_AXIS = 0
    #CONTROLE DE VELOCIDADE
    if key == b"z":
        I += 2
        print(f'Velodidade:{I/2}')
    if key == b"x":
        I -= 2
        print(f'Velocidade:{I/2}')
    #CONTROLE DE PRONFUNDIDADE
    if key == b"c":
        prof += 2
        print(f'Profundidade:{prof}')
    if key == b"v":
        prof -= 2
        print(f'Profundidade:{prof}')
    if key == b"a":
        lado -= 1
        print(f'lado:{lado}')
    if key == b"d":
        lado += 1
        print(f'lado:{lado}')
    if key == b"w":
        altura += 1
        print(f'altura:{altura}')
    if key == b"s":
        altura -= 1
        print(f'altura:{altura}')


def illuminar():
 
    #luzAmbiente =[0.2,0.2,0.2,1.0]; 
    #luzDifusa = [0.7,0.7,0.7,1.0];
    direction = [0.0, 0.0, -2.0];#pontiforme
    #luzEspecular= [1.0, 1.0, 1.0, 1.0];
    posicaoLuz=[1.0, 1.0, -10.0, 1.0];
    #especularidade=[1.0,1.0,1.0,1.0]; 
    #especMaterial = 60;
    #glShadeModel(GL_SMOOTH);
    #glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade);
    #glMateriali(GL_FRONT,GL_SHININESS,especMaterial);

    #glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente); 
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa );
    #glLightfv(GL_LIGHT, GL_SPECULAR, luzEspecular );
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz );
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, direction);#pontiforme
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT , 1.0);#pontiforme
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 70.0);#pontiforme
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    #glEnable(GL_DEPTH_TEST);

def rotacionar_cubo():
    global X_AXIS, Y_AXIS, Z_AXIS, run, parada, X ,Y ,Z , I
    parada = random.randint(2880,14400)
    if run == True:
        X_AXIS += random.randint(1,I)
        Y_AXIS += random.randint(1,I)
        Z_AXIS += random.randint(1,I)
        print(f'{X_AXIS}, {Y_AXIS}, {Z_AXIS}')

    #PARAMENTRO DE PARADA DO DADO
    if (X_AXIS >= parada) or (Y_AXIS >= parada) or (Z_AXIS >= parada):
        
        run = False
        X = X_AXIS%((0 + 360) + 1)
        Y = Y_AXIS%((0 + 360) + 1)
        Z = Z_AXIS%((0 + 360) + 1)

        print(f'Sem Correção\nX={X}\nY={Y}\nZ={Z}')
        
        #TRATAMENTO X
        if X > 0 and X <= 45:
            X_AXIS = 0
        elif X > 45 and X <= 90:
            X_AXIS = 90
        elif X > 90 and X <= 135:
            X_AXIS = 90
        elif X > 135 and X <= 180:
            X_AXIS = 180
        elif X > 180 and X <= 225:
            X_AXIS = 180
        elif X > 225 and X <= 270:
            X_AXIS = 270
        elif X > 270 and X <= 315:
            X_AXIS = 270
        elif X > 315 and X <= 360:
            X_AXIS = 360
            
        #TRATAMENTO Y
        if Y > 0 and Y <= 45:
            Y_AXIS = 0
        elif Y > 45 and Y <= 90:
            Y_AXIS = 90
        elif Y > 90 and Y <= 135:
            Y_AXIS = 90
        elif Y > 135 and Y <= 180:
            Y_AXIS = 180
        elif Y > 180 and Y <= 225:
            Y_AXIS = 180
        elif Y > 225 and Y <= 270:
            Y_AXIS = 270
        elif Y > 270 and Y <= 315:
            Y_AXIS = 270
        elif Y > 315 and Y <= 360:
            Y_AXIS = 360
            
        #TRATAMENTO Z
        if Z > 0 and Z <= 45:
            Z_AXIS = 0
        elif Z > 45 and Z <= 90:
            Z_AXIS = 90
        elif Z > 90 and Z <= 135:
            Z_AXIS = 90
        elif Z > 135 and Z <= 180:
            Z_AXIS = 180
        elif Z > 180 and Z <= 225:
            Z_AXIS = 180
        elif Z > 225 and Z <= 270:
            Z_AXIS = 270
        elif Z > 270 and Z <= 315:
            Z_AXIS = 270
        elif Z > 315 and Z <= 360:
            Z_AXIS = 360

        print(f'Com Correção\nX={X_AXIS}\nY={Y_AXIS}\nZ={Z_AXIS}')

def showScreem():
    global X_AXIS, Y_AXIS, Z_AXIS, prof, lado, altura
    global id_textures
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glLoadIdentity()
    glTranslatef(lado, altura, -prof)
    #print(f'{lado}, {altura}, {prof}')
    #glClearColor(1.0,1.0, 0.0, 1.0);

    glRotatef(X_AXIS, 1.0, 0.0, 0.0)
    glRotatef(Y_AXIS, 0.0, 1.0, 0.0)
    glRotatef(Z_AXIS, 0.0, 0.0, 1.0)

    glBindTexture(GL_TEXTURE_2D, id_textures[0])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glEnd()
    

    glBindTexture(GL_TEXTURE_2D, id_textures[1])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[2])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[3])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[4])
    glBegin(GL_QUADS)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0,  1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1.0, -1.0,  1.0)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, id_textures[5])
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.0, -1.0,  1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.0,  1.0,  1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0,  1.0, -1.0)
    glEnd()
    #CHAMADA DO CUBO
    rotacionar_cubo()
    glutSwapBuffers()

def load_textures():
    global id_textures
    id_textures.append(load_texture("1.png"))
    id_textures.append(load_texture("2.png"))
    id_textures.append(load_texture("3.png"))
    id_textures.append(load_texture("4.png"))
    id_textures.append(load_texture("5.png"))
    id_textures.append(load_texture("6.png"))

def main():
    
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(400, 300)
    glutCreateWindow(b'Projeto CG UESC')
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    init_gl(800, 600)
    load_textures()
    glutDisplayFunc(showScreem)
    glutIdleFunc(showScreem)
    glutKeyboardFunc(tecla)
    #illuminar()
    glutMainLoop()

main()

