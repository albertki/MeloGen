# MeloGen
MeloGen: A tool to inspire pop music melody composition via an application of genetic algorithms for informed melody generation

"MeloGen" Informed melody generator program
Written by: Albert Ki
5/1/2020

** Because a MIDI/MusixXML reader application is recommended to open/view music score file formats, MuseScore is highly recommended (free).
Link:
https://musescore.org/en/download

========================================================================
Instructions to run the program:
(Ensure meloGen.py, myMarkovChain.py, and __init__.py are in the same directory.)

>> python meloGen.py

# Then simply enter the appropriate key in response to the input prompts.

========================================================================

** OUTPUT:
The program will write the simplified chord-version of the original score file, the pre-GA melody score file, and the post-GA melody score file to your current directory.

** If you wish to see/hear the resulting output, please make sure that you have MuseScore downloaded, and respond accordingly when the prompt asks if you would like to view the results.

** If MuseScore prompts you with an error message stating the file is corrupted, click ignore. This is the result of an insignificant issue from the output program.

**INPUT:
Various example input files have been provided in the input_mxl folder.

**If you wish to test additional files downloaded online (ex. midiworld.com), you should ensure that the file does not contain any auxiliary or percussion instruments, or a melody line-the reason being that melody parts are sometimes "transposing instruments" that are in a different key and can negatively affect the generation. 
- If they do exist, please delete the part/instrument in the application (information on MuseScore.com on how to delete instruments from a music score), and then export the file as a .mxl (Compressed musicxml) file.

