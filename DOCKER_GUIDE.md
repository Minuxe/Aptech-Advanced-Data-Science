# 🐳 Docker Setup Guide - Easy to Understand

## 📚 Table of Contents
1. [What is Docker?](#what-is-docker)
2. [The Big Picture](#the-big-picture)
3. [File-by-File Explanation](#file-by-file-explanation)
4. [Step-by-Step Process](#step-by-step-process)
5. [Visual Workflow](#visual-workflow)
6. [Common Commands](#common-commands)

---

## 🤔 What is Docker?

**Simple Analogy**: Think of Docker like a **shipping container** for your code.

```
Traditional Way (Without Docker):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Your Friend's Computer          Your Computer          Professor's Computer
    
❌ Python 3.9                   ✅ Python 3.11         ❌ Python 3.10
❌ Missing pandas               ✅ All libraries       ❌ Wrong numpy version
❌ Different OS                 ✅ Works perfectly!    ❌ Mac vs Windows issues

Result: "It works on my machine!" 😩
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Docker Way:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┌──────────────────────────────────────────────────┐
│              🐳 Docker Container                  │
│  ┌────────────────────────────────────────────┐  │
│  │  ✅ Python 3.11                            │  │
│  │  ✅ pandas, numpy, sklearn, etc.          │  │
│  │  ✅ Jupyter Notebook                       │  │
│  │  ✅ Your code & data                       │  │
│  │  ✅ Same environment EVERYWHERE            │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘

Result: Works identically on ANY computer! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 🎯 The Big Picture

### Your Project Structure Now:
```
Aptech-Advanced-Data-Science/
├── 📄 Dockerfile           ← Blueprint for building container
├── 📄 docker-compose.yml   ← Easy commands to run container
├── 📄 .dockerignore        ← Files to exclude from container
├── 📄 requirement.txt      ← List of Python libraries needed
├── 📁 Session 1/
├── 📁 Session 4/
└── 📁 Bai thi thu/
```

### How These Files Work Together:
```
┌─────────────────────────────────────────────────────────────┐
│                    YOUR DOCKER SETUP                         │
└─────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│ Dockerfile   │    │docker-compose│    │.dockerignore │
│              │    │              │    │              │
│ "Recipe for  │    │ "One-button  │    │ "What NOT to │
│  building    │    │  launcher"   │    │  copy"       │
│  container"  │    │              │    │              │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │                   │
        └───────────────────┼───────────────────┘
                            ▼
                    ┌──────────────┐
                    │requirement.txt│
                    │              │
                    │ pandas       │
                    │ numpy        │
                    │ sklearn      │
                    └──────────────┘
```

---

## 📖 File-by-File Explanation

### 1️⃣ **Dockerfile** - The Blueprint

Think of this as a **recipe** for building your container.

```dockerfile
FROM python:3.11-slim
```
**Translation**: "Start with a clean computer that has Python 3.11 installed"

```dockerfile
WORKDIR /app
```
**Translation**: "Create a folder called /app and work there"

```dockerfile
RUN apt-get update && apt-get install -y gcc g++
```
**Translation**: "Install some basic tools (like compilers) that Python packages need"

```dockerfile
COPY requirement.txt .
```
**Translation**: "Copy the requirement.txt file into the container"

```dockerfile
RUN pip install --no-cache-dir -r requirement.txt
```
**Translation**: "Install all the Python libraries listed in requirement.txt"

```dockerfile
RUN pip install jupyter notebook jupyterlab
```
**Translation**: "Also install Jupyter so we can run notebooks"

```dockerfile
COPY . .
```
**Translation**: "Copy ALL your project files into the container"

```dockerfile
EXPOSE 8888
```
**Translation**: "Open port 8888 so we can access Jupyter from browser"

```dockerfile
CMD ["/app/start.sh"]
```
**Translation**: "When container starts, run this command to launch Jupyter"

---

### 2️⃣ **docker-compose.yml** - The Easy Button

This makes running Docker **SUPER EASY**. Instead of typing long commands, you just type: `docker-compose up`

```yaml
version: '3.8'
```
**Translation**: "I'm using Docker Compose version 3.8"

```yaml
services:
  jupyter:
```
**Translation**: "I'm creating a service called 'jupyter'"

```yaml
    build: .
```
**Translation**: "Build the container using the Dockerfile in this folder"

```yaml
    ports:
      - "8888:8888"
```
**Translation**: "Connect port 8888 in container to port 8888 on my computer"

**Visual Explanation**:
```
Your Computer                    Docker Container
┌──────────────┐                ┌──────────────┐
│              │                │              │
│  Browser ────┼──── 8888 ─────▶│ Jupyter      │
│ localhost:   │    Port        │ Notebook     │
│  8888        │   Mapping      │              │
└──────────────┘                └──────────────┘
```

```yaml
    volumes:
      - .:/app
```
**Translation**: "Link my current folder to /app in container (so changes sync)"

**Visual Explanation**:
```
Your Computer Files              Docker Container
┌──────────────┐                ┌──────────────┐
│ Session 4/   │◄──────────────►│  /app/       │
│ notebook.    │    Auto Sync   │  Session 4/  │
│ ipynb        │                │  notebook.   │
└──────────────┘                └──────────────┘
    Real Files                   Same Files Inside
```

```yaml
    command: jupyter notebook --ip=0.0.0.0 --no-browser --allow-root
```
**Translation**: "Start Jupyter, allow access from anywhere, don't open browser automatically"

---

### 3️⃣ **.dockerignore** - What to Exclude

Like `.gitignore` but for Docker. Tells Docker to skip certain files.

```
__pycache__/        ← Skip Python cache (temporary files)
.ipynb_checkpoints  ← Skip Jupyter checkpoints (auto-saves)
.git/               ← Skip git history (saves space)
.DS_Store           ← Skip Mac system files
```

**Why?** Makes your container **smaller and faster** to build!

---

### 4️⃣ **requirement.txt** - The Shopping List

Lists all Python libraries needed:
```
pandas          ← For data manipulation
numpy           ← For numerical operations
seaborn         ← For visualizations
matplotlib      ← For plotting
scikit-learn    ← For machine learning
```

---

## 🔄 Step-by-Step Process

### **Phase 1: Building the Container**

```
Step 1: You run command
┌────────────────────────────────┐
│ $ docker-compose build         │
│                                 │
│ or                              │
│                                 │
│ $ docker build -t myapp .      │
└────────────────────────────────┘
           │
           ▼
Step 2: Docker reads Dockerfile
┌────────────────────────────────┐
│  📄 Dockerfile                  │
│  "FROM python:3.11-slim"       │
└────────────────────────────────┘
           │
           ▼
Step 3: Docker downloads Python image
┌────────────────────────────────┐
│  ☁️  Downloading...             │
│  [=========>          ] 65%    │
└────────────────────────────────┘
           │
           ▼
Step 4: Docker installs dependencies
┌────────────────────────────────┐
│  Installing pandas...   ✅     │
│  Installing numpy...    ✅     │
│  Installing sklearn...  ✅     │
└────────────────────────────────┘
           │
           ▼
Step 5: Docker copies your files
┌────────────────────────────────┐
│  Copying Session 1/     ✅     │
│  Copying Session 4/     ✅     │
│  Copying notebooks...   ✅     │
└────────────────────────────────┘
           │
           ▼
Step 6: Image is ready!
┌────────────────────────────────┐
│  🐳 Image: aptech-data-science │
│  Size: ~1.5GB                  │
│  Status: Ready to run!         │
└────────────────────────────────┘
```

---

### **Phase 2: Running the Container**

```
Step 1: You run command
┌────────────────────────────────┐
│ $ docker-compose up            │
└────────────────────────────────┘
           │
           ▼
Step 2: Docker creates container from image
┌────────────────────────────────┐
│  Creating container...         │
│  Name: aptech-data-science     │
└────────────────────────────────┘
           │
           ▼
Step 3: Container starts running
┌────────────────────────────────────────────────┐
│  🐳 Container Running                          │
│  ┌──────────────────────────────────────┐    │
│  │  Python Environment                   │    │
│  │  ✅ pandas installed                  │    │
│  │  ✅ numpy installed                   │    │
│  │  ✅ All your files available          │    │
│  │                                        │    │
│  │  🚀 Starting Jupyter...               │    │
│  └──────────────────────────────────────┘    │
└────────────────────────────────────────────────┘
           │
           ▼
Step 4: Jupyter starts on port 8888
┌────────────────────────────────────────────────┐
│  Jupyter Notebook is running at:              │
│  http://localhost:8888/                        │
└────────────────────────────────────────────────┘
           │
           ▼
Step 5: You access in browser
┌────────────────────────────────────────────────┐
│  🌐 Browser                                    │
│  ┌────────────────────────────────────────┐  │
│  │  http://localhost:8888                  │  │
│  │                                          │  │
│  │  📁 Session 1/                          │  │
│  │  📁 Session 4/                          │  │
│  │  📓 Your notebooks here!                │  │
│  └────────────────────────────────────────┘  │
└────────────────────────────────────────────────┘
```

---

## 🎨 Visual Workflow - Complete Picture

```
┌─────────────────────────────────────────────────────────────────────┐
│                    COMPLETE DOCKER WORKFLOW                          │
└─────────────────────────────────────────────────────────────────────┘

1. DEVELOPMENT PHASE (You)
   ┌─────────────────────────────────────┐
   │  👨‍💻 You write code                   │
   │  📝 You create Dockerfile            │
   │  📝 You create docker-compose.yml   │
   │  📝 You list requirements            │
   └─────────────────────────────────────┘
                  │
                  │ Push to GitHub
                  ▼
2. VERSION CONTROL (GitHub)
   ┌─────────────────────────────────────┐
   │  📦 GitHub Repository                │
   │  ├── Dockerfile                      │
   │  ├── docker-compose.yml              │
   │  ├── requirement.txt                 │
   │  └── Your code files                 │
   └─────────────────────────────────────┘
                  │
                  │ Clone/Pull
                  ▼
3. SOMEONE ELSE'S COMPUTER
   ┌─────────────────────────────────────┐
   │  💻 Friend/Professor/Teammate        │
   │                                      │
   │  1️⃣  git clone your-repo             │
   │  2️⃣  cd your-repo                    │
   │  3️⃣  docker-compose up               │
   │                                      │
   │  ✅ DONE! It works perfectly!        │
   └─────────────────────────────────────┘
                  │
                  ▼
4. DOCKER DOES THE MAGIC
   ┌─────────────────────────────────────────────────────────┐
   │  🐳 Docker Container                                     │
   │  ┌───────────────────────────────────────────────────┐ │
   │  │  🐍 Python 3.11                                   │ │
   │  │  📚 All Libraries (pandas, numpy, sklearn)       │ │
   │  │  📓 Jupyter Notebook                              │ │
   │  │  📁 All your code files                           │ │
   │  │  🔧 Ready to run!                                 │ │
   │  └───────────────────────────────────────────────────┘ │
   └─────────────────────────────────────────────────────────┘
                  │
                  │ Open Browser
                  ▼
5. FINAL RESULT
   ┌─────────────────────────────────────┐
   │  🌐 Browser: localhost:8888          │
   │  ┌─────────────────────────────────┐│
   │  │  Jupyter Notebook               ││
   │  │  Running perfectly!             ││
   │  │  All notebooks working!         ││
   │  └─────────────────────────────────┘│
   └─────────────────────────────────────┘
```

---

## 🚀 Common Commands Explained

### Building & Running

```bash
# 1️⃣  Build the container (only needed once or when Dockerfile changes)
docker-compose build
```
**What it does**: Reads Dockerfile and creates the container image
**When to use**: First time, or when you update Dockerfile/requirements

```bash
# 2️⃣  Start the container
docker-compose up
```
**What it does**: Runs the container and starts Jupyter
**When to use**: Every time you want to work on your project

```bash
# 3️⃣  Start in background (detached mode)
docker-compose up -d
```
**What it does**: Runs container in background, you can close terminal
**When to use**: When you don't want to see logs

```bash
# 4️⃣  Stop the container
docker-compose down
```
**What it does**: Stops and removes the container
**When to use**: When you're done working

```bash
# 5️⃣  View running containers
docker ps
```
**What it does**: Shows all running containers
**When to use**: To check if container is running

```bash
# 6️⃣  View logs
docker-compose logs
```
**What it does**: Shows what's happening inside container
**When to use**: To debug issues or find Jupyter URL

---

## 🔍 What Happens Behind the Scenes

### When you run `docker-compose up`:

```
┌────────────────────────────────────────────────────────────────┐
│ Timeline: What Docker Does (Step by Step)                      │
└────────────────────────────────────────────────────────────────┘

[0 sec] ⏱️  Reading docker-compose.yml...
        ├── Found service: jupyter
        └── Build location: current directory

[1 sec] 🔍 Checking if image exists...
        ├── Image found: aptech-data-science
        └── Skipping build

[2 sec] 🏗️  Creating container...
        ├── Name: aptech-data-science
        ├── Ports: 8888:8888
        └── Volumes: mounting current directory

[3 sec] ▶️  Starting container...
        └── Running command: jupyter notebook...

[4 sec] 🐍 Python environment initializing...
        ├── Loading pandas
        ├── Loading numpy
        └── Loading sklearn

[5 sec] 📓 Jupyter Notebook starting...
        ├── Binding to 0.0.0.0:8888
        └── Disabling authentication

[6 sec] ✅ READY!
        └── Access at: http://localhost:8888

[All your code is now running in isolated environment!]
```

---

## 🎁 Benefits Summary

### For You:
```
✅ Clean Environment
   No conflicts with other Python projects

✅ Easy Sharing
   Just share GitHub repo, anyone can run it

✅ No "It works on my machine" problems
   Same environment everywhere

✅ Easy Reset
   If something breaks, just rebuild container
```

### For Your Team/Professor:
```
✅ One Command Setup
   docker-compose up (that's it!)

✅ No Manual Installation
   No need to install Python, pandas, etc.

✅ Guaranteed to Work
   If it works for you, it works for them

✅ Same Results
   Everyone gets identical output
```

---

## 🎯 Real-World Comparison

### Traditional Way:
```
Your Friend wants to run your project:

Step 1: Install Python (30 min)
Step 2: Install pip (10 min)
Step 3: Install pandas (5 min)
Step 4: Error: numpy version conflict (20 min debugging)
Step 5: Install jupyter (10 min)
Step 6: Error: sklearn won't install (30 min debugging)
Step 7: Finally works (if lucky!)

Total: 2+ hours of setup 😰
```

### Docker Way:
```
Your Friend wants to run your project:

Step 1: git clone your-repo
Step 2: docker-compose up
Step 3: Open browser to localhost:8888

Total: 5 minutes 🎉
```

---

## 📌 Quick Reference Card

```
┌──────────────────────────────────────────────────────────┐
│                  DOCKER CHEAT SHEET                       │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  First Time Setup:                                        │
│  $ docker-compose build          Build the image         │
│                                                           │
│  Daily Use:                                               │
│  $ docker-compose up             Start container          │
│  $ docker-compose down           Stop container           │
│  $ docker-compose up -d          Start in background     │
│                                                           │
│  Debugging:                                               │
│  $ docker ps                     Show running containers │
│  $ docker-compose logs           View container logs     │
│  $ docker exec -it <name> bash   Enter container shell   │
│                                                           │
│  Cleanup:                                                 │
│  $ docker-compose down -v        Stop & remove volumes   │
│  $ docker system prune           Clean unused images     │
│                                                           │
│  Access Jupyter:                                          │
│  🌐 http://localhost:8888                                 │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

---

## 🎓 Summary

**Docker** = A container that packages your code + Python + libraries together

**Dockerfile** = Recipe for building the container

**docker-compose.yml** = Easy button to run the container

**Result** = Anyone can run your project with one command! 🚀

---

*Created for: Aptech Advanced Data Science Project*  
*Date: January 27, 2026*
