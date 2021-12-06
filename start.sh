source ./env/bin/activate 
python -m pip install fastapi
python -m pip install "uvicorn[standard]"
python -m uvicorn main:app --reload