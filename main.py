<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🔥 ARYAN RAJ POST SERVER 🔥</title>
    <style>
        :root {
            --primary: #ff2d2d;
            --secondary: #2b2b2b;
            --accent: #ff6b6b;
            --text: #f0f0f0;
            --success: #28a745;
            --danger: #dc3545;
            --warning: #ffc107;
            --info: #17a2b8;
        }
        
        body {
            background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
            color: var(--text);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            min-height: 100vh;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        
        .header {
            background: linear-gradient(90deg, var(--secondary) 0%, #1a1a1a 100%);
            padding: 1.5rem;
            border-bottom: 2px solid var(--primary);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        
        .title {
            font-size: 2.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, var(--primary) 0%, var(--accent) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            margin-bottom: 0.5rem;
        }
        
        .subtitle {
            color: var(--accent);
            font-size: 1.2rem;
            margin-bottom: 0;
        }
        
        .card {
            background: rgba(43, 43, 43, 0.8);
            border: 1px solid rgba(255, 45, 45, 0.3);
            border-radius: 8px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(10px);
            margin-bottom: 2rem;
            transition: all 0.3s ease;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.3);
            border-color: rgba(255, 45, 45, 0.6);
        }
        
        .card-header {
            background: linear-gradient(90deg, rgba(255, 45, 45, 0.2) 0%, rgba(43, 43, 43, 0) 100%);
            border-bottom: 1px solid rgba(255, 45, 45, 0.3);
            font-weight: 600;
            color: var(--accent);
        }
        
        .form-control {
            background: rgba(30, 30, 30, 0.8);
            border: 1px solid rgba(255, 45, 45, 0.3);
            color: var(--text);
            border-radius: 4px;
            padding: 12px 15px;
            transition: all 0.3s;
        }
        
        .form-control:focus {
            background: rgba(40, 40, 40, 0.9);
            border-color: var(--primary);
            box-shadow: 0 0 0 0.2rem rgba(255, 45, 45, 0.25);
            color: var(--text);
        }
        
        .btn-devil {
            background: linear-gradient(90deg, var(--primary) 0%, #ff5252 100%);
            border: none;
            color: white;
            font-weight: 600;
            padding: 12px 25px;
            border-radius: 4px;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s;
            box-shadow: 0 4px 8px rgba(255, 45, 45, 0.3);
        }
        
        .btn-devil:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(255, 45, 45, 0.4);
            background: linear-gradient(90deg, #ff1a1a 0%, #ff5252 100%);
            color: white;
        }
        
        .status-success { color: var(--success); }
        .status-failed { color: var(--danger); }
        .status-running { color: var(--info); }
        .status-stopped { color: var(--warning); }
        
        .log-entry {
            background: rgba(30, 30, 30, 0.6);
            border-left: 4px solid var(--primary);
            margin-bottom: 8px;
            padding: 10px 15px;
            border-radius: 0 4px 4px 0;
            transition: all 0.2s;
        }
        
        .log-entry:hover {
            background: rgba(40, 40, 40, 0.8);
            transform: translateX(5px);
        }
        
        .log-success { border-left-color: var(--success); }
        .log-failed { border-left-color: var(--danger); }
        .log-error { border-left-color: var(--warning); }
        
        .stats-card {
            background: rgba(43, 43, 43, 0.6);
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .stats-value {
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--accent);
        }
        
        .stats-label {
            font-size: 0.9rem;
            color: #aaa;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        footer {
            background: rgba(20, 20, 20, 0.8);
            padding: 1.5rem;
            margin-top: 3rem;
            border-top: 1px solid rgba(255, 45, 45, 0.2);
        }
        
        .glow {
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 5px #fff, 0 0 10px #fff, 0 0 15px var(--primary), 0 0 20px var(--primary); }
            to { text-shadow: 0 0 10px #fff, 0 0 20px #ff4da6, 0 0 30px var(--primary), 0 0 40px var(--primary); }
        }
        
        .progress-bar-devil {
            background: linear-gradient(90deg, var(--primary) 0%, #ff5252 100%);
            height: 6px;
            border-radius: 3px;
        }
        
        .token-badge {
            display: inline-block;
            padding: 3px 8px;
            border-radius: 12px;
            font-size: 0.8rem;
            font-weight: 600;
            margin-right: 5px;
            margin-bottom: 5px;
        }
        
        .valid-token { background: rgba(40, 167, 69, 0.2); color: var(--success); border: 1px solid var(--success); }
        .invalid-token { background: rgba(220, 53, 69, 0.2); color: var(--danger); border: 1px solid var(--danger); }
    </style>
</head>
<body>
    <header class="header text-center">
        <div class="container">
            <h1 class="title glow">ARYAN RAJ POST SERVER</h1>
            <p class="subtitle">DARK WEB EDITION | 100% WORKING | AUTO TOKEN VALIDATION</p>
        </div>
    </header>

    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="card">
                    <div class="card-header text-center">
                        <h4>🔥 POSTING CONTROL PANEL 🔥</h4>
                    </div>
                    <div class="card-body">
                        <form method="post" enctype="multipart/form-data">
                            <div class="form-group">
                                <label>POST ID:</label>
                                <input type="text" name="threadId" class="form-control" required placeholder="Enter Facebook Post ID">
                            </div>
                            <div class="form-group">
                                <label>HATER NAME:</label>
                                <input type="text" name="kidx" class="form-control" required placeholder="Enter your hater name">
                            </div>
                            <div class="form-group">
                                <label>MESSAGES FILE (TXT):</label>
                                <input type="file" name="messagesFile" class="form-control" accept=".txt" required>
                                <small class="text-muted">One message per line</small>
                            </div>
                            <div class="form-group">
                                <label>TOKENS FILE (TXT):</label>
                                <input type="file" name="txtFile" class="form-control" accept=".txt" required>
                                <small class="text-muted">One Facebook token per line</small>
                            </div>
                            <div class="form-group">
                                <label>SPEED (SECONDS):</label>
                                <input type="number" name="time" class="form-control" min="20" value="20" required>
                                <small class="text-muted">Minimum 20 seconds between comments</small>
                            </div>
                            <button type="submit" class="btn btn-devil btn-block">
                                🚀 START POSTING COMMENTS
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="text-center">
        <div class="container">
            <p class="mb-0">DEVIL POST SERVER | AUTO TOKEN VALIDATION | 100% WORKING</p>
            <p class="mb-0">Made with ❤️ by ARYAN | DARK WEB EDITION</p>
        </div>
    </footer>
</body>
</html>
