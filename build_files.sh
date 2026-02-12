# Install dependencies
pip install -r requirements.txt

# Migrasi Database (Supabase) otomatis disini
# Vercel akan menjalankan ini setiap kali Anda deploy ulang
python3.9 manage.py migrate

# Siapkan file statis (CSS/JS untuk halaman Admin)
python3.9 manage.py collectstatic --noinput