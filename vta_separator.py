##### VTA TABBER/OPTIMIZER #####
vta1 = r"PUT VTA DIRECTORY HERE (KEEP QUOTATION MARKS)"
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
                        print(liness[m])
                        new.write("end")
                        f.close()
                        new.close()
                        breaking = 1
                        break
                    new.write(liness[m])
                    m += 1
                    continue
            if "  " in liness[m] and "+" in liness[m]:
                #print("true!")
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
                        if float(vertex_list[1]) > float(0.0):
                            new.write(liness[m])
                            m += 1
                            continue
                        #if float(vertex_list[1]) == float(0.0):
                            #new.write("\t" + vertex_list[0] + " " + vertex_list[1] + " " + str(float(vertex_list[2])/1) + " " +str(float(vertex_list[3])/1) + " " + str(float(vertex_list[4])/8) + " " + str(float(vertex_list[5])/8) + " " + str(float(vertex_list[6])/8) + "\n")
                            #print(vertex_list)
                            #time.sleep(0.05)
                            #m += 1
                            #continue
                        #x = input()
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
                        try:
                            if float(vertex_list[1]) < float(0.0):
                                new.write(liness[m])
                                m += 1
                                continue
                            if float(vertex_list[1]) == float(0.0):
                                new.write("\t" + vertex_list[0] + " " + vertex_list[1] + " " + str(float(vertex_list[2])/1) + " " +str(float(vertex_list[3])/1) + " " + str(float(vertex_list[4])/8) + " " + str(float(vertex_list[5])/8) + " " + str(float(vertex_list[6])/8) + "\n")
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