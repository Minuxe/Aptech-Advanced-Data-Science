# 🐳 Docker Setup Guide - Easy to Understand

## 📚 Table of Contents
1. [What is Docker?](#what-is-docker)
2. [The Big Picture](#the-big-picture)
3. [File-by-File Explanation](#file-by-file-explanation)
4. [Step-by-Step Process](#step-by-step-process)
5. [Visual Workflow](#visual-workflow)
6. [Common Commands](#common-commands)
7. [🚀 NEW: CI/CD with GitHub Actions & Docker Hub](#cicd-with-github-actions--docker-hub)
8. [Complete Setup Guide](#complete-setup-guide)

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

## 🚀 CI/CD with GitHub Actions & Docker Hub

### 🎯 What is CI/CD?

**CI/CD** = **Continuous Integration / Continuous Deployment**

**Simple Analogy**: Think of it as a **robot assistant** that automatically builds and delivers your project!

```
WITHOUT CI/CD (Manual Way):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. You write code                     (5 min)
2. You build Docker image manually    (3 min)
3. You test the image                 (5 min)
4. You push to Docker Hub manually    (2 min)
5. You tell everyone to update        (5 min)
6. Someone has issues, repeat...      (30+ min)

Total: 50+ minutes of tedious work 😩
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WITH CI/CD (Automated Way):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. You write code                     (5 min)
2. You: git push                      (10 sec)
3. Robot does everything else! 🤖     
   ✅ Builds image
   ✅ Tests it
   ✅ Pushes to Docker Hub
   ✅ Notifies you when done

Total: 5 minutes of YOUR time! 🎉
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 🌍 The Complete Ecosystem

```
┌────────────────────────────────────────────────────────────────────┐
│                    YOUR DEVELOPMENT ECOSYSTEM                       │
└────────────────────────────────────────────────────────────────────┘

YOUR COMPUTER                 GITHUB                    DOCKER HUB
┌──────────────┐             ┌──────────────┐         ┌──────────────┐
│              │             │              │         │              │
│  💻 Code     │   git push  │  📦 Repo     │  auto   │  🐳 Images   │
│  Editor      │────────────▶│  Storage     │────────▶│  Registry    │
│              │             │              │  build  │              │
│  Local Dev   │             │  🤖 Actions  │  push   │  Public      │
│              │             │  Automation  │         │  Download    │
└──────────────┘             └──────────────┘         └──────────────┘
                                    │                        │
                                    │                        │
                                    ▼                        ▼
                            ┌──────────────┐         ┌──────────────┐
                            │  Build Logs  │         │ Image Ready! │
                            │  Test Results│         │ Anyone can   │
                            │  Notifications│        │ pull & run   │
                            └──────────────┘         └──────────────┘
```

---

### 📁 New Files Created

```
Aptech-Advanced-Data-Science/
├── 📁 .github/
│   └── 📁 workflows/
│       └── 📄 docker-publish.yml    ← 🆕 GitHub Actions Workflow
├── 📄 Dockerfile
├── 📄 docker-compose.yml            ← Updated with Docker Hub option
├── 📄 README.md                     ← Updated with instructions
└── 📄 DOCKER_GUIDE.md               ← This file (updated)
```

---

### 🔍 Understanding GitHub Actions Workflow

Let's break down the **[.github/workflows/docker-publish.yml](.github/workflows/docker-publish.yml)** file:

#### **Part 1: When to Run (Trigger)**

```yaml
on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  workflow_dispatch:
```

**Translation**:
- Run when you push to `main` or `master` branch
- Run when someone creates a pull request
- `workflow_dispatch`: Allow manual trigger from GitHub UI

**Visual**:
```
YOU                           GITHUB ACTIONS
┌──────────────┐             ┌──────────────┐
│              │             │              │
│  git push    │────────────▶│  🚨 TRIGGER! │
│  origin main │             │  Start build │
│              │             │              │
└──────────────┘             └──────────────┘
```

---

#### **Part 2: The Build Job**

```yaml
jobs:
  build-and-push:
    runs-on: ubuntu-latest
```

**Translation**: Create a virtual Ubuntu computer in the cloud to do the work

---

#### **Part 3: Step-by-Step Actions**

```yaml
steps:
- name: Checkout code
  uses: actions/checkout@v3
```

**Translation**: Download all your code from GitHub

**Visual**:
```
GITHUB REPO                  VIRTUAL MACHINE
┌──────────────┐             ┌──────────────┐
│  Your Code   │   Download  │  Empty       │
│  All Files   │────────────▶│  Machine     │
│  📁📄📓      │             │  Now has     │
│              │             │  📁📄📓      │
└──────────────┘             └──────────────┘
```

---

```yaml
- name: Set up Docker Buildx
  uses: docker/setup-buildx-action@v2
```

**Translation**: Install Docker tools with advanced features (faster builds, caching)

---

```yaml
- name: Log in to Docker Hub
  uses: docker/login-action@v2
  with:
    username: ${{ secrets.DOCKER_USERNAME }}
    password: ${{ secrets.DOCKER_PASSWORD }}
```

**Translation**: Login to Docker Hub using secret credentials stored in GitHub

**Visual**:
```
GITHUB SECRETS               DOCKER HUB
┌──────────────┐             ┌──────────────┐
│ 🔐 Encrypted │             │              │
│ DOCKER_      │   Login     │  ✅ Access   │
│ USERNAME     │────────────▶│  Granted     │
│ DOCKER_      │             │              │
│ PASSWORD     │             │              │
└──────────────┘             └──────────────┘
```

**Why secrets?** 
- Never expose passwords in code
- GitHub encrypts them
- Only accessible during build

---

```yaml
- name: Extract metadata (tags, labels)
  id: meta
  uses: docker/metadata-action@v4
  with:
    images: ${{ secrets.DOCKER_USERNAME }}/aptech-data-science
    tags: |
      type=ref,event=branch
      type=sha
      type=raw,value=latest,enable={{is_default_branch}}
```

**Translation**: Create smart tags for your image

**What are tags?**
```
Image without tag:
your-username/aptech-data-science

Image with tags:
your-username/aptech-data-science:latest       ← Most recent
your-username/aptech-data-science:main         ← From main branch
your-username/aptech-data-science:sha-abc123   ← Specific version
```

**Why multiple tags?**
```
User wants:          They use:
├─ Latest version    → :latest
├─ Stable version    → :main
└─ Specific version  → :sha-abc123
```

---

```yaml
- name: Build and push Docker image
  uses: docker/build-push-action@v4
  with:
    context: .
    push: true
    tags: ${{ steps.meta.outputs.tags }}
    labels: ${{ steps.meta.outputs.labels }}
    cache-from: type=registry,ref=.../buildcache
    cache-to: type=registry,ref=.../buildcache,mode=max
```

**Translation**: Build the Docker image and push it to Docker Hub with caching

**What is caching?**
```
First Build (No Cache):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Install Python       [====] 2 min
Install pandas       [====] 1 min
Install numpy        [====] 1 min
Install sklearn      [====] 2 min
Copy files           [==  ] 30 sec
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: 6.5 minutes

Second Build (With Cache):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Install Python       [✓] Cached!
Install pandas       [✓] Cached!
Install numpy        [✓] Cached!
Install sklearn      [✓] Cached!
Copy files           [==  ] 30 sec
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Total: 30 seconds! 🚀
```

---

## 📋 Complete Setup Guide

### 🎯 STEP 1: Create Docker Hub Account

**What is Docker Hub?**
Think of it as **GitHub for Docker images** - a place to store and share your containers!

```
┌─────────────────────────────────────────────────────────┐
│  DOCKER HUB (hub.docker.com)                            │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Your Repositories:                               │  │
│  │  ┌─────────────────────────────────────────────┐ │  │
│  │  │ 🐳 aptech-data-science         Public  ✅   │ │  │
│  │  │    Latest: 1 hour ago                        │ │  │
│  │  │    Downloads: 15                             │ │  │
│  │  │    Tags: latest, main, sha-abc123           │ │  │
│  │  └─────────────────────────────────────────────┘ │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**Action Items:**
1. Go to https://hub.docker.com/
2. Click "Sign Up"
3. Choose a username (e.g., `johndoe`)
4. Verify your email
5. ✅ Done!

---

### 🎯 STEP 2: Generate Docker Hub Access Token

**Why access token instead of password?**
- ✅ More secure (can be revoked anytime)
- ✅ Limited permissions
- ✅ Doesn't expose your main password

**Action Items:**

```
Step 1: Login to Docker Hub
   └─▶ https://hub.docker.com/

Step 2: Click your profile (top right)
   └─▶ Account Settings

Step 3: Click "Security" in left menu
   └─▶ You'll see "Access Tokens" section

Step 4: Click "New Access Token"
   ┌────────────────────────────────────────┐
   │ Description: github-actions            │
   │ Access permissions: Read, Write, Delete│
   │                                        │
   │         [Create Access Token]          │
   └────────────────────────────────────────┘

Step 5: COPY THE TOKEN! ⚠️
   ┌────────────────────────────────────────┐
   │ dckr_pat_ABcd1234EFgh5678IJ...        │
   │                                        │
   │ ⚠️  This is the ONLY time you'll      │
   │    see this token. Copy it now!       │
   │                                        │
   │         [Copy]    [Close]              │
   └────────────────────────────────────────┘

Step 6: Save it somewhere temporarily
   └─▶ You'll need it in the next step!
```

**Visual Flow:**
```
Profile Icon → Account Settings → Security → New Access Token
     👤             ⚙️                🔐           ➕
                                                   ↓
                                            Copy Token! 📋
                                            (Only shown once)
```

---

### 🎯 STEP 3: Add Secrets to GitHub

**What are GitHub Secrets?**
- 🔒 Encrypted storage for sensitive data
- ♾️  Never exposed in logs or code
- 🤖 Only accessible by GitHub Actions

**Action Items:**

```
Step 1: Go to your GitHub repository
   └─▶ https://github.com/YOUR-USERNAME/Aptech-Advanced-Data-Science

Step 2: Click "Settings" tab
   ┌─────────────────────────────────────────────────┐
   │ < > Code  Issues  Pull requests  Actions  ⚙️ Settings │
   └─────────────────────────────────────────────────┘

Step 3: In left sidebar → "Secrets and variables" → "Actions"
   Left Menu:
   ├─ General
   ├─ Branches
   ├─ 🔐 Secrets and variables
   │   └─ Actions  ← Click here!
   └─ ...

Step 4: Click "New repository secret"
   ┌────────────────────────────────────────┐
   │  Repository secrets                     │
   │                                        │
   │  [New repository secret]               │
   └────────────────────────────────────────┘

Step 5: Add FIRST secret
   ┌────────────────────────────────────────┐
   │ Name*                                  │
   │ DOCKER_USERNAME                        │
   │                                        │
   │ Secret*                                │
   │ your-dockerhub-username                │
   │                                        │
   │         [Add secret]                   │
   └────────────────────────────────────────┘

Step 6: Click "New repository secret" AGAIN

Step 7: Add SECOND secret
   ┌────────────────────────────────────────┐
   │ Name*                                  │
   │ DOCKER_PASSWORD                        │
   │                                        │
   │ Secret*                                │
   │ dckr_pat_ABcd1234EFgh5678IJ...        │
   │ (paste the token from Step 2)         │
   │                                        │
   │         [Add secret]                   │
   └────────────────────────────────────────┘

Step 8: Verify both secrets exist
   ┌────────────────────────────────────────┐
   │  Repository secrets                     │
   │  ┌──────────────────────────────────┐  │
   │  │ DOCKER_USERNAME    Updated 1m ago│  │
   │  │ DOCKER_PASSWORD    Updated 1m ago│  │
   │  └──────────────────────────────────┘  │
   └────────────────────────────────────────┘
```

**Visual Diagram:**
```
GitHub Repository
    └─ Settings ⚙️
        └─ Secrets and variables 🔐
            └─ Actions
                ├─ DOCKER_USERNAME ✅
                └─ DOCKER_PASSWORD ✅
                    ↓
                These are now available to GitHub Actions!
```

---

### 🎯 STEP 4: Push Workflow File to GitHub

The workflow file is already created at [.github/workflows/docker-publish.yml](.github/workflows/docker-publish.yml)

**Action Items:**

```bash
# 1. Check if file exists
ls -la .github/workflows/docker-publish.yml

# 2. Add all files to git
git add .

# 3. Commit with message
git commit -m "Add GitHub Actions workflow for Docker Hub"

# 4. Push to GitHub
git push origin main
```

**What happens next:**
```
┌────────────────────────────────────────────────────────────┐
│ YOU: git push origin main                                  │
└──────────────────┬─────────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────────┐
│ GITHUB: Receives your push                                 │
│  ┌──────────────────────────────────────────────────────┐ │
│  │ New commit detected on 'main' branch                  │ │
│  │ Found: .github/workflows/docker-publish.yml           │ │
│  │ 🚨 TRIGGERING WORKFLOW!                               │ │
│  └──────────────────────────────────────────────────────┘ │
└──────────────────┬─────────────────────────────────────────┘
                   │
                   ▼
┌────────────────────────────────────────────────────────────┐
│ GITHUB ACTIONS: Starting build                             │
│  [0:00] ✅ Checkout code                                   │
│  [0:30] ✅ Set up Docker                                   │
│  [0:45] ✅ Login to Docker Hub                             │
│  [1:00] 🔨 Building image...                               │
│  [4:00] 📦 Pushing to Docker Hub...                        │
│  [5:00] ✅ COMPLETE!                                       │
└────────────────────────────────────────────────────────────┘
```

---

### 🎯 STEP 5: Watch the Magic Happen!

**View Build Progress:**

```
Step 1: Go to your GitHub repository

Step 2: Click "Actions" tab
   ┌─────────────────────────────────────────────────┐
   │ < > Code  Issues  🎬 Actions  Pull requests     │
   └─────────────────────────────────────────────────┘

Step 3: See your workflow running
   ┌────────────────────────────────────────────────┐
   │  All workflows                                 │
   │  ┌──────────────────────────────────────────┐ │
   │  │ 🟡 Build and Push Docker Image            │ │
   │  │    main  #1  Running...                  │ │
   │  │    Started 30s ago                       │ │
   │  └──────────────────────────────────────────┘ │
   └────────────────────────────────────────────────┘

Step 4: Click on the workflow to see details
   ┌────────────────────────────────────────────────┐
   │ build-and-push                                 │
   │ ┌────────────────────────────────────────────┐│
   │ │ ✅ Checkout code                 (5s)      ││
   │ │ ✅ Set up Docker Buildx          (15s)     ││
   │ │ ✅ Log in to Docker Hub          (3s)      ││
   │ │ ✅ Extract metadata              (2s)      ││
   │ │ 🔄 Build and push Docker image  (Running)  ││
   │ └────────────────────────────────────────────┘│
   └────────────────────────────────────────────────┘

Step 5: Wait for green checkmark ✅
   ┌────────────────────────────────────────────────┐
   │  All workflows                                 │
   │  ┌──────────────────────────────────────────┐ │
   │  │ ✅ Build and Push Docker Image            │ │
   │  │    main  #1  Success!                    │ │
   │  │    Completed in 5m 23s                   │ │
   │  └──────────────────────────────────────────┘ │
   └────────────────────────────────────────────────┘
```

---

### 🎯 STEP 6: Verify on Docker Hub

```
Step 1: Go to Docker Hub
   └─▶ https://hub.docker.com/

Step 2: Login and go to your repositories

Step 3: Find your image
   ┌────────────────────────────────────────────────┐
   │ 🐳 your-username/aptech-data-science           │
   │                                                │
   │ Public  ●  Updated 2 minutes ago               │
   │                                                │
   │ Tags:                                          │
   │ ├─ latest          1.45GB    2 min ago        │
   │ ├─ main            1.45GB    2 min ago        │
   │ └─ sha-abc1234     1.45GB    2 min ago        │
   │                                                │
   │ Pull command:                                  │
   │ docker pull your-username/aptech-data-science  │
   └────────────────────────────────────────────────┘
```

**Congratulations! 🎉 Your image is now publicly available!**

---

## 🎬 Complete Workflow Visualization

### The Full Journey: From Code to Worldwide Access

```
═══════════════════════════════════════════════════════════════════════
                        THE COMPLETE CI/CD PIPELINE
═══════════════════════════════════════════════════════════════════════

PHASE 1: LOCAL DEVELOPMENT (Your Computer)
┌─────────────────────────────────────────────────────────────────────┐
│  👨‍💻 YOU                                                              │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ 1. Write code in notebook                                     │  │
│  │    - Add new ML models                                        │  │
│  │    - Fix bugs                                                 │  │
│  │    - Update documentation                                     │  │
│  │                                                               │  │
│  │ 2. Test locally with Docker                                   │  │
│  │    $ docker-compose up                                        │  │
│  │    ✅ Works perfectly!                                        │  │
│  │                                                               │  │
│  │ 3. Commit and push                                            │  │
│  │    $ git add .                                                │  │
│  │    $ git commit -m "Add new feature"                          │  │
│  │    $ git push origin main                                     │  │
│  └───────────────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────────────┘
                       │ Internet ☁️
                       ▼
PHASE 2: VERSION CONTROL (GitHub)
┌─────────────────────────────────────────────────────────────────────┐
│  📦 GITHUB REPOSITORY                                               │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Repository: Aptech-Advanced-Data-Science                      │  │
│  │ ├── 📄 Session 4/Tran_Dai_Minh_Session_4_.ipynb              │  │
│  │ ├── 📄 Dockerfile                                             │  │
│  │ ├── 📄 docker-compose.yml                                     │  │
│  │ ├── 📄 requirement.txt                                        │  │
│  │ └── 📁 .github/workflows/docker-publish.yml                   │  │
│  │                                                               │  │
│  │ 🔔 NEW COMMIT DETECTED!                                       │  │
│  │    Author: You                                                │  │
│  │    Branch: main                                               │  │
│  │    Message: "Add new feature"                                 │  │
│  │                                                               │  │
│  │ 🚨 TRIGGERING: docker-publish.yml                             │  │
│  └───────────────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────────────┘
                       │
                       ▼
PHASE 3: AUTOMATION (GitHub Actions)
┌─────────────────────────────────────────────────────────────────────┐
│  🤖 GITHUB ACTIONS (Virtual Machine in the Cloud)                   │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ [00:00] 🚀 Workflow Started                                   │  │
│  │         Job: build-and-push                                   │  │
│  │         OS: Ubuntu Latest                                     │  │
│  │                                                               │  │
│  │ [00:05] ✅ Checkout code                                      │  │
│  │         Downloading repository...                             │  │
│  │         ├─ Dockerfile ✓                                       │  │
│  │         ├─ requirement.txt ✓                                  │  │
│  │         └─ All notebooks ✓                                    │  │
│  │                                                               │  │
│  │ [00:20] ✅ Set up Docker Buildx                               │  │
│  │         Installing Docker tools...                            │  │
│  │         Docker version: 24.0.7 ✓                              │  │
│  │                                                               │  │
│  │ [00:35] ✅ Log in to Docker Hub                               │  │
│  │         Using secrets:                                        │  │
│  │         ├─ DOCKER_USERNAME: ******* ✓                         │  │
│  │         └─ DOCKER_PASSWORD: ******* ✓                         │  │
│  │         Login successful!                                     │  │
│  │                                                               │  │
│  │ [00:45] ✅ Extract metadata                                   │  │
│  │         Creating tags:                                        │  │
│  │         ├─ your-username/aptech-data-science:latest           │  │
│  │         ├─ your-username/aptech-data-science:main             │  │
│  │         └─ your-username/aptech-data-science:sha-abc1234      │  │
│  │                                                               │  │
│  │ [01:00] 🔨 Build Docker image                                 │  │
│  │         Step 1/8: FROM python:3.11-slim                       │  │
│  │         Step 2/8: WORKDIR /app                                │  │
│  │         Step 3/8: Installing system dependencies...           │  │
│  │         Step 4/8: COPY requirement.txt                        │  │
│  │         Step 5/8: Installing Python packages...               │  │
│  │                  ├─ pandas ✓                                  │  │
│  │                  ├─ numpy ✓                                   │  │
│  │                  ├─ scikit-learn ✓                            │  │
│  │                  └─ [Using cache for unchanged layers]        │  │
│  │         Step 6/8: Installing Jupyter ✓                        │  │
│  │         Step 7/8: COPY project files ✓                        │  │
│  │         Step 8/8: Setting up startup script ✓                 │  │
│  │         Build complete! Size: 1.45GB                          │  │
│  │                                                               │  │
│  │ [04:30] ⬆️  Pushing to Docker Hub                             │  │
│  │         Pushing layer 1/12: [========>   ] 65%               │  │
│  │         Pushing layer 2/12: [===========>] 98%               │  │
│  │         ...                                                   │  │
│  │         All layers pushed successfully!                       │  │
│  │                                                               │  │
│  │ [05:23] ✅ WORKFLOW COMPLETE!                                 │  │
│  │         Status: Success ✓                                     │  │
│  │         Duration: 5m 23s                                      │  │
│  │         Image published:                                      │  │
│  │         └─ docker.io/your-username/aptech-data-science        │  │
│  └───────────────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────────────┘
                       │
                       ▼
PHASE 4: PUBLIC REGISTRY (Docker Hub)
┌─────────────────────────────────────────────────────────────────────┐
│  🐳 DOCKER HUB (hub.docker.com)                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │ Repository: your-username/aptech-data-science                 │  │
│  │ Visibility: Public 🌍                                         │  │
│  │                                                               │  │
│  │ 📦 Image Details:                                             │  │
│  │ ├─ Size: 1.45 GB                                              │  │
│  │ ├─ Last Updated: 2 minutes ago                                │  │
│  │ ├─ Downloads: 0 → 1 → 5 → 15... (growing!)                   │  │
│  │                                                               │  │
│  │ 🏷️  Available Tags:                                           │  │
│  │ ├─ latest      (most recent)                                  │  │
│  │ ├─ main        (from main branch)                             │  │
│  │ └─ sha-abc1234 (specific commit)                              │  │
│  │                                                               │  │
│  │ 📋 Pull Command:                                              │  │
│  │    docker pull your-username/aptech-data-science:latest       │  │
│  └───────────────────────────────────────────────────────────────┘  │
└──────────────────────┬──────────────────────────────────────────────┘
                       │
                       │ Anyone in the world can now...
                       │
        ┌──────────────┴──────────────┬─────────────────┐
        │                             │                 │
        ▼                             ▼                 ▼
PHASE 5: END USERS (Worldwide)
┌────────────────┐        ┌────────────────┐      ┌────────────────┐
│ 👨‍🎓 STUDENT     │        │ 👨‍🏫 PROFESSOR   │      │ 👨‍💻 COLLABORATOR│
├────────────────┤        ├────────────────┤      ├────────────────┤
│ No Python      │        │ Teaching       │      │ Contributing   │
│ No packages    │        │ Demo           │      │ Code review    │
│                │        │                │      │                │
│ Just runs:     │        │ Just runs:     │      │ Just runs:     │
│ docker pull    │        │ docker pull    │      │ docker pull    │
│ docker run     │        │ docker run     │      │ docker run     │
│                │        │                │      │                │
│ ✅ Works!      │        │ ✅ Works!      │      │ ✅ Works!      │
└────────────────┘        └────────────────┘      └────────────────┘

═══════════════════════════════════════════════════════════════════════
                    TOTAL TIME: 5-10 MINUTES (AUTOMATED)
                    YOUR TIME: 30 SECONDS (git push)
═══════════════════════════════════════════════════════════════════════
```

---

## 🔄 Daily Workflow After Setup

```
┌─────────────────────────────────────────────────────────────────────┐
│                     YOUR TYPICAL DAY                                 │
└─────────────────────────────────────────────────────────────────────┘

MORNING: Start working
┌──────────────────────────┐
│ $ docker-compose up      │  ← Start local environment
└────────┬─────────────────┘
         │
         ▼
    Work on code
    Make changes
    Test locally
         │
         ▼
AFTERNOON: Push updates
┌──────────────────────────┐
│ $ git add .              │
│ $ git commit -m "..."    │
│ $ git push origin main   │  ← Trigger automation
└────────┬─────────────────┘
         │
         ▼
    ☕ Take a coffee break
    GitHub Actions builds automatically
         │
         ▼
5 MINUTES LATER: Check email
┌──────────────────────────────────────────────┐
│ ✅ GitHub Actions: Build successful           │
│    Your image is live on Docker Hub!         │
└──────────────────────────────────────────────┘
         │
         ▼
    Tell your team:
    "New version available!
     docker pull your-username/aptech-data-science:latest"
         │
         ▼
EVENING: Go home
    Everything is automated!
    No manual deployment needed!
    Sleep well knowing CI/CD has your back! 😴
```

---

## ⚙️ Advanced: Understanding the Build Process

### What Happens During Build (Technical Deep Dive)

```
LAYER-BY-LAYER BUILD PROCESS
═══════════════════════════════════════════════════════════════

Layer 1: Base Image
┌────────────────────────────────────────────────────────┐
│ FROM python:3.11-slim                                  │
│                                                        │
│ What it contains:                                      │
│ ├─ Debian Linux (minimal)          ~120 MB            │
│ ├─ Python 3.11                      ~50 MB             │
│ └─ Basic system libraries           ~30 MB             │
│                                                        │
│ Total: ~200 MB                                         │
│ Status: ✅ Cached (unchanged)                          │
└────────────────────────────────────────────────────────┘

Layer 2: System Dependencies
┌────────────────────────────────────────────────────────┐
│ RUN apt-get update && apt-get install -y gcc g++      │
│                                                        │
│ What it installs:                                      │
│ ├─ gcc (C compiler)                 ~50 MB             │
│ ├─ g++ (C++ compiler)               ~30 MB             │
│ └─ Build tools                      ~20 MB             │
│                                                        │
│ Total: +100 MB                                         │
│ Status: ✅ Cached (unchanged)                          │
└────────────────────────────────────────────────────────┘

Layer 3: Copy Requirements
┌────────────────────────────────────────────────────────┐
│ COPY requirement.txt .                                 │
│                                                        │
│ What it does:                                          │
│ └─ Copies requirement.txt into image    ~1 KB          │
│                                                        │
│ Total: +1 KB                                           │
│ Status: ✅ Cached (unchanged)                          │
└────────────────────────────────────────────────────────┘

Layer 4: Install Python Packages
┌────────────────────────────────────────────────────────┐
│ RUN pip install -r requirement.txt                     │
│                                                        │
│ What it installs:                                      │
│ ├─ pandas                           ~80 MB             │
│ ├─ numpy                            ~50 MB             │
│ ├─ scikit-learn                     ~200 MB            │
│ ├─ matplotlib                       ~100 MB            │
│ ├─ seaborn                          ~10 MB             │
│ └─ Dependencies                     ~300 MB            │
│                                                        │
│ Total: +740 MB                                         │
│ Status: ✅ Cached (unchanged)                          │
└────────────────────────────────────────────────────────┘

Layer 5: Install Jupyter
┌────────────────────────────────────────────────────────┐
│ RUN pip install jupyter notebook jupyterlab           │
│                                                        │
│ What it installs:                                      │
│ ├─ Jupyter Notebook                 ~50 MB             │
│ ├─ JupyterLab                       ~80 MB             │
│ └─ Dependencies                     ~70 MB             │
│                                                        │
│ Total: +200 MB                                         │
│ Status: ✅ Cached (unchanged)                          │
└────────────────────────────────────────────────────────┘

Layer 6: Copy Project Files
┌────────────────────────────────────────────────────────┐
│ COPY . .                                               │
│                                                        │
│ What it copies:                                        │
│ ├─ Session 1/                       ~5 MB              │
│ ├─ Session 4/                       ~10 MB             │
│ ├─ Bai thi thu/                     ~50 MB             │
│ └─ Other files                      ~5 MB              │
│                                                        │
│ Total: +70 MB                                          │
│ Status: 🔄 REBUILDING (you changed code!)             │
└────────────────────────────────────────────────────────┘

Layer 7: Setup Script
┌────────────────────────────────────────────────────────┐
│ RUN echo '#!/bin/bash...' > start.sh                   │
│                                                        │
│ Total: +1 KB                                           │
│ Status: 🔄 REBUILDING (depends on Layer 6)            │
└────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════

SUMMARY:
├─ Total Image Size: ~1.45 GB
├─ Cached Layers: 5/7 (Layers 1-5)
├─ Rebuilt Layers: 2/7 (Layers 6-7)
└─ Build Time: ~30 seconds (thanks to caching!)

If no cache: ~6 minutes
With cache: ~30 seconds
Speed improvement: 12x faster! 🚀
```

---

## 🎓 Summary

**What You've Accomplished:**

1. ✅ **Created Dockerfile** - Recipe for your environment
2. ✅ **Created docker-compose.yml** - Easy run command
3. ✅ **Created GitHub Actions workflow** - Automatic builds
4. ✅ **Set up Docker Hub** - Public image storage
5. ✅ **Connected everything** - Full CI/CD pipeline

**The Magic Formula:**

```
git push
    ↓
GitHub Actions (automatic)
    ↓
Docker Hub (automatic)
    ↓
Anyone can use (docker pull)
```

**Benefits:**

- 🚀 **Automatic** - No manual deployment
- 🌍 **Worldwide** - Anyone can pull your image
- ⚡ **Fast** - Caching makes rebuilds quick
- 🔒 **Secure** - Secrets encrypted in GitHub
- 📦 **Versioned** - Multiple tags for different versions
- 🎯 **Professional** - Industry-standard CI/CD

---

*Created for: Aptech Advanced Data Science Project*  
*Updated: January 28, 2026*
*With CI/CD Pipeline*
*Date: January 27, 2026*
