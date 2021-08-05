import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def triangle():
    
        glBegin( GL_TRIANGLES )
        glVertex2f( 200, 200)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f( 250, 300)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f( 300, 200)
        glColor3f(0.0, 0.0, 1.0)
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

    glScaled(0.5, 0.5, 0)
    glRotated(10, 15, 0.0, 1.0)
    glTranslated(400.0, 230.0, 0.0)
    triangle()
    
    
    glRotated(20, 0.0, 0.0, 1.0)
    glTranslated(90, 20, 0.0)
    triangle()

    glRotated(50, 0.0, 0.0, 1.0)
    glTranslated(110, -150, 0.0)
    triangle()
     
    glRotated(50, 0.0, 0.0, 1.0)
    glTranslated(120, -150, 0.0)
    triangle()
    
    glRotated(50, 0.0, 0.0, 1.0)
    glTranslated(120, -150, 0.0)
    triangle()

    glRotated(50, 0.0, 0.0, 1.0)
    glTranslated(150, -150, 0.0)
    triangle()

    glRotated(50, 0.0, 0.0, 1.0)
    glTranslated(150, -150, 0.0)
    triangle()

    glRotated(50, 0.0, 0.0, 1.0)
    glTranslated(150, -150, 0.0)
    triangle()

    


    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
