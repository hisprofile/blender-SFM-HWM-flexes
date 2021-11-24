"""
Check me out at:
@his.animations
youtube.com/c/hisanimations
"""
##### QC FILE IMPORTER ######################################
import bpy
properties = []
context = bpy.context
obj = context.object
import time
##### FILE INPUTS #####
qcfile = r"PUT QC FILE DIRECTORY HERE (KEEP QUOTATION MARKS)"

'''READ THIS: I have removed the need of manually typing in
the names of the mesh-data block and the key block.
It is now automatically retrieved.'''

mdbloq = obj.data.name
kbloq = obj.data.shape_keys.name

qcfile2 = r"PUT 2ND QC FILE DIRECTORY HERE (KEEP QUOTATION MARKS)"
#PUT THIS TO 1 IF USING A 2ND QC FILE
secqc = 0
#######################
##### FLEX CONTROLLER RESET (DO NOT PUT TO 1 THE FIRST TIME, BUT AFTER SCRIPT HAS BEEN USED) #####
expfix = 0
#####
import string
alpha = string.ascii_lowercase
name = qcfile.rfind(r"\""[:-1]) + 1
name_end = qcfile.rfind(".")
extra_sliders = open(qcfile[:qcfile.rfind(r"\""[:-1])] + r"\""[:-1] + f"extra_{qcfile[name:name_end]}_expressions.txt", "w+")
if not obj.data.get('_RNA_UI'):
    obj.data['_RNA_UI'] = {}
propin = []
propident = 1
sortprop = {}
crntline = []
enabled = 0
extraexp = []
noexptemp = 0
leca = 1
luca = 1
efunca = ""
lecexpd = {}
inprop = []
dexp = ""
lecc = []
breaking = 0
counter = 0
normalline = ""
switch = 0
robottwat = 0
switch2 = 0
act_key = bpy.context.object
act_key.active_shape_key_index = 1
skey_range = list(range(0, len(bpy.data.shape_keys[kbloq].key_blocks) - 1))
sind = 0
percent = 0
sk_list = []
sk_NF = []
sk_NF_ind = []
progress = 0
checker = []
flexfile = 0
skipper = []
whyalaxe = []
qc = open(qcfile, "r")
global rrline
rrline = []
for line in qc:
    line = line.replace("\t","")
    breaking = 0
    if line.startswith("flexcontroller"):
        crntline = line.split(" ")
        switch3 = 0
        switch2 = 0
        switch = 0
        try:
            float(crntline[3])
        except:
            qqfind = line.find('"') + 1
            qqrfind = line.rfind('"')
            why = line[qqfind:qqrfind]
            if why not in whyalaxe:
                whyalaxe.append(why)
            rrline = []
            normalline = ""
            for a in crntline:
                if str(a) == "1":
                    normalline += " 1"
                    rrline = []
                    rrline = normalline.split(" ")
                    normalline += f' "{rrline[1]}"'
                    rrline.append("1")
                    rrline.append(f'"{rrline[1]}"\n')
                    breaking = 1
                    switch3 = 1
                    crntline = normalline.split(" ")
                    break
                elif a == "flexcontroller":
                    normalline += "flexcontroller "
                    switch2 = 1
                    continue
                elif a == "range" or switch == 1:
                    normalline += " " + a
                    switch = 1
                    continue
                elif switch2 == 1:
                    normalline += a
                    switch2 = 0
                    continue
                else:
                    normalline += "_" + str(a)
                    continue
            crntline = normalline.split(" ")
        if switch3 == 1:
            line = normalline
        qfind = line.find('"')
        qrfind = line.rfind('"') + 1
        propname = line[qfind + 1:qrfind - 1]
        if "-" in propname:
            whyalaxe.append(propname)
            propname = propname.replace("-", "_")
        if not propname in checker:
            checker.append(propname)
        else:
            continue
        bba = str(propident/1000)[2:]
        if len(bba) < 3:
            if len(bba) == 2:
                bba += "0"
            if len(bba) == 1:
                bba += "00"
        f = alpha[int(bba[0])]
        s = alpha[int(bba[1])]
        t = alpha[int(bba[2])]
        xd = {f'{propname}': f'{f}{s}{t}_{propname}'}
        sortprop.update(xd)
        properties.append(propname)
        if expfix == 0:
            obj.data[xd[propname]] = 0.0
            obj.data['_RNA_UI'][xd[propname]] = {"description":xd[propname],
                      "default": 0.0,
                      "min":float(crntline[3]),
                      "max":float(crntline[4]),
                      "soft_min":float(crntline[3]),
                      "soft_max":float(crntline[4]),
                    "is_overridable_library":0,
                    }
        propident += 1
qc.close()
flexfile = 0
if secqc == 1:
    qc = open(qcfile2, "r")
    for line in qc:
        line = line.replace("\t","")
        breaking = 0
        if line.startswith("flexcontroller"):
            crntline = line.split(" ")
            switch3 = 0
            switch2 = 0
            switch = 0
            qfind = line.find('"')
            qrfind = line.rfind('"') + 1
            propname = line[qfind + 1:qrfind - 1]
            if propname not in sortprop:
                try:
                    float(crntline[3])
                except:
                    qqfind = line.find('"') + 1
                    qqrfind = line.rfind('"')
                    why = line[qqfind:qqrfind]
                    if why not in whyalaxe:
                        whyalaxe.append(why)
                    rrline = []
                    normalline = ""
                    for a in crntline:
                        if str(a) == "1":
                            normalline += " 1"
                            rrline = []
                            rrline = normalline.split(" ")
                            normalline += f' "{rrline[1]}"'
                            rrline.append("1")
                            rrline.append(f'"{rrline[1]}"\n')
                            breaking = 1
                            switch3 = 1
                            crntline = normalline.split(" ")
                            break
                        elif a == "flexcontroller":
                            normalline += "flexcontroller "
                            switch2 = 1
                            continue
                        elif a == "range" or switch == 1:
                            normalline += " " + a
                            switch = 1
                            continue
                        elif switch2 == 1:
                            normalline += a
                            switch2 = 0
                            continue
                        else:
                            normalline += "_" + str(a)
                            continue
                    crntline = normalline.split(" ")
                if breaking == 1:
                    continue
                if "-" in propname:
                    whyalaxe.append(propname)
                    propname = propname.replace("-", "_")
                if not propname in checker:
                    checker.append(propname)
                else:
                    continue
                bba = str(propident/1000)[2:]
                if len(bba) < 3:
                    if len(bba) == 2:
                        bba += "0"
                    if len(bba) == 1:
                        bba += "00"
                f = alpha[int(bba[0])]
                s = alpha[int(bba[1])]
                t = alpha[int(bba[2])]
                xd = {f'{propname}': f'{f}{s}{t}_{propname}'}
                sortprop.update(xd)
                properties.append(propname)
                if expfix == 0:
                    obj.data[xd[propname]] = 0.0
                    obj.data['_RNA_UI'][xd[propname]] = {"description":xd[propname],
                              "default": 0.0,
                              "min":float(crntline[3]),
                              "max":float(crntline[4]),
                              "soft_min":float(crntline[3]),
                              "soft_max":float(crntline[4]),
                            "is_overridable_library":0,
                            }
                propident += 1
qc.close()
for i in skey_range:
    sind += 1
    propind = 0
    drivvar = 0
    propin = []
    percent = 0
    qc = open(qcfile, "r")
    for line in qc:
        counter = 0
        nodef = 1
        drivvar = 0
        del propin
        propin = []
        line = line.replace("\t","").replace("\n", "")
        rline = line
        if line.startswith("%"):
            percent = 1
            for i in whyalaxe:
                if i in line:
                    rlinetemp = rline[:rline.find("=")]
                    linetemp = line[:line.find("=")]
                    rlinetemp2 = rline[rline.find("="):]
                    linetemp2 = line[line.find("="):]
                    if "-" in i:
                        linetemp2 = linetemp2.replace(i, i.replace("-", "_"))
                        rlinetemp2 = rlinetemp2.replace(i, i.replace("-", "_"))
                    else:
                        linetemp2 = linetemp2.replace(i, i.replace(" ", "_"))
                        rlinetemp2 = rlinetemp2.replace(i, i.replace(" ", "_"))
                    line = linetemp + linetemp2
                    rline = rlinetemp + rlinetemp2
            line_split = line.replace("%", "")
            line_split = line_split.split(" ")
            if line_split[0] == bpy.context.object.active_shape_key.name:
                if secqc == 1:
                    skipper.append(line_split[0])
                if bpy.context.object.active_shape_key.name not in sk_list:
                    sk_list.append(bpy.context.object.active_shape_key.name)
                for a in properties:
                    if a in line[line.find("("):] and a not in propin:
                        nodef = 0
                        propin.append(a)
                    counter += 1
                for a in propin:
                    if expfix == 0:
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables.new()
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].name = sortprop[a]
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].targets[0].id_type = "MESH"
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].targets[0].id = bpy.data.meshes[mdbloq]
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].targets[0].data_path = f'["{sortprop[a]}"]'
                        if drivvar + 1 == len(propin):
                            break
                        drivvar += 1
            percent = 1
            line_split = line.replace("%", "")
            line_split = line_split.split(" ")
            if line_split[0] not in inprop:
                inprop.append(line_split[0])
            if line_split[0] == bpy.context.object.active_shape_key.name:
                begin = line.find("(")
                end = line.rfind(")")
                lineexp = line[begin: end + 1]
                rlineexp = line[begin: end + 1]
                lineexp = lineexp.replace(" ","")
                for i in properties:
                    if i in lineexp:
                        lineexp = lineexp.replace(f'{i}',f'{sortprop[i]}')
                if len(lineexp) >= 256:
                    efunca = ""
                    dexp = ""
                    luca = 1
                    leca = 0
                    lecc = []
                    lecexpd = {}
                    expfunc = lineexp
                    for i in sortprop:
                        i = sortprop[i]
                        if i in lineexp:
                            if i not in list(lecc):
                                d = {f"{i}" : lineexp.find(i)}
                                lecexpd.update(d)
                                leca += 1
                    lecexpd = dict(sorted(lecexpd.items(), key=lambda item: item[1]))
                    for i in lecexpd:
                        lecc.append(i)
                        expfunc = expfunc.replace(i,f"var{luca}")
                        efunca += f"var{luca}, "
                        dexp += f"{i}, "
                        luca += 1
                    dexp = dexp[:-2]
                    efunca = efunca[:-2]
                    exec(f"def {mdbloq[:4]}exp{robottwat}({efunca}):\n\treturn {expfunc}")
                    exec(f'bpy.app.driver_namespace["{mdbloq[:4]}exp{robottwat}"] = {mdbloq[:4]}exp{robottwat}')
                    bpy.context.object.active_shape_key.driver_add("value").driver.expression = f'{mdbloq[:4]}exp{robottwat}({dexp})'
                    robottwat += 1
                    break
                else:
                    if expfix == 0 and "(" in rline:
                        bpy.context.object.active_shape_key.driver_add("value").driver.expression = lineexp
                        break
                if not "(" in rline:
                    if expfix == 0:
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables.new()
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].name = sortprop[line_split[2]]
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].id_type = "MESH"
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].id = bpy.data.meshes[mdbloq]
                        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].data_path = f'["{sortprop[line_split[2]]}"]' 
                    if expfix == 0:
                        bpy.context.object.active_shape_key.driver_add("value").driver.expression = sortprop[line_split[2]]
                        break
        if not line.startswith("%") and percent == 1 and expfix == 0:
            bpy.context.object.active_shape_key.driver_remove("value")
            sk_NF.append(bpy.context.object.active_shape_key.name)
            sk_NF_ind.append(act_key.active_shape_key_index)
            qc.close()
            qc
            break
    if act_key.active_shape_key.name.endswith("R"):
        act_key.active_shape_key.vertex_group = "blendright"
    if act_key.active_shape_key.name.endswith("L"):
        act_key.active_shape_key.vertex_group = "blendleft"
    if progress == 7:
        print(str((act_key.active_shape_key_index / len(bpy.data.shape_keys[kbloq].key_blocks))*100)[:4] + "% done with first QC file")
        progress = 0
        act_key.active_shape_key_index += 1
        continue
    progress += 1
    act_key.active_shape_key_index += 1
qc.close()
print("Finished parsing first QC file!")
if secqc == 1:
    drivvar = 0
    name = qcfile2.rfind(r"\""[:-1]) + 1
    name_end = qcfile2.rfind(".")
    if not obj.data.get('_RNA_UI'):
        obj.data['_RNA_UI'] = {}
    crntline = []
    extraexp = []
    noexptemp = 0
    leca = 1
    luca = 1
    efunca = ""
    lecexpd = {}
    dexp = ""
    lecc = []
    breaking = 0
    counter = 0
    normalline = ""
    switch = 0
    switch2 = 0
    act_key = bpy.context.object
    act_key.active_shape_key_index = 1
    skey_range = list(range(0, len(bpy.data.shape_keys[kbloq].key_blocks) - 1))
    sind = 0
    percent = 0
    qc = open(qcfile2, "r")
    rrline = []
    for i in skey_range:
        sind += 1
        propind = 0
        drivvar = 0
        propin = []
        percent = 0
        qc = open(qcfile2, "r")
        for line in qc:
            counter = 0
            nodef = 1
            drivvar = 0
            del propin
            propin = []
            line = line.replace("\t","").replace("\n", "")
            rline = line
            if line.startswith("%"):
                percent = 1
                for i in whyalaxe:
                    if i in line:
                        rlinetemp = rline[:rline.find("=")]
                        linetemp = line[:line.find("=")]
                        rlinetemp2 = rline[rline.find("="):]
                        linetemp2 = line[line.find("="):]
                        if "-" in i:
                            linetemp2 = linetemp2.replace(i, i.replace("-", "_"))
                            rlinetemp2 = rlinetemp2.replace(i, i.replace("-", "_"))
                        else:
                            linetemp2 = linetemp2.replace(i, i.replace(" ", "_"))
                            rlinetemp2 = rlinetemp2.replace(i, i.replace(" ", "_"))
                        line = linetemp + linetemp2
                        rline = rlinetemp + rlinetemp2
                line_split = line.replace("%", "")
                line_split = line_split.split(" ")
                if line_split[0] == bpy.context.object.active_shape_key.name and not line_split[0] in skipper:
                    if bpy.context.object.active_shape_key.name:
                        sk_list.append(bpy.context.object.active_shape_key.name)
                    for a in properties:
                        if a in line[line.find("("):] and a not in propin:
                            nodef = 0
                            propin.append(a)
                        counter += 1
                    for a in propin:
                        if expfix == 0:
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables.new()
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].name = sortprop[a]
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].targets[0].id_type = "MESH"
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].targets[0].id = bpy.data.meshes[mdbloq]
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[drivvar].targets[0].data_path = f'["{sortprop[a]}"]'
                            if drivvar + 1 == len(propin):
                                break
                            drivvar += 1
                percent = 1
                line_split = line.replace("%", "")
                line_split = line_split.split(" ")
                if line_split[0] not in inprop:
                    inprop.append(line_split[0])
                if line_split[0] == bpy.context.object.active_shape_key.name:
                    begin = line.find("(")
                    end = line.rfind(")")
                    lineexp = line[begin: end + 1]
                    rlineexp = line[begin: end + 1]
                    lineexp = lineexp.replace(" ","")
                    for i in properties:
                        if i in lineexp:
                            lineexp = lineexp.replace(f'{i}',f'{sortprop[i]}')
                    if len(lineexp) >= 256:
                        efunca = ""
                        dexp = ""
                        luca = 1
                        leca = 0
                        lecc = []
                        lecexpd = {}
                        expfunc = lineexp
                        for i in sortprop:
                            i = sortprop[i]
                            if i in lineexp:
                                if i not in list(lecc):
                                    d = {f"{i}" : lineexp.find(i)}
                                    lecexpd.update(d)
                                    leca += 1
                        lecexpd = dict(sorted(lecexpd.items(), key=lambda item: item[1]))
                        for i in lecexpd:
                            lecc.append(i)
                            expfunc = expfunc.replace(i,f"var{luca}")
                            efunca += f"var{luca}, "
                            dexp += f"{i}, "
                            luca += 1
                        dexp = dexp[:-2]
                        efunca = efunca[:-2]
                        exec(f"def {mdbloq[:4]}exp{robottwat}({efunca}):\n\treturn {expfunc}")
                        exec(f'bpy.app.driver_namespace["{mdbloq[:4]}exp{robottwat}"] = {mdbloq[:4]}exp{robottwat}')
                        bpy.context.object.active_shape_key.driver_add("value").driver.expression = f'{mdbloq[:4]}exp{robottwat}({dexp})'
                        robottwat += 1
                        break
                    else:
                        if expfix == 0 and "(" in rline:
                            bpy.context.object.active_shape_key.driver_add("value").driver.expression = lineexp
                            break
                    if not "(" in rline:
                        if expfix == 0:
                            bpy.context.object.active_shape_key.driver_remove("value")
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables.new()
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].name = sortprop[line_split[2]]
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].id_type = "MESH"
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].id = bpy.data.meshes[mdbloq]
                            bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].data_path = f'["{sortprop[line_split[2]]}"]' 
                        if expfix == 0:
                            bpy.context.object.active_shape_key.driver_add("value").driver.expression = sortprop[line_split[2]]
                            break
            if not line.startswith("%") and percent == 1 and expfix == 0:
                bpy.context.object.active_shape_key.driver_remove("value")
                sk_NF.append(bpy.context.object.active_shape_key.name)
                sk_NF_ind.append(act_key.active_shape_key_index)
                qc.close()
                qc
                break
        if progress == 7:
            print(str((act_key.active_shape_key_index / len(bpy.data.shape_keys[kbloq].key_blocks))*100)[:4] + "% done with second QC file")
            progress = 0
            act_key.active_shape_key_index += 1
            continue
        progress += 1
        act_key.active_shape_key_index += 1
    qc.close()
extra_sliders.close()
print("Finished parsing second QC file!")
act_key.active_shape_key_index = 1
counter = 0
for i in sk_NF_ind:
    act_key.active_shape_key_index = i
    if expfix == 0:
        obj.data["NA_in_qc_" + sk_NF[counter]] = 0.0
        obj.data['_RNA_UI']["NA_in_qc_" + sk_NF[counter]] = {"description":f"NA_in_qc_{sk_NF[counter]}",
            "default": 0.0,
            "min":float(0.0),
            "max":float(1.0),
            "soft_min":float(0.0),
            "soft_max":float(1.0),
            "is_overridable_library":0,
        }
        bpy.context.object.active_shape_key.driver_add("value").driver.variables.new()
        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].name = f'NA_in_qc_{sk_NF[counter]}'
        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].id_type = "MESH"
        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].id = bpy.data.meshes[mdbloq]
        bpy.context.object.active_shape_key.driver_add("value").driver.variables[0].targets[0].data_path = f'["NA_in_qc_{sk_NF[counter]}"]'
    bpy.context.object.active_shape_key.driver_add("value").driver.expression = f"NA_in_qc_{sk_NF[counter]}"
    counter += 1
act_key.active_shape_key_index = 1