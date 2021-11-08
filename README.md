# Errory
## Tired of executing testcases one by one for your assignment🤨 Here's a solution for that.
Errory is a quick and dirty python script to evaluate your  programming assignments. Just give your  zipped assignment and testcases file, it gives the error reports of mismatching test cases,compilation and runtime  errors.




## Getting Started

### Requirements

* Linux/WSL(Windows Subsystem for Linux)/Cygwin Terminal
* Python 3
* GNU Compiler Collection (GCC)
* GDB (optional)
* diff

I have tested the script on WSL, similar behavior is expected on Linux and Cygwin.
### Setting Up

* Download errory.py
* Place the script in the same folder as the zip files
* The program zip file should be according to the conventions provided by the evaluators.
* You can place the files in different folder, but then you would have to give the directory path instead of the file name in the command

### Executing program

* ASSGX_ROLLNO_FIRSTNAME.zip - Zip file containing c code (The filename should be according to the naming convention provided,X is any number)
* Testcases.zip - Zip file containing test cases ( The name of the zipfile has no format restrictions)
* Three options are given inside the python script file which the users can change : TIMEOUT, DELETE_TEMP_FILES and USE_GDB.
* TIMEOUT : Stops execution of the program if it takes more than TIMEOUT seconds to execute.This is considered as a runtime error as an occurence of non terminating program.
* DELETE_TEMP : If this option is set to True  it deletes the temporary files after execution, otherwise it will be  retained.
* USE_GDB : By setting this variable to True , the program will use GDB during runtime errors to give more information about the error. If you haven't installed GDB, set this option to False.

#### Shell Command for execution

```
python3 errory.py ASSG5_ROLLNO_FIRSTNAME.zip Testcases.zip
```

## Output

Compilation errors,Runtime errors(Along with timeout errors) and Mismatching testcases are stored in different files in the error_ASSGX_ subfolder. Mismatching testcases output file is actually the output of the diff command in Linux. To understand the output refer to a tutorial like this [one](https://www.geeksforgeeks.org/diff-command-linux-examples/).

### Sample Output
```
Starting Execution 
The options set are:   
TIMEOUT: 30 seconds    
DELETE_TEMP_FILES: True
USE_GDB: True
Generating Report....  

Checking complete with 0 Compile errors, 4 Runtime errors(0 TIMEOUT errors) and 0 Test case mismatches
Check "error_ASSG5_" folder for detailed report
Happy Coding :)
```

### Sample runtime error file generated with GDB. (Other error files for compile and testcase mismatch errors  are also generated similarly)

```
q1 TestCase2
Segmentation fault (core dumped)


Program received signal SIGSEGV, Segmentation fault.
LIST_DELETE (L=0x7ffffffee0f0, x=0x80054f0) at ./error_ASSG5_/temp/ASSG5_B200735CS_Alen/ASSG5_B200735CS_Alen_1.c:130
130	    printf("%c\n",x->next->key);




q1 TestCase3
Segmentation fault (core dumped)


Program received signal SIGSEGV, Segmentation fault.
LIST_DELETE (L=0x7ffffffee0f0, x=0x80054d0) at ./error_ASSG5_/temp/ASSG5_B200735CS_Alen/ASSG5_B200735CS_Alen_1.c:130
130	    printf("%c\n",x->next->key);




q2 TestCase3
Segmentation fault (core dumped)


Program received signal SIGSEGV, Segmentation fault.
0x00000000080013b3 in LIST_INSERT_AFTER (L=0x7ffffffee0f0, x=0x8006500, y=0x80064c0) at ./error_ASSG5_/temp/ASSG5_B200735CS_Alen/ASSG5_B200735CS_Alen_2.c:80
80	    y->next->previous=x;




q2 TestCase4
Segmentation fault (core dumped)


Program received signal SIGSEGV, Segmentation fault.
0x0000000008001402 in LIST_INSERT_BEFORE (L=0x7ffffffee0f0, x=0x80054f0, y=0x80054b0) at ./error_ASSG5_/temp/ASSG5_B200735CS_Alen/ASSG5_B200735CS_Alen_2.c:90
90	    y->previous->next=x;

```


## Improvements to be done
* Suggest some improvements and collaborate


## Authors


 Alen Antony  


## Version History


* 0.1
    * Initial Release
* 0.2
    * Added Runtime error reporting
    * Reports stored in a subfolder
    * Report overwrite issue resolved
* 0.3
    * Fixed some bugs
    * Mini report on the output terminal
* 0.4
    * The program now handles non terminating programs
    * Timeout and Delete options added
    * Error folder need not be deleted for every execution
* 1.0
    * Shell commands are refactored into python native code.
    * Added GDB support for better info on segmentation faults.
    * Code is rewritten in more readable format.
    * Timeout variable is set up to prevent the script running forever if it encounters non-terminating program.
    * Empty error files are deleted.
    * The temporary files and error files need not be deleted for every execution , it is handled by the code itself.
    * GCC argument added for including math.h library.
    * And other minor changes

## Any doubts on usage 
Contact me at alenantonyme@gmail.com


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
The project is under development , if you find some error or unexpected behaviour please contact me at alenantonyme@gmail.com


## License

This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details
