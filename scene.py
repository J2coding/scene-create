# Import the functions from the Draw 2-D library
# so that they can be used in this program.

from os import scandir
from textwrap import fill
import turtle
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    #draw_sky(canvas,scene_width,scene_height)
    
    draw_ground(canvas,scene_width,scene_height)
    draw_sky(canvas,scene_width,scene_height)
    draw_cloud(canvas,300,400,200,90)
    draw_cloud(canvas,200,350,150,80)
    draw_cloud(canvas,250,300,140,60)
    draw_cloud(canvas,600,380,100,50)
    draw_sun(canvas,720,420,90,50)
    
    draw_pine_tree(canvas,550,150,250)
    draw_grid(canvas,scene_width,scene_height,50)

    #sun
    
    


        # Draw another pine tree.
    tree_center_x = 170
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height,)

        
        # Draw another pine tree.
    tree_center_x = 70
    tree_bottom = 50
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)


# Call the finish_drawing function
# in the draw2d.py library.
    finish_drawing(canvas)



# Define your functions such as
#draw_ground here.
def draw_sun(canvas,origin_x,origin_y,width,height):
    draw_oval(canvas,origin_x, origin_y,origin_x+width,origin_y+height, fill="yellow")
def draw_ground(canvas,scene_width,scene_height):
    draw_rectangle(canvas,0,0,scene_width,scene_height/.1
    ,width=0,fill="tan4")
# draw_sky 
def draw_sky(canvas,scene_width,scene_height):
    draw_rectangle(canvas, 0, scene_height / 2,
        scene_width, scene_height, width=0, fill="sky blue")
        
def draw_cloud(canvas,origin_x,origin_y,width,height):
    draw_oval(canvas,origin_x, origin_y,origin_x+width,origin_y+height, fill="white")
    
        

    
def draw_pine_tree(canvas,center_x, bottom, height):
    #draw the trunk
    trunk_width= height/10
    trunk_height = height/5
    left_trunk=center_x -trunk_width/2
    bottom_trunk = bottom
    right_truck = center_x +trunk_width/2
    trunk_top = bottom+trunk_height 

    draw_rectangle(canvas,left_trunk,bottom_trunk,right_truck,trunk_top,fill="tan4")

    skirt_width = height/2
    skirt_left = center_x-skirt_width/2
    skirt_bottom = trunk_top
    peak_x = center_x
    peak_y = bottom+ height
    skirt_right = center_x + skirt_width/2

    draw_polygon(canvas,skirt_left,skirt_bottom,peak_x,peak_y, skirt_right,skirt_bottom,fill="forestGreen")
    
    
def draw_grid(canvas,width,height,interval,fill="blue"):
    #draw a vertical line
    label_y =5
    for x in range(interval,width,interval):
        draw_line(canvas,x,5,x,height,fill="")
        draw_text(canvas,x,label_y,f"{x}",fill="")

#draw horizontal lines
    label_x =5
    for y in range(interval,height,interval):
        draw_line(canvas,5,y,width,y,fill="")
        draw_text(canvas,label_x,y,f"{x}",fill="")


# Call the main function so that
# this program will start executing.
main()