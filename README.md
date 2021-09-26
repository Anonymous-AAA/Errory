# Errory
Errory is a quick and dirty python script to evaluate your  programming assignments. Just give your  zipped assignment and testcases file, it gives the error reports of mismatching test cases,compilation and runtime  errors.




## Getting Started

### Requirements

* Linux/WSL(Windows Subsystem for Linux)/Cygwin Terminal
* Python 3

I have tested the script on WSL, similar behavior is expected on Linux and Cygwin.
### Setting Up

* Download errory.py
* Place the script in the same folder as the zip files
* You can place the files in different folder, but then you would have to give the directory path instead of the file name in the command

### Executing program

* ASSGX_ROLLNO_FIRSTNAME.zip - Zip file containing c code (The filename should be according to the naming convention provided,X is any number)
* Testcases.zip - Zip file containing test cases
* d(optional)-Delete the decompressed and temporary files
```
python3 errory.py ASSGX_ROLLNO_FIRSTNAME.zip Testcases.zip d
```

## Output

Compilation errors,Runtime errors and Mismatching testcases are stored in different files in the same subfolder. Mismatching testcases output file is actually the output of the diff command in Linux. To understand the output refer to a tutorial like this [one](https://www.geeksforgeeks.org/diff-command-linux-examples/).

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
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Disclaimer
The project is under development , if you find some error or unexpected behaviour please contact me at alenantonyme@gmail.com


## License

This project is licensed under the GNU GPLv3 License - see the LICENSE.md file for details
