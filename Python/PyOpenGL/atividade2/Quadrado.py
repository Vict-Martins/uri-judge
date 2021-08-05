from OpenGL.GL import *
from OpenGL.GLUT import *

def drawl():
        glClearColor(1.0, 1.0, 1,0)
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3d(0.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        glVertex2d(-0.5, -0.5)
        glVertex2d(0.5, -0.5)
        glVertex2d(0.5, 0.5)
        glVertex2d(-0.5, 0.5)
        glEnd()
        glFlush()

glutInit() # Iniciando o glut
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB) #tipo de display simples ou colorido RGB
glutCreateWindow(b'quadrado') #criando a tela e nomeando
glutInitWindowSize(500, 500) # tamanho da tela
glutDisplayFunc(drawl) #invocando o função
glutMainLoop() # Fazendo acontecer
