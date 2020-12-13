@ECHO OFF
//:B
SET MyProcess=python.exe
ECHO "%MyProcess%"
TASKLIST | FINDSTR /I "%MyProcess%"
IF ERRORLEVEL 1 (GOTO :StartScripts) ELSE (TASKKILL /F /IM python.exe )

set FLASK_ENV=development
python app.py

//GOTO :B 

:StartScripts 
::: //-- Put in the full path to the batch scripts to call
::: //-- Be sure the security context this process runs as has access to execute the below called batch scripts
set FLASK_ENV=development
python app.py
GOTO :B 