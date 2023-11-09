from ikpy import chain
from ikpy import link

# Define your robotic arm's chain
my_chain = chain.Chain(links=[
    link.URDFLink(
      name="base",
      translation_vector=[0, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
    link.URDFLink(
      name="first_link",
      translation_vector=[0, 0, 0.5],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    # Add more links as per your robot configuration
], active_links_mask=[False, True])

# Define your target position
target_vector = [0.1, 0.1, 0.1]  # Desired position of the gripper relative to the base frame, which is at [0, 0, 0]
target_frame = np.eye(4) # 4x4 matrix for Rot, Pos and an extra dimension for homogeneous coordinates.
#do i need a line for defining the rotations of target frame? 
target_frame[:3, 3] = target_vector # Selects the first three elements of the fourth column of the target_frame matrix representing the position in space.

#
ik = my_chain.inverse_kinematics(target_frame) # Compute the inverse kinematics
