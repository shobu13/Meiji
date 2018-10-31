init python:

    # Step 1. Create the gallery object.
    g = Gallery()

    # Step 2. Add buttons and images to the gallery.

    # This button has a condition associated with it, allowing the game
    # to choose which images unlock.
    g.button("end1")
    g.condition("persistent.unlock_1")
    g.image("bad_ending")

    # The transition used when switching images.
    g.transition = dissolve

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
        add g.make_button("end1", "gui/slot_hover_background.png", xalign=0.5, yalign=0.5)
        add g.make_button("end1", "gui/slot_hover_background.png", xalign=0.5, yalign=0.5)
        add g.make_button("end1", "gui/slot_hover_background.png", xalign=0.5, yalign=0.5)

        add g.make_button("end1", "gui/slot_hover_background.png", xalign=0.5, yalign=0.5)
        add g.make_button("end1", "gui/slot_hover_background.png", xalign=0.5, yalign=0.5)
        add g.make_button("end1", "gui/slot_hover_background.png", xalign=0.5, yalign=0.5)

        text ""
        text ""


        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
        textbutton "Return" action Return() xalign 0.5 yalign 0.5
