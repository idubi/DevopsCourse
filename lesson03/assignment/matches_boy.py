from PIL import Image, ImageDraw


def draw_matches_boy(color="black"):
    # Create a new image with a white background
    image = Image.new("RGB", (300, 300), "white")
    draw = ImageDraw.Draw(image)

    # Draw the head
    head_radius = 50
    head_center = (150, 75)
    head_bbox = (
        head_center[0] - head_radius,
        head_center[1] - head_radius,
        head_center[0] + head_radius,
        head_center[1] + head_radius,
    )
    draw.ellipse(head_bbox, fill=color)

    # Draw the body
    body_start = (150, 125)
    body_end = (150, 250)
    draw.line([body_start, body_end], fill=color, width=5)

    # Draw the arms
    arm_length = 75
    arm_width = 5

    left_arm_start = (body_start[0] - arm_length, body_start[1] + arm_width)
    left_arm_end = (body_start[0], body_start[1] + arm_width)
    draw.line([left_arm_start, left_arm_end], fill=color, width=arm_width)

    right_arm_start = (body_start[0], body_start[1] + arm_width)
    right_arm_end = (body_start[0] + arm_length, body_start[1] + arm_width)
    draw.line([right_arm_start, right_arm_end], fill=color, width=arm_width)

    # Draw the legs
    leg_length = 100
    leg_width = 5

    left_leg_start = (body_end[0] - leg_width, body_end[1])
    left_leg_end = (body_end[0] - leg_width, body_end[1] + leg_length)
    draw.line([left_leg_start, left_leg_end], fill=color, width=leg_width)

    right_leg_start = (body_end[0] + leg_width, body_end[1])
    right_leg_end = (body_end[0] + leg_width, body_end[1] + leg_length)
    draw.line([right_leg_start, right_leg_end], fill=color, width=leg_width)

    # Save the image
    image.save("./stick_figure_man.png")
