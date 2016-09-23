
##very tiny intro
The command line is a interface to your computer which you operate through text rather than through a graphical interface.   
Opening the command line means opening a 'shell' in which you can specify processes that your computer will execute.   
You can imagine every application you are using to run such processes underneath the hood. 

Don't worry about the rest.   
**Why do you want to use the command line:**  
  
* use your precious machine to its full potential
* Every device that runs a program, can be interfaced with through a command line 
* unavoidable once stepping beyond p5js (node, python, git/github, connected devices...)
* makes you look very cool 

[**SKIP TO FUN**](http://)

##terminal 101 

###how to think of it
start by thinking of the command line as like a geeky, text-based version of your Finder. It let's you navigate through your file system using unix commands. Later, you will use it to 'do' things with your files.  
**filenames/paths:** in your system, every file or folder is described through the path that leads to it from the systems 'root' (the directory on the lowest levels, that contains everything else). Paths look like this `/Users/username/Desktop/photo.jpg`.


###navigating basics
* *where am I?*  
`pwd` - **p**resent **w**orking **d**irectory ("directory" == "folder")  
* *what's here, where I am?*   
`ls` - **l**i**s**t  
* *go somewhere else!*  
`cd [path]` - **c**hange **d**irectory
	* good to know:   
1) the cd command can bring your *deeper* into the filesystem by specifyig a path, or you can *move backwards* using ".." (e.g. `cd ..`).  
2) Dragging a file or folder into the Terminal will write the path to it. Trick: type 'cd ', drag a folder into the terminal, hit enter. Or drag folder into Terminal application symbol.

###file handling basics
#####make
* *make a new file!*  
`touch [filename]`  
* *make a directory!*  
`makedir [folder name]`  

#####move / rename
* *move a file!*  
`mv [path to file] [path to new location]`    
* *move a folder!*    
`mv -r [path to folder] [path to new location]` - "-r" is a flag and stands for 'recursive' (to move also files in folder in folder in folder that you specified).  
	* good to know:   
the mv command is also used to rename files or directories. Just include the new name in the second argument.  
  
#####copy
  
* *copy a file!*  
`cp [path to file] [path to new location]`  
* *copy a folder!*  
`cp -r [path to folder] [path to new location]`    
  
#####remove

* *remove a file or folder!*   
`rm [-r] [filename/foldername]`

###do things with files

####basics:
* *open file/folder with default application!*  
`open [file/folder]` - for folders, the default Finder -> type `open .` to open current directory.  
* *print file content to the terminal!*  
`cat [filename]`
  
  
##Advanced
* `|` - the pipe symbol lets you pipe the output of one command into another command.  
   
* `grep` - lets your filter a text for keywords  
	* **e.g.** `cat yesterday_lyrics.txt | grep yesterday` prints out all the lines that contain the word "yesteday".  
  
* ``&&`` - chains commands. ""run this first, then this".  
	* **e.g.** `mkdir website && cd website && touch index.html`   
  
* `clear` or `cmd + k` clears the command line.  
 
* `echo [anything]` - echoes anything  
  
* `>` - pipes output into a file. `>` overwrites, `>>` appends.  
	* **e.g.** `echo <h1>Welcome to my page</h1> > index.html`

* `curl [url]` - prints the html (or other text) from any url.  
	* **e.g.** `curl http://www.nytimes.com/ > nytimes_page_copy.html`  
  
* `which [command/exceutive/program]` - shows path to that program on your disk.   
	* **e.g.** `which cd` returns something like `/usr/bin/cd` and then `open /usr/bin` shows where most the commands you are using on your command line are located.

* `find directory` - lists ALL files/paths *behind* specified directory.  
	* **e.g.** `find . | grep file_i_cant_find_anymore.txt` return the path of that file if it exsits somehwere behind the current directory.   
	
* `sudo nano [filename]` - opens a fairly intuitive text editor in the command line for quick file editing.

##Fun Stuff

* `say [anything]` - makes your command line speal
* `cal [optional: year etc.]` - shows you a calendar
* **./.bash_profile** - a file for shortcuts and modifications of Terminal functionality
	* `sudo nano ~/.bash_profile` (FYI bash is a own language)
	* change your Terminal selector: `PS1="◉ [\W]:"`
	* make alias:
		* alias weather='curl -4 wttr.in'
		* alias cl='clear'
		* function cdl { cd $1; ls;}
		* alias github='cdl ~/Developer/1_github'
		* alias smile="for i in {1..20000};  do  printf '😊 '; done;"
	* after making changes in .bash_profile, save and run `source ~/.bash_profile` to make changes take effect.
	* [https://asciinema.org/](https://asciinema.org/)
	* watch star wars: `telnet towel.blinkenlights.nl`	
	* [some people get real serious with this](https://natelandau.com/my-mac-osx-bash_profile/) (disclaimer: I didn't read through this link actually)
	

##Useful Knowledge

###"/" and "~"
you know "/" as the sperator between locations in a path. It also represents the root. `cd /` will take you to the root of your file systems.  
"~" represents the *root* of your current user. 
   
###The `sudo` thing
You can make a real mess out of a computer from the command line. That's why some commands can not just be executed, but require to be "done" in "super user" mode (`sudo` = super user do).   
After `sudo [command]` you will need to provide your computer's password (confusig at first, while typing it, you will not see anything like *****, just type it and enter).  
`cd ~ && pwd` returns something like `/Users/username`

###*close* things
you will find yourself \*trapped\* inside programs within the command line (like "vim" text editor).  
Here are some common ways to exit:  

* `q`  
* `ctrl + d`  
* `ctrl + c`   
* `exit`   
* just close window  
* `[esc] :q!` - when you are lost in vim suddenly



###THREE *TRICKS* YOU WILL USE A LOT

####tab (button that looks like `->|`)
hitting tab halfway through a command or path, will autocomplete. 

####up arrow
let's you use commands you previously typed.

####`man` command
...stands for "manual" and typing `man [any command]` will open a description of how to use the command and what it does for you. Almost all commands have flags they can be used with to modify what they do.  
Navigate the instruction page with scroll or enter, exit is by hitting `q`. 



