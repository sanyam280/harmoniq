<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MelodicMind</title>
  <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: linear-gradient(to bottom right, #00008B, #203a43, #2c5364);
      color: #ffffff;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-start;
      min-height: 100vh;
      text-align: center;
      padding: 40px 20px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      max-width: 1200px;
      padding: 10px 20px;
      background-color: rgba(255,255,255,0.05);
      border-radius: 12px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }

    .logo {
      display: flex;
      align-items: center;
    }

    .logo span {
      font-size: 32px;
      margin-right: 10px;
    }

    .logo h1 {
      font-size: 1.8rem;
      color: #4fbcf7;
      margin: 0;
    }

    nav a {
      color: #b2ebf2;
      text-decoration: none;
      margin: 0 12px;
      font-size: 1rem;
      transition: color 0.3s ease;
    }

    nav a:hover {
      color: #ffffff;
    }

    footer {
      margin-top: auto;
      padding: 20px;
      font-size: 0.9rem;
      color: #90caf9;
      text-align: center;
    }

    h1 {
      font-size: 3rem;
      margin-bottom: 0.2rem;
      color: #4fc3f7;
    }

    p.tagline {
      font-size: 2.4rem;
      margin-bottom: 2rem;
      color: #b2ebf2;
      font-style: Playfair Display, cursive;
      font-weight: 400;        
    }

    .btn {
      padding: 0.8rem 1.8rem;
      font-size: 1.1rem;
      border: none;
      border-radius: 25px;
      background-color: #4fc3f7;
      color: #ffffff;
      cursor: pointer;
      transition: 0.3s ease;
      margin: 0.5rem;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    }

    .btn:hover {
      background-color: #29b6f6;
      transform: translateY(-2px);
    }

    #videoContainer {
      display: none;
      margin-top: 20px;
      border: 3px solid #4dd0e1;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }

    video {
      width: 360px;
      height: 270px;
      object-fit: cover;
    }

    #recommendationSection {
      margin-top: 40px;
      width: 100%;
      max-width: 600px;
      text-align: left;
      background: rgba(255,255,255,0.1);
      padding: 20px;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }

    #recommendationSection h2 {
      margin-top: 0;
      color: #ffffff;
      font-size: 1.8rem;
    }

    #moodLabel {
      font-weight: bold;
      color: #ffd54f;
    }

    #songList {
      list-style: none;
      padding: 0;
      margin-top: 10px;
    }

    #songList li {
      background: rgba(255,255,255,0.1);
      margin: 0.5rem 0;
      padding: 1rem;
      border-radius: 8px;
      font-size: 1rem;
      color: #ffffff;
    }
  </style>
</head>
<body>
  <header>
    <div class="logo">
      <span>🎵</span>
      <h1>Harmoniq</h1>
    </div>
    <nav>
      <a href="#">Home</a>
      <a href="#infoSection">About</a>
      <a href="#recommendationSection">Recommendations</a>
    </nav>
  </header>

  <p class="tagline">Capturing Emotions, Discovering Melodies</p>

  <section id="quoteSection" style="margin-top: 30px; text-align: center; max-width: 800px;">
    <blockquote style="font-size: 2rem; font-style: italic; color: #e3f2fd;">
      "Music can change the world because it can change people."
    </blockquote>
    <p style="margin-top: 10px; font-size: 1rem; color: #bbdefb;">– Bono</p>
  </section>

  <section id="infoSection" style="margin-top: 40px; text-align: center; max-width: 850px; background-color: rgba(255,255,255,0.08); padding: 25px; border-radius: 12px;">
    <h2 style="font-size: 2rem; color: #ffeb3b;">The Science & Soul of Music</h2>
    <p style="margin-top: 15px; font-size: 1.1rem; color: #ffffff; line-height: 1.6;">
      Music has the power to uplift our spirits, calm our anxiety, or energize us in moments of fatigue. Scientific studies show that listening to music stimulates the brain’s reward centers, releasing dopamine – the "feel good" hormone.
      <br><br>
      Whether you're feeling down or on top of the world, the right tune can guide your emotional journey. That’s the magic Harmoniq brings — a melody for every emotion, handpicked for your unique mood.
    </p>
  </section>

  <button class="btn" onclick="startCamera()">Start Camera</button>
  <button class="btn" onclick="captureMood()">Capture Mood</button>

  <div id="videoContainer">
    <video id="video" autoplay></video>
  </div>

  <div id="recommendationSection">
    <h2>Mood: <span id="moodLabel">None</span></h2>
    <ul id="songList">
      <!-- Songs will be injected here -->
    </ul>
  </div>

  <footer>
    &copy; 2025 Harmoniq. All rights reserved.
  </footer>

  <script>
    const video = document.getElementById('video');
    const videoContainer = document.getElementById('videoContainer');
    const moodLabel = document.getElementById('moodLabel');
    const songList = document.getElementById('songList');
  
    async function startCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        video.srcObject = stream;
        videoContainer.style.display = 'block';
      } catch (err) {
        alert('Error accessing camera: ' + err.message);
      }
    }
  
    async function captureMood() {
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      const context = canvas.getContext('2d');
      context.drawImage(video, 0, 0, canvas.width, canvas.height);
  
      const blob = await new Promise(resolve => canvas.toBlob(resolve, 'image/jpeg'));
  
      const formData = new FormData();
      formData.append('image', blob, 'frame.jpg');
  
      try {
        const response = await fetch('https://harmoniq-ir8l.onrender.com/analyze', {
          method: 'POST',
          body: formData
        });
  
        if (!response.ok) {
          throw new Error('Failed to fetch from backend');
        }
  
        const data = await response.json();
        const { emotion, recommendations } = data;
  
        moodLabel.textContent = emotion;
        songList.innerHTML = '';
        console.log('Backend response:', data);
        console.log('Recommendations:', recommendations);

        recommendations.forEach(song => {
            const li = document.createElement('li');
            li.textContent = `${song.title} by ${song.artist}`;
            songList.appendChild(li);
        });

  
      } catch (err) {
        alert('Error detecting mood: ' + err.message);
      }
    }
  </script>
  
</body>
</html>
