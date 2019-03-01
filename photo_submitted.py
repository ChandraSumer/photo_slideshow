import sys

args = sys.argv
input_file = open(args[1], 'r')
output_file = open(args[2], 'w')

lines = int(input_file.readline())

horizontal_slides = {}
vertical_slides = {}
verticals = {}
transitions = []
tags = []

for i in range(lines):
    photo_data = input_file.readline().rstrip()
    photo_data_list = photo_data.split(' ')

    # separate horizontals
    if photo_data_list[0] == 'H':
        for j in range(int(photo_data_list[1])):
            tags.append(photo_data_list[j + 2])
        horizontal_slides[i] = tags

    # separate verticals
    if photo_data_list[0] == 'V':
        for j in range(int(photo_data_list[1])):
            tags.append(photo_data_list[j + 2])
        verticals[i] = tags
    tags = []


# create slides out of verticals
v_len = len(verticals)

if v_len == 2:
    v_ids = tuple(list(verticals.keys()))
    v_tags = list(set(verticals[1] + verticals[2]))
    vertical_slides[0] = {v_ids: v_tags}
# elif v_len > 2:
#     print(dict(horizontal_slides.items()[0:v_len/2]))
#     # verticals1 = dict(verticals.items()[:v_len/2])
#     # verticals2 = dict(verticals.items()[v_len/2:])
#     # for i, j in zip(verticals1, verticals2):
#     #     v_ids = tuple(i.keys(), j.keys())
#     #     v_tags = list(set(i.keys() + j.keys()))
#     #     vertical_slides[0] = {v_ids: v_tags}

horizontal_transitions = sorted(horizontal_slides.items(), key=lambda kv: kv[1])
vertical_transitions = sorted(vertical_slides.items(), key=lambda kv: kv[1])

# data for output
S = len(horizontal_transitions) + len(vertical_transitions) # no. of slides
output_file.write("{}\n".format(S))

for i in horizontal_transitions:
    output_file.write("{}\n".format(i[0]))

for i in vertical_transitions:
    # print(list(i[1].keys())[0][0])
    output_file.write("{} {}\n".format(list(i[1].keys())[0][0], list(i[1].keys())[0][1]))

output_file.close()
input_file.close()
