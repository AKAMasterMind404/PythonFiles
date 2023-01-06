from PIL import Image, ImageDraw, ImageChops
import random
import colorsys

from PIL.Image import Resampling


def random_color():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = tuple([int(x * 255) for x in float_rgb])

    return rgb


def interpolate(c1, c2, factor: float):
    reciprocal = 1 - factor
    return (
        int(c1[0] * reciprocal + c2[0] * factor),
        int(c1[1] * reciprocal + c2[1] * factor),
        int(c1[2] * reciprocal + c2[2] * factor),
    )


def generate_art():
    print("Generating art...")
    target_size = 256
    scale_factor = 1
    img_size = target_size * scale_factor
    padding = 16 *  scale_factor
    img_bg_color = (0, 0, 0)
    start_color = random_color()
    end_color = random_color()
    image = Image.new('RGB', (img_size, img_size), img_bg_color)

    points = []

    for _ in range(10):
        point = (random.randint(padding, img_size - padding), random.randint(padding, img_size - padding))
        points.append(point)

    thickness = 8 * scale_factor
    n_points = len(points) - 1

    for i, point in enumerate(points):
        overlay_image = Image.new("RGB", size=(img_size, img_size), color=img_bg_color)
        overlay_draw = ImageDraw.Draw(overlay_image)

        p1 = point
        p2 = points[0] if i == n_points else points[i + 1]

        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        overlay_draw.line((p1, p2), fill=line_color, width=thickness)
        image = ImageChops.add(image, overlay_image)

    image.resize((target_size, target_size), resample=Resampling.LANCZOS)
    image.show()


if __name__ == '__main__':
    for i in range(10):
        generate_art()
