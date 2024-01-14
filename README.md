# Bash Challenges -Solved By Arjun Rajesh
This repository contains answers of the Bash Challenge solved by Arjun Rajesh

## Answers of Challenges:
1.
(a) execute 'pwd' in the shell to display the path of your current directory(b) execute 'ls' in the shell to list out the contents of you current directory
(c) execute 'ls -a ' in the shell to list out the contents of your current directory including hidden files

2.
(a) To create a new directory named a, excute 'mkdir a' in the shell
(b) To move to the newly created directory a, execute 'cd a' in the shell
(c) To create a blank file named file1, type 'touch file1' in the shell
(d) To display the file type of file1, type file file1 in the shell
(e) To add line Hello World to file1 using command echo, type echo "Hello World" > file1 in the terminal and press enter.
(f) To display contents of file1, type cat file1 in the terminal and press enter.
(g) To display file type of file1 again, type file file1 in the terminal and press enter.

3.
(a) To stay in directory a, type cd a in the terminal and press enter.
(b) To create file file2 and add contents First Line Second Line Third Line using command cat, type cat > file2 in the terminal and press enter. Then type
first Line, press enter, type Second Line, press enter, type Third Line, and press Ctrl + D.
(c) To break display contents of file2 with lines reversed, type tac file2 in the terminal and press enter.

4.
(a) excute 'cd a' , then execute 'cat file1 file2 > file3' ,then 'cat file3'(b) excute 'file file3'

5.excute this in order
(a) mkdir -p a/b/c/{b,c}
(b) mkdir a/d
(c) cp -r a/d a/b/c/
(d) rm -r a/d
(e) cp file3 a/d/

6.
(a) cd a/d
(b) mv file3 file0
    mv file0 ../

7.
(a) cd ~
(b) touch a/b/c/d/test
(c) find a/b/c/d -name test

8.
(a) cd a
    man grep > grepman.txt
(b) grep FILE grepman.txt

9.
(a) cd a
(b) rm -r b
    rm file*

10.
(a) cd ~
    wget https://blog.bios.in/logo.png
(b) python3 -c "import requests; open('logo2.png', 'wb').write(requests.get('https://blog.bio5.in/logo.png').content)"
(c) identify -verbose logo.png

11.
(a)traceroute google.com
traceroute google.com
nslookup google.com
nslookup google.com

12.python3 -m http.server 8080

13.
(b)
 nmap -sS -sV -A 10.10.8.142

14.Do this in Netcat
	# On server terminal
	nc -l -p 1234
	nc -l -p 1234 > file.txt

	# On client terminal
	nc localhost 1234
	nc localhost 1234 < file_.txt
	cat file.txt

# Reversing challenges flags
1.





2.flag{thisistheflag1lG1lY}
flag{KnoW_YouR_A5C115}




# arjunr24-su
