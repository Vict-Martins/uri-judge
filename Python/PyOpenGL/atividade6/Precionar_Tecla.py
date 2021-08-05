#Objetos Wire e Solid com controle via teclado
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def tecla(key, x, y):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    if key == b"q":
        glColor3f(1.0, 0.0, 0.0)
        glRotated(20.0, 1.0, 0.0, 1.0)
        glutSolidSphere(100, 50, 50)
    elif key == b"w":
        glColor3f(1.0, 0.0, 0.0)
        glRotated(20.0, 1.0, 0.0, 1.0)
        glutWireSphere(100, 50, 50)
    elif key == b"e":
        glColor3f(1.0, 1.0, 0.0)
        glRotated(20.0, 1.0, 0.0, 1.0)
        glutSolidCube(150)
    elif key == b"r":
        glColor3f(1.0, 1.0, 0.0)
        glRotated(20.0, 1.0, 0.0, 1.0)
        glutWireCube(150)
    elif key == b"t":
        glColor3f(1.0, 1.0, 1.0)
        glRotatef(45.0, 1.0, 0.0, 1.0)
        #glTranslated(100.0, 100.0, 0.0)
        glutSolidCone(50, 100, 10, 20)
    elif key == b"y":
        glColor3f(1.0, 1.0, 1.0)
        glRotatef(45.0, 1.0, 0.0, 1.0)
        #glTranslated(100.0, 100.0, 0.0)
        glutWireCone(50, 100, 10, 20)
    elif key == b"u":
        glColor3f(1.0, 0.0, 1.0)
        glRotatef(45.0, 1.0, 0.0, 1.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glutSolidTorus(10, 100, 10, 20)
    elif key == b"i":
        glColor3f(1.0, 0.0, 1.0)
        glRotatef(45.0, 1.0, 0.0, 1.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glutWireTorus(10, 100, 10, 20)
    elif key == b"o":
        glColor3f(0.0, 1.0, 1.0)
        glRotatef(25.0, 1.0, 0.0, 1.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutSolidDodecahedron()
    elif key == b"p":
        glColor3f(0.0, 1.0, 1.0)
        glRotatef(25.0, 1.0, 0.0, 1.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutWireDodecahedron()
    elif key == b"a":
        glColor3f(0.0, 1.0, 0.0)
        glRotatef(25.0, 1.0, 1.0, 0.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutSolidOctahedron()
    elif key == b"s":
        glColor3f(0.0, 1.0, 0.0)
        glRotatef(25.0, 1.0, 1.0, 0.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutWireOctahedron()
    elif key == b"d":
        glColor3f(0.0, 0.0, 1.0)
        glRotatef(25.0, 1.0, 0.0, 1.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutSolidTetrahedron()
    elif key == b"f":
        glColor3f(0.0, 0.0, 1.0)
        glRotatef(25.0, 1.0, 0.0, 1.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutWireTetrahedron()
    elif key == b"g":
        glColor3f(1.0, 1.0, 1.0)
        glRotatef(60.0, 1.0, 1.0, 0.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutSolidIcosahedron()
    elif key == b"h":
        glColor3f(1.0, 1.0, 1.0)
        glRotatef(60.0, 1.0, 1.0, 0.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glScaled(50,50,50);
        glutWireIcosahedron()
    elif key == b"j":
        glColor3f(1.0, 1.0, 0.0)
        glRotatef(40.0, 1.0, 1.0, 0.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glutSolidTeapot(60)
    elif key == b"k":
        glColor3f(1.0, 1.0, 0.0)
        glRotatef(40.0, 1.0, 1.0, 0.0)
        #glTranslated(-100.0, -100.0, 0.0)
        glutWireTeapot(60)
            

    glutSwapBuffers()
    
def iterate():
    glViewport(0, 0, 1980, 1020)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-200.0, 200, -200.0, 200, -100.0, 100.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
      

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(1980, 1020)
glutInitWindowPosition(-400, -400)
glutCreateWindow("OpenGL")

glutSwapBuffers()
glutDisplayFunc(iterate)
glutKeyboardFunc(tecla)
glutIdleFunc(iterate)

glutMainLoop()



