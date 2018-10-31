init:
    image vignette none = "gui/slot_hover_background.png"

init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    g.button("akie")
    g.condition("persistent.akie_end")
    g.image("cg akie")

    g.button("clateau")
    g.condition("persistent.clateau_end")
    g.image("cg clateau")

    g.button("ran")
    g.condition("persistent.ran_end")
    g.image("cg ran")

    g.button("sei")
    g.condition("persistent.sei_end")
    g.image("cg sei")

    g.button("tsugumi")
    g.condition("persistent.tsugumi_end")
    g.image("cg tsugumi")

    g.button("yoshino")
    g.condition("persistent.yoshino_end")
    g.image("cg yoshino")

    # The transition used when switching images.
    g.transition = dissolve

    g.locked_button="vignette none"

# Step 3. The gallery screen we use.
screen gallery:

    # Ensure this replaces the main menu.
    tag menu

    style_prefix "gallerie"

    # The background.
    add "bg game_gui"

    use navigation

    # A grid of buttons.
    grid 3 3:

        xpos 500
        ypos 100

        xspacing 50
        yspacing 100

        # Call make_button to show a particular button.
        add g.make_button("akie", "images/gui/akie_vignette.png", xalign=0.5, yalign=0.5)
        add g.make_button("clateau", "images/gui/clateau_vignette.png", xalign=0.5, yalign=0.5)
        add g.make_button("ran", "images/gui/ran_vignette.png", xalign=0.5, yalign=0.5)

        add g.make_button("sei", "images/gui/sei_vignette.png", xalign=0.5, yalign=0.5)
        add g.make_button("tsugumi", "images/gui/tsugumi_vignette.png", xalign=0.5, yalign=0.5)
        add g.make_button("yoshino", "images/gui/yoshino_vignette.png", xalign=0.5, yalign=0.5)

        text ""
        text ""


        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
