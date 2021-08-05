from coordenadas import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Cubo():
    glBegin(GL_QUADS)
    for face in cube_faces:
        x = 0
        for vertex in face:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(cube_verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in cube_edges:
        for vertex in edge:
            glVertex3fv(cube_verticies[vertex])
    glEnd()

def Cadeira():
    glBegin(GL_QUADS)
    for face in chair_faces:
        x = 0
        for vertex in face:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(chair_verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in chair_edges:
        for vertex in edge:
            glVertex3fv(chair_verticies[vertex])
    glEnd()


def Diamante():
    glBegin(GL_QUADS)
    for face in diamont_faces:
        x = 0
        for vertex in face:
            x+=1
            glColor3fv(colors[x])
            glVertex3fv(diamont_verticies[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in diamont_edges:
        for vertex in edge:
            glVertex3fv(diamont_verticies[vertex])
    glEnd()

