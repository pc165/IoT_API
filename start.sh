source ./env/bin/activate 
python -m pip install fastapi "uvicorn[standard]" aiosqlite sqlalchemy "python-jose[cryptography]" "passlib[bcrypt]" python-multipart
python -m uvicorn main:app --host 0.0.0.0 --reload
