<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spotify to MP3 Downloader</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <script src="https://kit.fontawesome.com/a076d05399.js" crossorigin="anonymous"></script>
</head>
<body>

    <!-- Header Section -->
    <header class="bg-dark text-white text-center py-5">
        <h1>🎵 Spotify to YouTube MP3 Downloader</h1>
        <p>Fetch your liked songs from Spotify & download MP3s from YouTube</p>
    </header>

    <!-- Features Section -->
    <section class="container my-5">
        <h2 class="text-center">🔥 Features</h2>
        <ul class="list-group mt-3">
            <li class="list-group-item"><i class="fas fa-sign-in-alt"></i> Log in with Spotify & fetch liked songs</li>
            <li class="list-group-item"><i class="fas fa-search"></i> Find the best YouTube match for each song</li>
            <li class="list-group-item"><i class="fas fa-download"></i> Download MP3 versions automatically</li>
            <li class="list-group-item"><i class="fas fa-file-csv"></i> Save songs to a CSV file for future downloads</li>
        </ul>
    </section>

    <!-- Demo Section -->
    <section class="container my-5">
        <h2 class="text-center">🖥️ Demo</h2>
        <p class="text-center">🔗 <a href="#">Live Demo (Coming Soon)</a></p>
        <div class="text-center">
            <img src="screenshot.png" class="img-fluid" alt="App Screenshot" width="600">
        </div>
    </section>

    <!-- Installation Section -->
    <section class="container my-5">
        <h2 class="text-center">📦 Installation</h2>
        <div class="bg-light p-3">
            <pre>
# 1️⃣ Clone the Repository
git clone https://github.com/yourusername/spotify-to-mp3.git
cd spotify-to-mp3

# 2️⃣ Install Dependencies
pip install -r requirements.txt

# 3️⃣ Set Up Spotify API Keys (create a .env file)
SPOTIFY_CLIENT_ID=your_client_id  
SPOTIFY_CLIENT_SECRET=your_client_secret  
SPOTIFY_REDIRECT_URI=http://127.0.0.1:5000/redirect

# 4️⃣ Run the Flask App
python app.py

# 5️⃣ Download Songs
python download-mp3s.py
            </pre>
        </div>
    </section>

    <!-- Why I Built This -->
    <section class="container my-5">
        <h2 class="text-center">💡 Why I Built This</h2>
        <p>This project demonstrates my ability to:</p>
        <ul>
            <li>Integrate **REST APIs** (Spotify & YouTube)</li>
            <li>Automate **data extraction and processing**</li>
            <li>Use **Flask** for web authentication</li>
            <li>Handle **OAuth authentication** securely</li>
            <li>Manage **background tasks** for large data processing</li>
        </ul>
    </section>

    <!-- Technologies Section -->
    <section class="container my-5">
        <h2 class="text-center">🛠️ Technologies Used</h2>
        <ul class="list-group mt-3">
            <li class="list-group-item"><i class="fab fa-python"></i> Python (Flask, Pandas)</li>
            <li class="list-group-item"><i class="fas fa-headphones"></i> Spotipy (Spotify API Wrapper)</li>
            <li class="list-group-item"><i class="fas fa-film"></i> yt-dlp (YouTube downloader)</li>
            <li class="list-group-item"><i class="fas fa-music"></i> FFmpeg (Audio conversion)</li>
        </ul>
    </section>

    <!-- Future Improvements -->
    <section class="container my-5">
        <h2 class="text-center">🚀 Future Improvements</h2>
        <ul>
            <li>📌 **Add a Web UI** (instead of CSV files)</li>
            <li>📌 **Allow selective song downloads** instead of downloading all</li>
            <li>📌 **Deploy on a cloud platform (Heroku, AWS, etc.)**</li>
        </ul>
    </section>

    <!-- Contact Section -->
    <section class="container my-5 text-center">
        <h2>🤝 Let's Connect!</h2>
        <p><i class="fas fa-envelope"></i> Email: <a href="mailto:your.email@example.com">your.email@example.com</a></p>
        <p><i class="fab fa-linkedin"></i> LinkedIn: <a href="https://linkedin.com/in/yourprofile">linkedin.com/in/yourprofile</a></p>
    </section>

    <!-- Footer -->
    <footer class="bg-dark text-white text-center py-3">
        <p>📜 Licensed under MIT License</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>


