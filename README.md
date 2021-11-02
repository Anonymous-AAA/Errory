# Errory
## Tired of executing testcases one by one for your assignment🤨 Here's a solution for that.
Errory is a quick and dirty python script to evaluate your  programming assignments. Just give your  zipped assignment and testcases file, it gives the error reports of mismatching test cases,compilation and runtime  errors.




## Getting Started

### Requirements

* Linux/WSL(Windows Subsystem for Linux)/Cygwin Terminal
* Python 3
* GNU C Compiler (GCC)

I have tested the script on WSL, similar behavior is expected on Linux and Cygwin.
### Setting Up

* Download errory.py
* Place the script in the same folder as the zip files
* The program zip file should be according to the conventions provided by the evaluators.
* You can place the files in different folder, but then you would have to give the directory path instead of the file name in the command

### Executing program

* ASSGX_ROLLNO_FIRSTNAME.zip - Zip file containing c code (The filename should be according to the naming convention provided,X is any number)
* Testcases.zip - Zip file containing test cases
* Two options are given inside the python script file which the users can change :Timeout and Delete
* Timeout : Stops execution of the program if it takes more than Timeout seconds to execute.This is considered as a runtime error as an occurence of non terminating program.
* Delete : If the option is set to True  it deletes the temporary files after execution, anything else will retain it.Please delete these files for every execution if you are thinking to retain it.

```
python3 errory.py ASSGX_ROLLNO_FIRSTNAME.zip Testcases.zip d
```

## Output

Compilation errors,Runtime errors(Along with timeout errors) and Mismatching testcases are stored in different files in the same subfolder. Mismatching testcases output file is actually the output of the diff command in Linux. To understand the output refer to a tutorial like this [one](https://www.geeksforgeeks.org/diff-command-linux-examples/).

### Sample Output
```
Starting Execution 
The options set are: 
Timeout: 30 seconds  
Delete: True
Generating Report....

Checking complete with 0 Compile errors, 4 Runtime errors(0 Timeout errors) and 0 Test case mismatches
Check "error_ASSG5_" folder for detailed report
Happy Coding :)
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
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
The project is under development , if you find some error or unexpected behaviour please contact me at alenantonyme@gmail.com


## License

This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details
