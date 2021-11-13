"""
hisprofile @ github
"""
##### VTA TABBER/OPTIMIZER #####
vta1 = r"PUT VTA FILE DIRECTORY HERE (KEEP QUOTATION MARKS)"
vtatab = vta1[:-4] + "_tab.vta"
vta = open(vta1, "r")
vta_tabbed = open(vtatab, "w+")
spacetotab = ""
for line in vta:
    if "    ":
        spacetotab = line.replace("    ","\t")
        vta_tabbed.write(spacetotab)
    else:
        vta_tabbed.write(line)
vta.close()
vta_tabbed.close()
##### VTA SEPARATOR #####
temp_frame = ""
temp_frame_e = ""
temp_frame_L = ""
temp_frame_R = ""
frame_list = []
vertex_list = []
vertex_split = []
vertex_tab = ""
vertex_dict = {}
frame_placeholder = 0
a = open(vtatab, "r")
liness = a.readlines()
a.close()
f = open(vtatab, "r")
new = open(vta1, "w+")
end = 0
n = 0
m = 0
c = 0
var5 = 0
switch = True
loccompare = {}
breaking = 0
for line in f:
    c += 1
    temp_frame = line.strip()
    if end == 0 and not temp_frame == "end":
        new.write(line)
        m += 1
        continue
    if line.strip() == "end":
        end += 1
        new.write(line)
        m += 1
        continue
    if end == 1:    
        if "+" in line.strip():
            temp_frame_e = temp_frame[2:].split(" ")
            temp_frame_e = temp_frame_e[3].split("+")
            temp_frame_L = temp_frame_e[0]
            temp_frame_R = temp_frame_e[1]
            new.write(f"{line[:6]} {n} # {temp_frame_L}\n")
            frame_list.append(f"{line[:6]} {n} # {temp_frame_L}\n")
            n += 1
            new.write(f"{line[:6]} {n} # {temp_frame_R}\n")
            frame_list.append(f"{line[:6]} {n} # {temp_frame_R}\n")
            n += 1
            m += 1
            continue
        else:
            if line.startswith("  "):
                temp_frame = temp_frame.split("# ")
                new.write(f"{line[:6]} {n} # {temp_frame[1]}\n")
                frame_list.append(f"{line[:6]} {n} # {temp_frame[1]}\n")
                n += 1
                m += 1
                continue
            else:
                new.write(line)
                m += 1
                continue
    if end == 2:
        while True:
            if not liness[m].startswith("  "):
                new.write(liness[m])
                m += 1
                continue
            if "  " in liness[m] and not "+" in liness[m]:
                new.write(frame_list[var5])
                frame_placeholder = m
                var5 += 1
                m += 1
                while True:
                    try:
                        if liness[m + 1].startswith("  "):
                            new.write(liness[m])
                            m += 1
                            break
                    except:
                        new.write("end")
                        f.close()
                        new.close()
                        breaking = 1
                        break
                    nullcheck = liness[m][1:-1].split(" ")
                    if (float(nullcheck[1]) >= float(-0.01) and float(nullcheck[1]) <= float(0.01)) and switch == True:
                        xd = {nullcheck[0] : f"{nullcheck[1]} {nullcheck[2]} {nullcheck[3]} {nullcheck[4]} {nullcheck[5]} {nullcheck[6]}"}
                        loccompare.update(xd)
                    new.write(liness[m])
                    m += 1
                    continue
                switch = False
            if "  " in liness[m] and "+" in liness[m]:
                for i in range(2):
                    new.write(frame_list[var5])
                    var5 += 1
                    m += 1
                    frame_placeholder = m
                    while True:
                        try:
                            if "  " in liness[m + 1]: 
                                m += 1
                                break
                        except:
                            breaking = 1
                            break
                        vertex_list = liness[m][1:].split(" ")
                        vl = vertex_list
                        if vl[0] in loccompare:
                            y = float(vl[2]) + ((float(loccompare[vl[0]].split(" ")[1]) - float(vl[2]))/2)
                            z = float(vl[3]) + ((float(loccompare[vl[0]].split(" ")[2]) - float(vl[3]))/2)
                            new.write(f"\t{vl[0]} 0.000000 {y} {z} {vl[4]} {vl[5]} {vl[6]}")
                            m += 1
                            continue
                        if float(vertex_list[1]) > float(0.01):
                            new.write(liness[m])
                            m += 1
                            continue
                        m += 1
                    new.write(frame_list[var5])
                    var5 += 1
                    m = frame_placeholder
                    while True:
                        try:
                            if "  " in liness[m + 1]:
                                m += 1
                                break
                        except:
                            pass
                        vertex_list = liness[m][1:].split(" ")
                        vl = vertex_list
                        try:
                            if vl[0] in loccompare:
                                y = float(vl[2]) + ((float(loccompare[vl[0]].split(" ")[1]) - float(vl[2]))/2)
                                z = float(vl[3]) + ((float(loccompare[vl[0]].split(" ")[2]) - float(vl[3]))/2)
                                new.write(f"\t{vl[0]} 0.000000 {y} {z} {vl[4]} {vl[5]} {vl[6]}")
                                m += 1
                                continue
                            if float(vertex_list[1]) < float(-0.01):
                                new.write(liness[m])
                                m += 1
                                continue
                        except:
                            break
                        m += 1
                    if breaking == 1:
                        break
                    break
            if breaking == 1:
                break
        if breaking == 1:
            break
    if breaking == 1:
        break
                    
            
    break
try:
    new.write("end")
except:
    pass
a.close()
f.close()
new.close()
