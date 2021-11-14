# blender-HWM-flexes
Hey all! I made a script that allows for the HWM flex controller data of a source .mdl file to be imported into blender! It's fast, and easy! And incredibly unproffesional!

# Instructions
Make sure you use blender 2.9X to do this! 3.0 does not fully work!

First of all, make sure you have Blender Source Tools (BST) installed before you do all this.

To start off, you have to decompile the model with crowbar. Once that's done, locate the .vta file within the decompiled files.

Open the vta_separator.py script in a text editor window in blender, then put in the vta file's directory in the variable "vta1". Run the script.

Next, import the .qc file using BST. Once done, open a new text in the text editor, and open the latest qc_flex_data_importer.py script. 
(alternatively, you could import the smd file first, then import the vta file to apply shape keys.)

In qcfile (line 13), put the qc file's directory in between the quotation marks. 

Once all is done, make sure you have the model selected, run the script, and you should now have HWM flexes on your model! ALMOST exactly like in sfm.

# Things to know, and tips and tricks
Again, this does not work in Blender 3.0, due to it having a different RNA UI structure.

When reopening the file, you will see a prompt warning you about my script. I mean, my script is pretty self explanitory and has like 400 lines of code, so just click "Allow execution". If it really worries you, feel free to look through many lines of code.

You may notice that the face looks different. This is due to some shape keys having expressions that are longer than 256 characters. To fix this, just set "expfix" to 1 (line 27), and run the script. Everything will then go back to normal.

If your model uses a second qc file for it's HWM flex data, like Alaxe's HWM Skeleton, put the directory of whatever qc file it uses in qcfile2 (line 22), and put secqc (line 24) to 1. HWM Skeleton uses sniper's qc file, but another model might user another qc file.

# You should be good to go!
Feel free to ask any questions you have, or an issue regarding the support of a file.
If you join my discord server, I'll be quicker to respond regarding any question you'll have.
https://discord.gg/t4EjF9q
