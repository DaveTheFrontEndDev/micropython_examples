import math

def calculate_orientation(accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z, delta_time=0.01):
    """
    Calculate pitch, roll, and yaw from raw accelerometer and gyroscope data.
    
    :param accel_x: Raw accelerometer value along X-axis
    :param accel_y: Raw accelerometer value along Y-axis
    :param accel_z: Raw accelerometer value along Z-axis
    :param gyro_x: Raw gyroscope value along X-axis (degrees per second)
    :param gyro_y: Raw gyroscope value along Y-axis (degrees per second)
    :param gyro_z: Raw gyroscope value along Z-axis (degrees per second)
    :param delta_time: Time interval between measurements (in seconds)
    :return: Tuple of (pitch, roll, yaw) in degrees
    """
    # Convert raw accelerometer values to G-forces
    accel_x = accel_x / 16384.0  # Scale factor for ±2g range (adjust if different)
    accel_y = accel_y / 16384.0
    accel_z = accel_z / 16384.0

    # Calculate pitch and roll using accelerometer data
    pitch_acc = math.atan2(accel_y, math.sqrt(accel_x**2 + accel_z**2)) * 180 / math.pi
    roll_acc = math.atan2(-accel_x, accel_z) * 180 / math.pi

    # Convert raw gyroscope values to degrees per second
    gyro_x_deg = gyro_x / 131.0  # Scale factor for ±250 dps range (adjust if different)
    gyro_y_deg = gyro_y / 131.0
    gyro_z_deg = gyro_z / 131.0

    # Calculate yaw by integrating gyroscope z-axis rotation
    yaw = gyro_z_deg * delta_time  # Delta time is the time between consecutive readings

    # Return pitch, roll, and yaw
    return pitch_acc, roll_acc, yaw
