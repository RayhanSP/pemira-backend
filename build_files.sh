# Update pip (opsional tapi bagus)
python3.9 -m pip install --upgrade pip

# Install dependencies dengan flag "break-system-packages"
# Ini memaksa install library ke sistem Vercel
python3.9 -m pip install -r requirements.txt --break-system-packages

# Jalankan Migrasi
python3.9 manage.py migrate

# Collect Static
python3.9 manage.py collectstatic --noinput