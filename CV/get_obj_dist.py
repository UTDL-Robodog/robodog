import math


def getStereoDistance(x1_a, y1_a, x2_a, y2_a, x1_b, y1_b, x2_b, y2_b):
    ''' 
    Returns the distance of an object seen by the cameras.
    The calculations are implementations of the algorithm presented in this paper: https://www.sciencedirect.com/science/article/pii/S2590005620300011#fd13
        
        Parameters: 
            x1 (int) : x coordinate of lower left corner of object bounding box.
            y1 (int) : y coordinate of lower left corner of object bounding box.
            x2 (int) : x coordinate of upper right corner of object bounding box.
            y2 (int) : y coordinate of upper right corner of object bounding box.
        
        Note: y coordinates are actually not used by this distance calculation algorithm
        Returns:
            distance (float) : Distance of object returned in the same units as A, the distance between the two cameras.
    '''
    
    # FIXED HARDWARE CONSTANTS
    OMEGA1, OMEGA2 = 1, 1           # view angles of each camera in DEGREES
    H1, H2 = 1000, 1000             # number of horizontal pixels on each camera
    A = 1                           # horizontal distance between the cameras 

    
    # LEFT CAMERA (A)
    centre_x_a = (x1_a + x2_a) / 2
    # centre_y_a = (y1_a + y2_a) / 2
    P1 = H1 - centre_x_a            # P1 = pixel distance from right side from left camera

    # RIGHT CAMERA (B)
    centre_x_b = (x1_b + x2_b) / 2
    # centre_y_b = (y1_b + y2_b) / 2
    P2 = centre_x_b                 # P2 = pixel distance from left side of right camera

    # Intermediate calculations for finding distance:
    beta1, beta2 = (180-OMEGA1)/2, (180-OMEGA2)/2
    num1 = P2 * (OMEGA2/H2) + beta2
    num2 = P1 * (OMEGA1/H1) + beta1

    distance = A * math.sin(math.radians(num1)) * math.sin(math.radians(num2)) \
                / math.sin(math.radians(180 - (num1 + num2)))
    
    return distance