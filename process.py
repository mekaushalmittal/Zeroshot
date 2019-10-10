# lines = []
# with open('fp2w_processed.csv') as fp:
#     line = fp.readline()
#     while line:
#         line = line.replace(",,", ",")
#         # line = line.replace(">", "")
#         # line = line.replace(" ", "")
#         # line = line.replace("\t", ",")
#         lines.append(line)
#         line = fp.readline()

# with open('fp2w_processed.csv', 'w') as f:
#     f.writelines(lines)
d = {}
with open('fp2w_processed.csv') as fp:
    line = fp.readline()
    while line:
        arr = line.strip().split(",")
        d[arr[0]] = arr[1]
        # print (arr[0])
        # print (d[arr[0]])
        line = fp.readline()

# l2 = []
with open("entity_p.vocab", "w") as fp1:
    with open("data/nocopy/entity.vocab") as fp:
        line = fp.readline().strip()
        while line:
            # print (line)
            if line in d:
                fp1.write(d[line])
                fp1.write("\n")
            else: 
                fp1.write("NULL")
                fp1.write("\n")
            line = fp.readline().strip()
