#Modificando Escala, translação e rotação

import OpenGL
import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
  
def triangle():
    glBegin( GL_TRIANGLES )
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f( -100.0, -100.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f( 100.0, -100.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f( 0.0, 100.0)
    glEnd()
    
def eixoXY():
    glColor3f(1.0, 1.0, 1.0)
    glBegin( GL_LINES )
    glVertex2f(-200,0)
    glVertex2f(200,0)
    glEnd()
    glBegin( GL_LINES )
    glVertex2f(0,-200)
    glVertex2f( 0,200)
    glEnd()

def iterate():
    glViewport(0, 0, 400, 400)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200.0, 200, -200.0, 200, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    triangle()

    cos = math.cos(math.radians(40))
    sin = math.sin(math.radians(40))
    m = np.array([
        cos, -sin, 0.0, 0.0, 
        sin, cos, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        90.0, 90.0, 0.0, 2.0])
    
 
    glLoadMatrixf(m)
    triangle()
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(400, 400)
glutInitWindowPosition(-200, -200)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
