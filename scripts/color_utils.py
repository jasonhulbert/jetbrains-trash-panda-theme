import numpy as np
import colorspacious as cs

# Define the sRGB to XYZ transformation matrix
srgb_to_xyz_matrix = np.array([
    [0.4124564, 0.3575761, 0.1804375],
    [0.2126729, 0.7151522, 0.0721750],
    [0.0193339, 0.1191920, 0.9503041]
])

# Define the XYZ to P3 transformation matrix
xyz_to_p3_matrix = np.array([
    [2.493496911941425, -0.9313836179191239, -0.40271078445071684],
    [-0.8294889695615747, 1.7626640603183463, 0.023624685841943577],
    [0.03584583024378447, -0.07617238926804182, 0.9568845240076872]
])

def srgb_to_xyz(srgb):
    # Normalize sRGB values to the range [0, 1]
    srgb = np.array(srgb) / 255.0
    # Convert to XYZ using colorspacious
    xyz = cs.cspace_convert(srgb, "sRGB1", "XYZ100")

    # Normalize XYZ values to the range [0, 1]
    return xyz / 100.0

def xyz_to_p3(xyz):
    # Convert from XYZ to P3
    p3 = np.dot(xyz, xyz_to_p3_matrix.T)
    # Clip values to the range [0, 1]
    p3 = np.clip(p3, 0, 1)

    # Map to 17 point floating precision
    p3 = list(map(lambda x:f'{x:.17f}', p3))

    return p3

def srgb_to_p3(srgb):
    xyz = srgb_to_xyz(srgb)
    p3 = xyz_to_p3(xyz)

    return p3

def hex_to_srgb(hex_color):
    red = int(hex_color[0:2], 16) / 255.0
    green = int(hex_color[2:4], 16) / 255.0
    blue = int(hex_color[4:6], 16) / 255.0

    # Map to 17 point floating precision
    srgb = list([red, green, blue])

    return srgb
