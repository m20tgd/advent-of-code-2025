import math

# filename = 'example.txt'
filename = 'input.txt'


def get_dist_between_points(a, b):
    [ax, ay, az] = a
    [bx, by, bz] = b
    return math.sqrt(
        (ax - bx) ** 2 +
        (ay - by) ** 2 +
        (az - bz) ** 2
    )


def is_box_in_circuit(box, circuits):
    for circuit in circuits:
        if circuit > set({box}):
            return circuit
    return None


j_boxes = []
with open(filename) as file:
    for line in file:
        [x, y, z] = line.split(',')
        j_boxes.append((int(x), int(y), int(z)))

distances = []
for i in range(len(j_boxes)):
    if i == len(j_boxes) - 1:
        break
    box_a = j_boxes[i]
    for j in range(i+1, len(j_boxes)):
        box_b = j_boxes[j]
        distance = get_dist_between_points(box_a, box_b)
        distances.append({"a": box_a, "b": box_b, "distance": distance})

distances = sorted(distances, key=lambda x: x["distance"])

circuits = []
i = 0
a_box = None
b_box = None
while len(circuits) != 1 or len(circuits[0]) < len(j_boxes):
    a_box = distances[i]["a"]
    b_box = distances[i]["b"]
    a_circuit = is_box_in_circuit(a_box, circuits)
    b_circuit = is_box_in_circuit(b_box, circuits)
    if a_circuit is None and b_circuit is None:
        circuits.append(set({a_box, b_box}))
    elif a_circuit is None:
        b_circuit.add(a_box)
    elif b_circuit is None:
        a_circuit.add(b_box)
    elif a_circuit is not b_circuit:
        circuits.append(a_circuit | b_circuit)
        circuits.remove(a_circuit)
        circuits.remove(b_circuit)
    i += 1

[ax, *_] = a_box
[bx, *_] = b_box
print(f"Answer: {ax * bx}")
