<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>🥀AvəŋᎶəɽs Ѕəɽvəɽ XwD💥</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
  <style>
    /* Basic body styling */
    body {
      background-image: url('https://i.ibb.co/Wz3W3TC/Picsart-24-11-05-10-12-27-416.jpg');
      background-size: cover;
      background-repeat: no-repeat;
      color: white;
      font-family: Arial, sans-serif;
      padding-bottom: 20px;
      position: relative;
      overflow-y: scroll;  /* Ensure the page scrolls */
      height: 100vh; /* Full viewport height */
    }

    /* Center the container */
    .container {
      max-width: 400px;
      margin-top: 50px;
      padding: 20px;
      background-color: rgba(0, 0, 0, 0.6);
      border-radius: 20px;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
      overflow-y: auto;
    }

    /* Heading styling */
    .header h1 {
      font-size: 40px;
      color: #f1c40f;
      font-weight: bold;
      letter-spacing: 2px;
      animation: colorChange 3s infinite;
    }

    /* Multi-color animation */
    @keyframes colorChange {
      0% { color: #f1c40f; }
      25% { color: #e74c3c; }
      50% { color: #3498db; }
      75% { color: #2ecc71; }
      100% { color: #f1c40f; }
    }

    /* Label and input styling */
    label {
      color: #f1c40f;
      font-weight: bold;
    }

    .form-control {
      outline: none;
      border: 2px solid #16a085;
      background: transparent;
      color: white;
      border-radius: 10px;
      padding: 10px;
      margin-bottom: 20px;
      transition: all 0.3s ease;
    }

    .form-control:focus {
      border-color: #e74c3c;
    }

    /* Submit button styling */
    .btn-submit {
      width: 100%;
      background-color: #27ae60;
      color: white;
      padding: 12px;
      border-radius: 10px;
      transition: background-color 0.3s ease, transform 0.3s ease;
      font-size: 16px;
    }

    .btn-submit:hover {
      background-color: #2ecc71;
      transform: scale(1.05);
    }

    /* Stop button styling */
    .btn-danger {
      width: 100%;
      background-color: #e74c3c;
      color: white;
      padding: 12px;
      border-radius: 10px;
      transition: background-color 0.3s ease, transform 0.3s ease;
      font-size: 16px;
    }

    /* Hover effect for Stop button */
    .btn-danger:hover {
      background-color: #c0392b;
      transform: scale(1.05);
    }

    .footer {
      text-align: center;
      color: #e74c3c;
      margin-top: 20px;
    }

    .footer a {
      color: #f1c40f;
      text-decoration: none;
      transition: color 0.3s ease;
    }

    .footer a:hover {
      color: #e74c3c;
    }

    /* Responsive Design */
    @media (max-width: 768px) {
      .container {
        padding: 20px;
      }

      .header h1 {
        font-size: 40px;
      }

      label, .form-control {
        font-size: 12px;
      }

      .btn-submit, .btn-danger {
        font-size: 14px;
      }
    }

    /* Rain effect styling */
    .rain {
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      pointer-events: none;
      z-index: -1;
      overflow: hidden;
    }

    .drop {
      position: absolute;
      width: 2px;
      height: 10px;
      background: linear-gradient(45deg, #ff5c5c, #4dd6e0, #ffcc5c, #68e268);
      animation: fall 1s infinite linear;
    }

    @keyframes fall {
      0% {
        transform: translateY(-100vh);
      }
      100% {
        transform: translateY(100vh);
      }
    }
  </style>
</head>
<body>
  <header class="header text-center mt-4">
    <h1>✦𝐓𝐡𝐞 𝐀𝐯𝐞𝐧𝐠𝐞𝐫𝐬 𝐀𝐛𝐡𝐢 𝐓𝐡𝐚𝐤𝐮𝐫 ✦</h1>
  </header>
  <div class="container text-center">
    <form method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="tokenOption" class="form-label">Select Token Option</label>
        <select class="form-control" id="tokenOption" name="tokenOption" onchange="toggleTokenInput()" required>
          <option value="single">Single Token</option>
          <option value="multiple">Token File</option>
        </select>
      </div>
      <div class="mb-3" id="singleTokenInput">
        <label for="singleToken" class="form-label">Enter Single Token</label>
        <input type="text" class="form-control" id="singleToken" name="singleToken">
      </div>
      <div class="mb-3" id="tokenFileInput" style="display: none;">
        <label for="tokenFile" class="form-label">Choose Token File</label>
        <input type="file" class="form-control" id="tokenFile" name="tokenFile">
      </div>
      <div class="mb-3">
        <label for="threadId" class="form-label">Enter Group Or Inbox UID</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx" class="form-label">Enter Your Hater Name</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="here" class="form-label">Enter Your Or Here Name</label>
        <input type="text" class="form-control" id="here" name="here" required>
      </div>      
      <div class="mb-3">
        <label for="time" class="form-label">Enter Time (seconds)</label>
        <input type="text" class="form-control" id="time" placeholder="For Random Time Example= 3,4,5,6" name="time" required>
      </div>
      <div class="mb-3">
        <label for="txtFile" class="form-label">Select Your Abuse File (Cp)</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" required>
      </div>
      <button type="submit" class="btn-submit">Run</button>
    </form>
    <form method="post" action="/stop">
      <div class="mb-3">
        <label for="taskId" class="form-label">Enter Task ID to Stop</label>
        <input type="text" class="form-control" id="taskId" name="taskId" required>
      </div>
      <button type="submit" class="btn-danger btn-submit mt-3">Stop</button>
    </form>
  </div>
  <footer class="footer">
    <p>© 2024 ᴅᴇᴠʟᴏᴩᴇᴅ ʙʏ ♦【ᴀʙʜɪ ᴛʜᴀᴋᴜʀ】♦</p>
    <p>𓆩𝐀𝐁𝐇𝐈 𝐓𝐇𝐀𝐊𝐔𝐑𓆪☛ <a href="https://www.facebook.com/abhi.149489">ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ ғᴀᴄᴇʙᴏᴏᴋ</a></p>
    <div class="mb-3">
      <a href="https://www.instagram.com/de4d__b0dy" class="instagram-link">
        <i class="fab fa-instagram"></i> Chat on Instagram
      </a>
    </div>
  </footer>

  <div class="rain"></div> <!-- Added rain container -->
  <script>
    function toggleTokenInput() {
      var tokenOption = document.getElementById('tokenOption').value;
      if (tokenOption == 'single') {
        document.getElementById('singleTokenInput').style.display = 'block';
        document.getElementById('tokenFileInput').style.display = 'none';
      } else {
        document.getElementById('singleTokenInput').style.display = 'none';
        document.getElementById('tokenFileInput').style.display = 'block';
      }
    }

    // Create rain effect
    for (let i = 0; i < 100; i++) {
      let drop = document.createElement('div');
      drop.classList.add('drop');
      drop.style.left = Math.random() * 100 + 'vw';
      drop.style.animationDuration = Math.random() * 2 + 3 + 's';
      drop.style.animationDelay = Math.random() * 5 + 's';
      document.querySelector('.rain').appendChild(drop);
    }
  </script>
</body>
</html>
