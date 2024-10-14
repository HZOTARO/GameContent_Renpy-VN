# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define MC = Character("Person", color="#E03BBB")


# The game starts here.

label start:
    scene bg home bedroom
    # show gerry smile at left:
    #     xzoom 1.0
    
    MC "Hello."
# menu:
#     "Hello":
#         jump yes
#     "...":
#         jump no
#     "...":
#         jump no

# label yes:
#     "Yes"
#     return

# label no:
#     "..."
#     "..."
#     return
