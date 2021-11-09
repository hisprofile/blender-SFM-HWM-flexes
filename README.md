# blender-HWM-flexes
Hey all! I made a script that allows for the HWM flex controller data of a source .mdl file to be imported into blender! It's fast, and easy! And incredibly unproffesional!

# Instructions
Make sure you use blender 2.9X to do this! 3.0 does not fully work!

First of all, make sure you have Blender Source Tools (BST) installed before you do all this.

To start off, you have to decompile the model with crowbar. Once that's done, locate the .vta file within the decompiled files.

Open the vta_separator.py script in a text editor window in blender, then put in the vta file's directory in the variable "vta1". Run the script.

Next, import the .qc file using BST. Once done, open a new text in the text editor, and open the latest qc_flex_data_importer.py script. In qcfile, put the qc file's directory in between the quotation marks. To find the mesh data and key blocks to put them in "mdbloq" and "kbloq", just click the drop down arrow twice on the model that has the flexes.
![image](https://user-images.githubusercontent.com/41131633/140957442-ea0be96f-30e4-4b55-9975-c8f753986ec8.png)
The mesh data block has a triangle with a square at each vertext. Put it's name in "mdbloq". The key block has a cube (or a plane extruding) by its side. Put it's name in kbloq.

Once all is done, run the script, and you should now have HWM flexes on your model! ALMOST exactly like in sfm.

# Things to know, and tips and tricks
Again, this does not work in Blender 3.0, due to it having a different RNA UI structure.

When reopening the file, you will see a prompt warning you about my script. I mean, my script is pretty self explanitory and has like 400 lines of code, so just click "Allow execution". If it really worries you, feel free to look through many lines of code.

You may notice that the face looks different. This is due to some shape keys having expressions that are longer than 256 characters. To fix this, just set "expfix" to 1, and run the script. Everything will then go back to normal.

When using multiple models, there is likely a high chancer that the expressions will overlap each other. This is because of how my code is built, and I can't find a better way around it. To get over this, you have to open my script in a different text for every model you have. In the first one, type print(robottwat) at the bottom of the script. (i swear there is context for that) Open the console, then run it. If it for example prints "312", then for the script on the next model, go to line 50 and put robottwat to 313. (robottwat = 313). Do the same for the next model, and so on.

If your model uses a second qc file for it's HWM flex data, like Alaxe's HWM Skeleton, put the directory whatever qc file it uses in qcfile2, and put secqc to 1. HWM Skeleton uses sniper's qc file, but another model might user another qc file.

# You should be good to go!
Feel free to ask any questions you have, or an issue regarding the support of a file.
If you join my discord server, I'll be quicker to respond regarding any question you'll have.

# TO-DO
Tweak the vta separator. Vertices in the middle are moved with the right side of the face, because if moved with both, the shape key will be applied twice in the middle. I want to make it so that each sides moves it half the distance, but I don't know if I can do this yet. I won't give up though.
