from Logic import FlappyBird
from Logic import RubiksCube
from Logic import StandardMovement

FPS = 60
resolution = (800, 600)
debug = True
# normal, render, testing
mode = "normal"
scene_name = "barrel.rsc"
frame_count = 1000
mouse_control = False
mouse_sensitivity = 0.5

# Drawing settings
culling_coloring = False
frustum_culling = True
back_culling = True
lighting = True
homemade_rasterizer = True

def get_settings():
    return [FPS, resolution, debug, mode, scene_name, frame_count, mouse_control, mouse_sensitivity, 
            culling_coloring, frustum_culling, back_culling, lighting, homemade_rasterizer]

match scene_name:
    case "flappy_bird.rsc": GameFile = FlappyBird
    case "rubiks_cube.rsc": GameFile = RubiksCube
    case _:                 GameFile = StandardMovement
