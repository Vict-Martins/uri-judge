import OpenGL
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
    
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
    glOrtho(-200.0, 200, -200.0, 200, -100.0, 100.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
        
def esfera():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glutSolidSphere(100, 50, 50)
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glutWireSphere(100, 50, 50)
    glutSwapBuffers()

def cubo():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glutSolidCube(100)
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glutWireCube(100)
    glutSwapBuffers()

def cone():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glutSolidCone(50, 100, 10, 20)
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glutWireCone(50, 100, 10, 20)
    glutSwapBuffers()

def anel():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glutSolidTorus(10, 100, 10, 20)
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glutWireTorus(10, 100, 10, 20)
    glutSwapBuffers()

def decahedron():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glScaled(50,50,1);
    glutSolidDodecahedron()
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glScaled(50,50,1);
    glutWireDodecahedron()
    glutSwapBuffers()

def octahedron():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glScaled(50,50,1);
    glutSolidOctahedron()
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glScaled(50,50,1);
    glutWireOctahedron()
    glutSwapBuffers()

def tetrahedron():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glScaled(50,50,1);
    glutSolidTetrahedron()
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glScaled(50,50,1);
    glutWireTetrahedron()
    glutSwapBuffers()

def Icosahedron():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glScaled(50,50,1);
    glutSolidIcosahedron()
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glScaled(50,50,1);
    glutWireIcosahedron()
    glutSwapBuffers()

def Teapot():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    eixoXY()
    glColor3f(1.0, 0.0, 0.0)
    glRotatef(40.0, 1.0, 1.0, 0.0)
    glTranslated(-100.0, -100.0, 0.0)
    glutSolidTeapot(60)
    glLoadIdentity()
    glColor3f(0.0, 1.0, 0.0)
    glRotatef(45.0, 1.0, 1.0, 0.0)
    glTranslated(100.0, 100.0, 0.0)
    glutWireTeapot(60)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(400, 400)
glutInitWindowPosition(-200, -200)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(esfera)
glutIdleFunc(esfera)
glutMainLoop()

