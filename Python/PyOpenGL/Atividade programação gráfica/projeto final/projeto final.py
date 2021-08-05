#O seguinte projeto é uma simulação de um buraco negro. Não somente, mas diversos cubos são gerados de formas aleatória.


import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

max_distance = 500
cube_dict = {}
reiniciar = 0
velocidade = 0

def illuminar():
    luzAmbiente =[0.2,0.2,0.2,1.0]; 
    luzDifusa = [0.7,0.7,0.7,1.0];
    direction = [1.0, 1.0, -50.0];#pontiforme
    luzEspecular= [1.0, 1.0, 1.0, 1.0];
    posicaoLuz=[-1.0, -1.0, -10.0, 1.0];
    especularidade=[1.0,1.0,1.0,1.0]; 
    especMaterial = 60;
    glShadeModel(GL_SMOOTH);
    glMaterialfv(GL_FRONT,GL_SPECULAR, especularidade);
    glMateriali(GL_FRONT,GL_SHININESS,especMaterial);
    glLightfv(GL_LIGHT0, GL_AMBIENT, luzAmbiente); 
    glLightfv(GL_LIGHT0, GL_DIFFUSE, luzDifusa );
    glLightfv(GL_LIGHT0, GL_SPECULAR, luzEspecular );
    glLightfv(GL_LIGHT0, GL_POSITION, posicaoLuz );
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, direction);#pontiforme
    glLightf(GL_LIGHT0, GL_SPOT_EXPONENT , 1.0);#pontiforme
    glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 70.0);#pontiforme
    glEnable(GL_COLOR_MATERIAL);
    glEnable(GL_LIGHTING);
    glEnable(GL_LIGHT0);
    glEnable(GL_DEPTH_TEST);
    
vertices = (
    (2, -2, -2),
    (2, 2, -2),
    (-2, 2, -2),
    (-2, -2, -2),
    (2, -2, 2),
    (2, 2, 2),
    (-2, -2, 2),
    (-2, 2, 2)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

surfaces = (
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    )


colors = (
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),
    (1,1,1),    
)

def loadTexture():
    textureSurface = pygame.image.load('2.1.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    return texid

def set_vertices(max_distance):
    
    #distância entre blocos
    x_value_change = random.randrange(-50,50)
    y_value_change = random.randrange(-50,50)
    z_value_change = random.randrange(-1*max_distance,-20)

    new_vertices = []

    for vert in vertices:
        new_vert = []
        new_x = vert[0] + x_value_change
        new_y = vert[1] + y_value_change
        new_z = vert[2] + z_value_change

        new_vert.append(new_x)
        new_vert.append(new_y)
        new_vert.append(new_z)

        new_vertices.append(new_vert)

    return new_vertices
        
def Cube(vertices):
    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x = 0
        for vertex in surface:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(vertices[vertex])
            
            #Textura dos cubos
            glTexCoord2f(x, -x)
            
    glEnd()
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def draw_cube(lines=False):
        glBegin(GL_QUADS)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-300.0, -300.0, -500)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-300.0,  300.0, -500)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(300.0,  300.0, -500)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(300.0, -300.0, -500)
        glEnd()
        
        #rotação da textura de fundo
        glRotatef (0.2, 0, 0, 0.2)

def main():
    global velocidade, reiniciar
    pygame.init()
    display = (1500,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    loadTexture()
    
    gluPerspective(45, (display[0]/display[1]), 0.1, 50000.0)
    
    #minha posicção inicial
    glTranslatef(random.randrange(-5,5),random.randrange(-5,5), -490)
    
    #quantidade de cubos
    for x in range(200):
        cube_dict[x] = set_vertices(max_distance)

    x_move = 0
    y_move = 0
    
    #bindando keys
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = 0.3
                if event.key == pygame.K_RIGHT:
                    x_move = -0.3

                if event.key == pygame.K_UP:
                    y_move = -0.3
                if event.key == pygame.K_DOWN:
                    y_move = 0.3
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = 0.3

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_move = 0
        
        glGetDoublev(GL_MODELVIEW_MATRIX)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        #Velocidade percorrer
        velocidade += 0.03
        glTranslatef(x_move,y_move,velocidade)
        if velocidade >= 8.5:
            reiniciar -= 0.2
            glTranslatef(0,0, reiniciar)

        #Produzindo os cubos
        draw_cube(lines=False) 
        for each_cube in cube_dict:
            Cube(cube_dict[each_cube])
        
        #Illuminação para ver os objetos
        illuminar()
        pygame.display.flip()
        pygame.time.wait(10)

main()
pygame.quit()
quit()
