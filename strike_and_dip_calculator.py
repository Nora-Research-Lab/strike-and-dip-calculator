import numpy as np

def calculate_strike_and_dip(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    """
    Calculate strike and dip from three points in 3D space.
    
    Args:
        x1, y1, z1: coordinates of point A
        x2, y2, z2: coordinates of point B
        x3, y3, z3: coordinates of point C
    
    Returns:
        dict containing:
            - strike_azimuth: strike direction in degrees (0-180)
            - strike_compass: strike direction as compass quadrant (e.g., N45E)
            - dip_direction_azimuth: dip direction in degrees (0-360)
            - dip_direction_compass: dip direction as compass quadrant
            - dip_angle: dip angle in degrees (0-90)
            - plane_coeffs: coefficients (a, b, c, d) for plane equation ax+by+cz+d=0
    """
    # Convert points to numpy arrays
    p1 = np.array([x1, y1, z1])
    p2 = np.array([x2, y2, z2])
    p3 = np.array([x3, y3, z3])
    
    # Calculate vectors
    v1 = p2 - p1
    v2 = p3 - p1
    
    # Calculate normal vector (cross product)
    normal = np.cross(v1, v2)
    a, b, c = normal
    
    # Check if points are collinear
    if np.allclose(normal, [0, 0, 0]):
        raise ValueError("Points are collinear – cannot define a plane")
    
    # Calculate dip angle (in radians, then convert to degrees)
    dip_radians = np.arctan(np.sqrt(a**2 + b**2) / abs(c))
    dip_angle = np.degrees(dip_radians)
    
    # Calculate dip direction azimuth (in radians, then convert to degrees)
    dip_direction_radians = np.arctan2(b, a)
    dip_direction_degrees = np.degrees(dip_direction_radians)
    
    # Normalize dip direction to 0-360 range
    dip_direction_degrees = dip_direction_degrees % 360
    
    # Calculate strike (dip direction + 90 degrees)
    strike_degrees = (dip_direction_degrees + 90) % 360
    
    # Ensure strike is in range [0, 180)
    if strike_degrees >= 180:
        strike_degrees -= 180
    
    # Calculate plane equation coefficients: ax + by + cz + d = 0
    d = -(a*p1[0] + b*p1[1] + c*p1[2])
    
    # Convert strike and dip directions to compass quadrants
    strike_compass = _convert_to_compass_quadrant(strike_degrees)
    dip_direction_compass = _convert_to_compass_quadrant(dip_direction_degrees)
    
    return {
        'strike_azimuth': strike_degrees,
        'strike_compass': strike_compass,
        'dip_direction_azimuth': dip_direction_degrees,
        'dip_direction_compass': dip_direction_compass,
        'dip_angle': dip_angle,
        'plane_coeffs': (a, b, c, d)
    }

def _convert_to_compass_quadrant(angle_degrees):
    """
    Convert an azimuth angle (0-360) to a compass quadrant notation (e.g., N45E).
    
    Args:
        angle_degrees: angle in degrees (0-360)
    
    Returns:
        Compass quadrant string (e.g., N45E, S23W, etc.)
    """
    # Normalize angle to 0-360 range
    angle = angle_degrees % 360
    
    if 0 <= angle < 90:  # NE quadrant
        bearing = angle
        return f"N{bearing:.0f}E"
    elif 90 <= angle < 180:  # SE quadrant
        bearing = 180 - angle
        return f"S{bearing:.0f}E"
    elif 180 <= angle < 270:  # SW quadrant
        bearing = angle - 180
        return f"S{bearing:.0f}W"
    else:  # NW quadrant
        bearing = 360 - angle
        return f"N{bearing:.0f}W"
