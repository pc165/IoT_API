source ./env/bin/activate 
python -m pip install fastapi uvicorn[standard] aiosqlite sqlalchemy
python -m uvicorn main:app --reload