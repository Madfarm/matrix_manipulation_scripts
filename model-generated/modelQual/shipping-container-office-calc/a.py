def check_container_fit(room_dims, container_dims, door_dims):
    assert len(room_dims) == 3, "room_dims should have 3 values"
    assert len(container_dims) == 3, "container_dims should have 3 values"
    assert len(door_dims) == 2, "door_dims should have 2 values"

    # Check if container can fit through doorway
    if container_dims[0] > door_dims[0] or container_dims[1] > door_dims[1]:
        return False

    # Check if container can fit in room
    if container_dims[0] > room_dims[0] or container_dims[1] > room_dims[1] or container_dims[2] > room_dims[2]:
        return False

    return True

# Test the function
room_dims = [15.5, 200, 600]
container_dims = [8.5, 8.9, 40]
door_dims = [15, 12]

print(check_container_fit(room_dims, container_dims, door_dims))