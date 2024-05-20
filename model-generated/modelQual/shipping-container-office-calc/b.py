def container_fits(room_dims, container_dims, door_dims):
    assert len(room_dims) == 3, "room_dims must contain exactly 3 values"
    assert len(container_dims) == 3, "container_dims must contain exactly 3 values"
    assert len(door_dims) == 2, "door_dims must contain exactly 2 values"

    # Check if the container can fit through the doorway
    if container_dims[0] > door_dims[0] or container_dims[1] > door_dims[1]:
        return False

    # Check if the container can fit in the room
    if container_dims[0] > room_dims[0] or container_dims[1] > room_dims[1] or container_dims[2] > room_dims[2]:
        return False

    return True

# Test the function with the given input
room_dims = [15.5, 200, 600]
container_dims = [8.5, 8.9, 40]
door_dims = [15, 12]

print(container_fits(room_dims, container_dims, door_dims))