import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def quad_strip():
        glColor3f(1.0 ,1.0 ,1.0)
        glBegin(GL_QUAD_STRIP)
        glVertex2f( 30, 400)
        glVertex2f( 30, 370)
        glVertex2f( 50, 403)
        glVertex2f( 50, 367)
        glVertex2f( 70, 410)
        glVertex2f( 70, 360)
        glVertex2f( 90, 400)
        glVertex2f( 90, 370)
        glEnd()


def triangle_fan():
        glColor3f(1.0 ,1.0 ,1.0)
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f( 430, 450)
        glVertex2f( 410, 490)
        glVertex2f( 390, 440)
        glVertex2f( 435, 420)
        glVertex2f( 470, 440)
        glVertex2f( 450, 490)
        glEnd()

def triangle_strip():
        glColor3f(1.0 ,1.0 ,1.0)
        glBegin(GL_TRIANGLE_STRIP)
        glVertex2f( 270, 490)
        glVertex2f( 290, 450)
        glVertex2f( 310, 490)
        glVertex2f( 330, 450)
        glVertex2f( 350, 490)
        glVertex2f( 370, 450)
        glEnd()


def poligon():
        glColor3f(1.0 ,1.0 ,1.0)
        glBegin(GL_POLYGON)
        glVertex2f( 190, 490)
        glVertex2f( 180, 470)
        glVertex2f( 170, 450)
        glVertex2f( 180, 430)
        glVertex2f( 190, 410)
        glVertex2f( 230, 410)
        glVertex2f( 250, 450)
        glVertex2f( 230, 490)
        glEnd()

def square():
        glBegin( GL_QUADS )
        glVertex2f( 200, 240)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f( 250, 220)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f( 300, 240)
        glColor3f(0.5, 0.1, 0.8)
        glVertex2f( 250, 260)
        glColor3f(1.0, 0.0, 0.0)
        glEnd()

def square1():
       
        glBegin( GL_QUADS )
        glVertex2f( 250, 180)
        glColor3f(0.5, 0.1, 0.8)
        glVertex2f( 250, 220)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f( 300, 240)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f( 300, 200)
        glColor3f(1.0, 0.0, 0.0)
        glEnd()

def square2():
        glBegin( GL_QUADS )
        glVertex2f( 200, 240)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f( 200, 200)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f( 250, 180)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f( 250, 220)
        glColor3f(0.5, 0.1, 0.8)
        glEnd()

def triangle():
    
        glBegin( GL_TRIANGLES )
        glVertex2f( 250, 400)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f( 200, 300)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f( 250, 290)
        glColor3f(0.0, 0.0, 1.0)
        glEnd()

def triangle1():
        glColor3f(1.0, 1.0, 1.0)
        glBegin( GL_TRIANGLES )
        glVertex2f( 250, 400)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f( 250, 290)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f( 300, 300)
        glColor3f(1.0, 0.0, 0.0)
        glEnd()


def line():
        glColor3f(1.0, 1.0, 1.0)
        glBegin( GL_LINES )
        glVertex2f( 30, 490)
        glVertex2f( 30, 450)
        glEnd()

def point():
    glBegin( GL_POINTS)
    glVertex2f( 10,490)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    triangle()
    
    triangle1()
    
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
