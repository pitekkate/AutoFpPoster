from flask import Flask, render_template, request, flash
import facebook
from flask_apscheduler import APScheduler
from datetime import datetime
import os

# --- Konfigurasi Aplikasi ---
class Config:
    """Konfigurasi untuk Flask dan APScheduler."""
    SCHEDULER_API_ENABLED = True
    # Menggunakan SQLAlchemy sebagai backend untuk menyimpan data job
    # File database akan bernama 'scheduler.sqlite' di direktori yang sama
    SCHEDULER_JOBSTORES = {
        'default': {'type': 'sqlalchemy', 'url': 'sqlite:///scheduler.sqlite'}
    }

app = Flask(__name__)
app.config.from_object(Config())
app.secret_key = 'kunci_rahasia_untuk_penjadwalan_yang_aman'

# --- Fungsi untuk Posting ke Facebook ---
def execute_facebook_post(page_id, page_access_token, message):
    """
    Fungsi inti yang akan dieksekusi oleh scheduler atau secara langsung.
    Mencetak status ke konsol server.
    """
    print(f"[{datetime.now()}] Mencoba memposting ke Page ID: {page_id}...")
    try:
        graph = facebook.GraphAPI(access_token=page_access_token, version="v19.0")
        post_result = graph.put_object(
            parent_object=page_id,
            connection_name='feed',
            message=message
        )
        print(f">>> SUKSES: Post berhasil dibuat dengan ID: {post_result['id']}")
    except facebook.GraphAPIError as e:
        print(f">>> GAGAL: Terjadi kesalahan GraphAPI: {e.message}")
    except Exception as e:
        print(f">>> GAGAL: Terjadi kesalahan tidak terduga: {str(e)}")


# --- Inisialisasi Scheduler ---
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# --- Tampilan dan Logika Web ---
@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Menampilkan halaman utama, memproses form, dan menjadwalkan postingan.
    """
    if request.method == 'POST':
        page_id = request.form.get('page_id')
        page_token = request.form.get('page_token')
        message = request.form.get('message')
        schedule_time_str = request.form.get('schedule_time')

        if not page_id or not page_token or not message:
            flash("Page ID, Page Access Token, dan Message wajib diisi!", "error")
        else:
            # Jika pengguna mengisi waktu penjadwalan
            if schedule_time_str:
                try:
                    # Ubah string waktu dari form menjadi objek datetime
                    schedule_time = datetime.fromisoformat(schedule_time_str)
                    
                    # Validasi agar waktu tidak di masa lalu
                    if schedule_time < datetime.now():
                        flash("Waktu penjadwalan tidak boleh di masa lalu.", "error")
                    else:
                        # Tambahkan job ke scheduler
                        scheduler.add_job(
                            id=f'post_{page_id}_{int(schedule_time.timestamp())}', # ID unik untuk job
                            func=execute_facebook_post,
                            trigger='date',
                            run_date=schedule_time,
                            args=[page_id, page_token, message]
                        )
                        flash(f"Postingan berhasil dijadwalkan untuk {schedule_time.strftime('%d %B %Y pukul %H:%M')}.", "success")
                except ValueError:
                    flash("Format tanggal dan waktu tidak valid.", "error")
            # Jika tidak ada waktu, posting langsung
            else:
                execute_facebook_post(page_id, page_token, message)
                flash("Postingan berhasil dikirim sekarang juga!", "success")

    # Ambil daftar job yang sedang dijadwalkan untuk ditampilkan
    jobs = scheduler.get_jobs()
    return render_template('index.html', jobs=jobs)

# Route untuk menghapus job yang dijadwalkan
@app.route('/delete_job/<job_id>')
def delete_job(job_id):
    try:
        scheduler.remove_job(job_id)
        flash(f"Jadwal dengan ID {job_id} berhasil dihapus.", "success")
    except Exception as e:
        flash(f"Gagal menghapus jadwal: {str(e)}", "error")
    return index()


if __name__ == '__main__':
    # Hapus file database lama jika ada untuk memulai dari awal (opsional)
    if os.path.exists('scheduler.sqlite'):
        print("Menghapus database scheduler lama...")
        os.remove('scheduler.sqlite')
        
    app.run(debug=True, use_reloader=False) # use_reloader=False penting agar scheduler tidak berjalan dua kali
