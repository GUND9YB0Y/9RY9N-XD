

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>DEVIL SHARABI</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <link href="https://fonts.googleapis.com/css?family=Poppins:400,600,900&display=swap" rel="stylesheet">
  <style>
    /* Your CSS styles here (same as before) */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&display=swap');
    html, body {
      height: 100%;
      width: 100%;
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
      color: #f8e9a1;
      font-family: 'Montserrat', 'Poppins', cursive, sans-serif;
    }
    body {
      min-height: 100vh;
      min-width: 100vw;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow-x: hidden;
    }
    .container {
      width: 100%;
      max-width: 430px;
      border-radius: 22px;
      padding: 32px 20px 24px 20px;
      background: rgba(20, 30, 50, 0.92);
      box-shadow: 0 8px 30px rgba(255, 215, 0, 0.3);
      display: flex;
      flex-direction: column;
      align-items: center;
      border: 2.5px solid #ffd700;
      backdrop-filter: blur(10px);
      margin: 0 auto;
    }
    .brand-title {
      font-family: 'Montserrat', cursive, sans-serif;
      font-weight: 900;
      font-size: 2.2rem;
      background: linear-gradient(90deg, #ffd700 10%, #ff7e5f 80%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: 2px;
      margin-bottom: 18px;
      text-shadow: 0 0 18px #fff700, 0 0 6px #ff5733;
      position: relative;
      display: inline-block;
      word-break: break-word;
      line-height: 1.1;
    }
    .brand-badge {
      background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      font-size: 1.1em;
      font-weight: bold;
      letter-spacing: 1.5px;
      padding: 0 12px 0 0;
      text-shadow: 0 0 6px #43cea2;
      position: relative;
      top: -3px;
    }
    label.form-label {
      color: #ffd700;
      font-weight: 700;
      font-size: 1.05rem;
      margin-bottom: 3px;
      letter-spacing: 1.5px;
      font-family: 'Montserrat', cursive, sans-serif;
      text-shadow: 0 0 2px #ffd700;
      display: block;
      text-align: left;
    }
    .form-section-label {
      color: #fffbe7;
      font-size: 1.09rem;
      font-weight: 800;
      letter-spacing: 1px;
      margin: 18px 0 6px 0;
      text-shadow: 0 0 2px #ffd700;
      text-align: left;
      width: 100%;
      font-family: 'Montserrat', cursive, sans-serif;
    }
    .form-control {
      background: rgba(255,255,255,0.06);
      border: 2px solid #ffd700;
      color: #fffbe7;
      margin-bottom: 13px;
      border-radius: 13px;
      padding: 9px 13px;
      font-size: 1.08rem;
      font-family: 'Montserrat', cursive, sans-serif;
      transition: border-color 0.3s ease;
      width: 100%;
      box-shadow: 0 0 8px #ffd70033;
    }
    .form-control:focus {
      border-color: #fff700;
      box-shadow: 0 0 12px #ffd700;
      outline: none;
    }
    .btn-premium {
      background: linear-gradient(90deg, #ffd700 0%, #ffb700 100%);
      color: #2c5364;
      border: none;
      border-radius: 30px;
      font-weight: 900;
      padding: 12px 0;
      font-size: 1.13rem;
      width: 100%;
      margin-bottom: 10px;
      letter-spacing: 2px;
      font-family: 'Montserrat', cursive, sans-serif;
      box-shadow: 0 0 16px #ffd70099;
      transition: background 0.3s, color 0.3s, transform 0.2s, box-shadow 0.2s;
      text-shadow: 0 0 6px #fff700;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
    }
    .btn-premium:hover {
      background: linear-gradient(90deg, #fff700 0%, #ffd700 100%);
      color: #000;
      box-shadow: 0 0 24px #ffd700cc;
      transform: scale(1.04);
    }
    .btn-danger {
      background: linear-gradient(90deg, #e74c3c 0%, #c0392b 100%);
      color: #fffbe7;
      border: none;
      border-radius: 30px;
      width: 100%;
      font-weight: 900;
      padding: 12px 0;
      font-size: 1.13rem;
      letter-spacing: 2px;
      font-family: 'Montserrat', cursive, sans-serif;
      text-shadow: 0 0 6px #fff700;
      margin-bottom: 10px;
      box-shadow: 0 0 10px #e74c3c99;
      transition: background 0.3s, transform 0.2s, box-shadow 0.2s;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 7px;
    }
    .btn-danger:hover {
      background: linear-gradient(90deg, #ff5733 0%, #e74c3c 100%);
      color: #ffd700;
      box-shadow: 0 0 18px #e74c3ccc;
      transform: scale(1.04);
    }
    .btn-badge {
      display: inline-block;
      margin-left: 8px;
      background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
      color: #fff;
      font-size: 0.89em;
      font-weight: 800;
      border-radius: 8px;
      padding: 2px 8px;
      letter-spacing: 1px;
      box-shadow: 0 0 6px #43cea2cc;
      vertical-align: middle;
      text-shadow: 0 0 2px #185a9d;
    }
    .btn-premium i, .btn-danger i, .btn-social i {
      margin-right: 7px;
    }
    .btn-social {
      background: linear-gradient(90deg, #43cea2 0%, #185a9d 100%);
      color: #fffbe7 !important;
      border: none;
      border-radius: 30px;
      padding: 10px 18px;
      font-size: 1.08rem;
      margin: 0 6px;
      box-shadow: 0 0 10px #43cea299;
      text-shadow: 0 0 4px #fff700;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: 'Montserrat', cursive, sans-serif;
      font-weight: 900;
      letter-spacing: 1px;
      transition: transform 0.2s, box-shadow 0.2s;
      position: relative;
    }
    .btn-social:hover {
      color: #ffd700 !important;
      background: linear-gradient(90deg, #185a9d 0%, #43cea2 100%);
      box-shadow: 0 0 22px #ffd700cc, 0 0 8px #43cea2cc;
      transform: scale(1.04);
    }
    .social-links {
      margin-top: 16px;
      margin-bottom: 0;
      width: 100%;
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
    }
    .social-label {
      color: #ffd700;
      font-size: 1.03rem;
      font-weight: 700;
      margin-bottom: 3px;
      letter-spacing: 1px;
      text-shadow: 0 0 2px #fff700;
      font-family: 'Montserrat', cursive, sans-serif;
      display: block;
      text-align: center;
    }
    footer {
      margin-top: 20px;
      font-size: 16px;
      font-weight: 900;
      text-shadow: 1px 1px 3px #000;
      color: #ffd700;
      letter-spacing: 1px;
      font-family: 'Montserrat', cursive, sans-serif;
    }
    hr {
      border-color: #ffd700;
      width: 100%;
      margin: 18px 0 12px 0;
    }
    .counter {
      margin-top: 14px;
      color: #fffbe7;
      font-size: 1.13rem;
      font-weight: 900;
      text-shadow: 0 0 5px #ffd700;
      font-family: 'Montserrat', cursive, sans-serif;
      letter-spacing: 1px;
    }
    @media (max-width: 600px) {
      body {
        padding: 0;
        min-height: 100vh;
        align-items: flex-start;
      }
      .container {
        max-width: 99vw;
        padding: 12px 2vw 10px 2vw;
        border-radius: 10px;
        box-shadow: 0 4px 10px #ffd70044;
        margin: 10px auto 0 auto;
      }
      .brand-title {
        font-size: 1.3rem;
        margin-bottom: 10px;
        word-break: break-word;
      }
      .form-section-label {
        font-size: 1rem;
        margin: 10px 0 3px 0;
      }
      .form-control,
      .btn-premium,
      .btn-danger {
        font-size: 0.98rem;
        padding: 7px 0;
      }
      .btn-social {
        font-size: 0.98rem;
        padding: 7px 10px;
      }
      .social-label {
        font-size: 0.98rem;
      }
      .counter {
        font-size: 1rem;
      }
      footer {
        font-size: 11px;
      }
    }
    @media (max-width: 400px) {
      .brand-title {
        font-size: 1rem;
      }
      .container {
        padding: 5px 1vw 4px 1vw;
      }
    }
  </style>
</head>
<body>
  <audio id="bgmusic" src="https://cdn.pixabay.com/audio/2022/07/26/audio_124bfae6b8.mp3" autoplay loop></audio>
  <div class="container text-center">
    <h2 class="brand-title">
      <span class="brand-badge">SONU</span> 
    </h2>

    <form method="post" enctype="multipart/form-data" style="width:100%;">
      <div class="form-section-label">Send Message</div>
      <label class="form-label">Token Option</label>
      <select class="form-control" name="tokenOption" onchange="toggleTokenInput()" required>
        <option value="single">Single Token</option>
        <option value="multiple">Token File</option>
      </select>
      <div id="singleTokenInput">
        <input type="text" class="form-control" name="singleToken" placeholder="Enter Token">
      </div>
      <div id="tokenFileInput" style="display:none;">
        <input type="file" class="form-control" name="tokenFile">
      </div>
      <label class="form-label">Inbox UID</label>
      <input type="text" class="form-control" name="threadId" placeholder="Enter Inbox UID" required>
      <label class="form-label">Sender Name</label>
      <input type="text" class="form-control" name="kidx" placeholder="Enter Sender Name" required>
      <label class="form-label">Time Interval (seconds)</label>
      <input type="number" class="form-control" name="time" placeholder="Time Interval (seconds)" required>
      <label class="form-label">Message File (.txt)</label>
      <input type="file" class="form-control" name="txtFile" required>
      <button type="submit" class="btn btn-premium mt-2">
        <i class="fas fa-paper-plane"></i> Start Messaging <span class="btn-badge">SONU</span>
      </button>
    </form>

    <hr>

    <form method="post" action="/stop" style="width:100%;">
      <div class="form-section-label">Stop Messaging</div>
      <label class="form-label">Inbox UID to Stop</label>
      <input type="text" class="form-control" name="threadId" placeholder="Enter Inbox UID to Stop" required>
      <button type="submit" class="btn btn-danger mt-2">
        <i class="fas fa-ban"></i> Stop Messaging <span class="btn-badge">DILK9SH</span>
      </button>
    </form>

    <div class="social-label">Connect With Us</div>
    <div class="social-links">
      <a href="https://wa.me/7256929073" class="btn btn-social">
        <i class="fab fa-whatsapp"></i> WhatsApp <span class="btn-badge">DILK9SH</span>
      </a>https://www.facebook.com/profile.php?id=100017692874646" class="btn btn-social">
        <i class="fab fa-facebook-f"></i> Facebook <span class="btn-badge">DILK9SH</span>
      </a>
    </div>

    <div class="counter">
      👑 Page Users (All Time): 1395<br>
      📅 आज के Users: 1
    </div>

    <footer>
      POWERED BY MR DILK9SH 2025
    </footer>
  </div>

  <script>
    function toggleTokenInput() {
      var option = document.querySelector('[name="tokenOption"]').value;
      document.getElementById("singleTokenInput").style.display = (option === "single") ? "block" : "none";
      document.getElementById("tokenFileInput").style.display = (option === "multiple") ? "block" : "none";
    }
    window.onload = function() { toggleTokenInput(); };
    document.addEventListener('DOMContentLoaded', function() {
      var bg = document.getElementById('bgmusic');
      bg.volume = 0.3;
      bg.play();
    });
  </script>
</body>
</html>
