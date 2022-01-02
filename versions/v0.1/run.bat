SET var=%cd%

IF EXIST "%var%\venv" (
	cd venv/Scripts/
	call activate.bat
	cd ../../
  call python app.py

) ELSE (
  call python -m venv venv
	cd venv/Scripts/
	call activate.bat
	cd ../../
	call python -m pip install --upgrade pip
	pip install -r "%var%\requirements.txt"
  call python app.py
)