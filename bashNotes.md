**BASH**


touch foo.sh

chmod +x !$  !$ is the last argument of the last command i.e. foo.sh

*Navigating Directories*


| pwd   | Print current directory path|

| ls | List directories |
|ls -a|--all               |# List directoRIES including hidden


|ls -l                     |# List directories in long form
|ls -l -h|--human-readable |# List directories in long form with human readable sizes
|ls -t                     |# List directories by modification time, newest first
|stat foo.txt              |# List size, created and modified timestamps for a file
|stat foo                  |# List size, created and modified timestamps for a directory
|tree                      |# List directory and file tree
|tree -a                   |# List directory and file tree including hidden
|tree -d                   |# List directory tree
|cd foo                    |# Go to foo sub-directory
|cd                        |# Go to home directory
|cd ~                      |# Go to home directory
|cd -                      |# Go to last directory
|pushd foo                 |# Go to foo sub-directory and add previous directory to stack
|popd                      |# Go back to directory 

*Creating Directories*

|mkdir foo                        | # Create a directory
|mkdir foo bar                    |# Create multiple directories
|mkdir -p|--parents foo/bar       |# Create nested directory
|mkdir -p|--parents {foo,bar}/baz |# Create multiple nested directories
|mktemp -d|--directory            |# Create a temporary directory

echo hello world.. Echo is a command and Hello world is an argument, so its for displaying .. Think of it as print "Hello world"

VIM- is a text editor
creating a new file .. vim textfile.txt vim shelltest.sh
and to check the files created you use ls(list)
cat is for displayin
:q is to ignore changes
exit with !wq


ppwd: print working directory - to check that we are in that working directory

First_Name= Letho
echo Hello $First_Name... its going to print "hello Letho"

You create a file like : vim hellothere.sh bese you press u I which means insect( as in you are putting stuff
ku file yakho) then after you #!/bin/bash
then you define your First_name = Letho
Last_name = Mntungwa.. then uthi echo Hello $First_name & Last_Name then exit with wq
then chmod u+x hellothere.sh and run it like ./hellothere.sh.. you will output Hello Letho Mntungwa

to prompt use "read" 

pippping

ls -l/usr/bin | grep bash (this is for filtering)
```js
> greater symbol overwrites the existing file
>> doesnt overwrite

WC -w hello.txt .. 6 hello.txt .. stands for word count

 Else if statement:
 if [${1,,} = herbet], then
   echo "Oh, you are the boss here . welcome!"
 elif [${1,,}= help], then 
   echo "Just enter your username"
else 
   echo "I dont know who you are. But you are ot the boss"
fi           
```

so basicaly, you first create a script/file, like  something.sh
then type in the shebang, uvule the lines, like write something in that script.. then you run it with chmod u+x something.sh


Arrays
My_first_list =(one two three four five)
if i want to print out the array.. echo ${My_first_list[@A]}