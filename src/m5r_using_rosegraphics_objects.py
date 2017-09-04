"""
This module uses ROSEGRAPHICS to demonstrate:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Andrew White.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
#
# DONE: 2.
#   RUN this program.  Then answer the following,
#     GETTING HELP AS NEED! (Ask questions!!!)
#
#     a. For the RoseGraphics coordinate system:
#
#        -- Where is the (0, 0) point on the screen?
#              The point (0,0) is located at the top-left of a rose window
#
#        -- In what direction on the screen does the positive X-axis point?
#              The positive x-axis points to the right of the screen
#
#        -- In what direction on the screen does the positive Y-axis point?
#              THe positive y-axis points to the bottom of the screen
#
#     b. Write a line of code that constructs a RoseGraphics object:
#            import rosegraphics as rg
#
#     c. What is the default height of a RoseWindow?
#        (Use the HOVER trick to determine the answer to this question.)
#            The default height of a RoseWindow is 300px
#
#     d. Write a line of code that construct a RoseWindow object
#        whose height is 100:  (Use the HOVER trick to figure it out)
#            window = rg.RoseWindow(400,100,'')
#
#     e. Use the DOT trick to answer the following:
#
#          -- Write the names of two types of graphics objects that
#             you can construct OTHER than Circle and Point:
#                You can additionally construct a line and an ellipse
#
#          -- Write the names of three METHODs that Circle objects have:
#                move_by() , move_center_to(), and attach_to()
#
#          -- Write the names of three INSTANCE VARIABLEs that Circle
#             objects have:
#                circle objects have an outline thickness, a center, and a fill_color
#
#     f. What does a RoseWindow RENDER method do?
#            The render methods updates and then draws all of the shapes attached to a RoseWindow
#            and then it pauses for a given number of seconds
#
#     g. When is a RoseWindow close_on_mouse_click method call
#        necessary?  Why?
#           A close_on_mouse_click call is necessary after the window renders because the window displays on the
#         screen after it renders and and a close_on_mouse_click is necessary to close it if need be.
#
#   ASK QUESTIONS ** NOW ** if you do not understand how the
#     RoseGraphics graphics system works.
#
#   When you are confident that you have written correct answers
#   to the above questions (ASK QUESTIONS AS NEEDED!),
#   change the above TO DO to DONE.
#
########################################################################

import rosegraphics as rg


def main():
    """
    Uses ROSEGRAPHICS to demonstrate:
      -- CONSTRUCTING objects,
      -- applying METHODS to them, and
      -- accessing their DATA via INSTANCE VARIABLES
    """
    circ = rg.Circle()
    example1()
    example2()
    example3()


def example1():
    """ Displays an empty window. """
    window = rg.RoseWindow(500, 300, 'Example 1: An empty window')
    window.render()
    window.close_on_mouse_click()


def example2():
    """ Displays two Point objects. """
    # ------------------------------------------------------------------
    # Construct the window in which objects will be drawn.
    # ------------------------------------------------------------------
    window = rg.RoseWindow()

    # ------------------------------------------------------------------
    # Construct some rg.Point objects.
    # Note: the y-axis goes DOWN from the TOP.
    # ------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)

    # ------------------------------------------------------------------
    # A RoseGraphics object is not associated with a window,
    # and hence are not drawn, until you ATTACH it to a window.
    # ------------------------------------------------------------------
    point1.attach_to(window)
    point2.attach_to(window)

    # ------------------------------------------------------------------
    # And they still are not DRAWN until you RENDER the window.
    # That will draw ALL the objects on the window.
    # This two-step approach is important for animation.
    # ------------------------------------------------------------------
    window.render()

    window.close_on_mouse_click()


def example3():
    """ Displays a Circle and a Rectangle. """
    # ------------------------------------------------------------------
    # RoseWindow: optionally takes its width and height.
    # ------------------------------------------------------------------
    width = 700
    height = 400
    window = rg.RoseWindow(width, height)

    # ------------------------------------------------------------------
    # Circle: needs its center and radius.
    # Has  fill_color  instance variable.
    # ------------------------------------------------------------------
    center_point = rg.Point(300, 100)
    radius = 50
    circle = rg.Circle(center_point, radius)
    circle.fill_color = 'green'
    circle.attach_to(window)

    # ------------------------------------------------------------------
    # Rectangle: needs two opposite corners.
    # ------------------------------------------------------------------
    point1 = rg.Point(100, 150)
    point2 = rg.Point(200, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)

    # ------------------------------------------------------------------
    # render: Draw ALL the objects attached to this window.
    # ------------------------------------------------------------------
    window.render()

    # ------------------------------------------------------------------
    # A Rectangle has instance variables  corner_1  and  corner2.
    # ------------------------------------------------------------------
    corner1 = rectangle.corner_1
    corner2 = rectangle.corner_2
    print(corner1, corner2)  # You can also PRINT RoseGraphics objects.
    print(rectangle)  # See the Console for the output.

    # ------------------------------------------------------------------
    # close_on_mouse_click: Keeps the window open until user clicks.
    # ------------------------------------------------------------------
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
