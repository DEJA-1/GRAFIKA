#!/usr/bin/env python3
import sys

from glfw.GLFW import *

from OpenGL.GL import *
from OpenGL.GLU import *

CONST_WINDOW_WIDTH = 1400
CONST_WINDOW_HEIGHT = 800

def startup():
    update_viewport(None, CONST_WINDOW_WIDTH, CONST_WINDOW_HEIGHT)
    glClearColor(0.5, 0.5, 0.5, 1.0)


def shutdown():
    pass


def render(time):
    glClear(GL_COLOR_BUFFER_BIT)

    drawMulticolorTriangle()  
    drawRect(0.0, 0.0, 100, 100)  

    glFlush()

def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-100.0, 100.0, -100.0 / aspect_ratio, 100.0 / aspect_ratio,
                1.0, -1.0)
    else:
        glOrtho(-100.0 * aspect_ratio, 100.0 * aspect_ratio, -100.0, 100.0,
                1.0, -1.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawRect(x, y, width, height):
    width = width / 2
    height = height / 2

    top_left = (x - width, y + height)
    top_right = (x + width, y + height)
    bottom_left = (x - width, y - height)
    bottom_right = (x + width, y - height)

    glColor3ub(33, 113, 33)
    drawTriangle(top_left, bottom_left, bottom_right)

    glColor3ub(13, 33, 7)
    drawTriangle(top_left, bottom_right, top_right)


def drawTriangle(v1, v2, v3):
    glBegin(GL_TRIANGLES)
    
    glVertex2f(v1[0], v1[1])
    glVertex2f(v2[0], v2[1])
    glVertex2f(v3[0], v3[1])
    
    glEnd()
    

def drawMulticolorTriangle():
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 50.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-50.0, -50.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(50.0, -50.0)

    glEnd()

def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(CONST_WINDOW_WIDTH, CONST_WINDOW_HEIGHT, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()