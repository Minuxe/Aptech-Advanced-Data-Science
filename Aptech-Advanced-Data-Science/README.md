# 🎓 Aptech Advanced Data Science

A comprehensive data science project with Decision Trees, Gradient Boosting, and automated Docker deployment.

## 🚀 Quick Start

### Option 1: Using Pre-built Image from Docker Hub (Fastest) ⚡

Once the image is published to Docker Hub:

```bash
# Pull the latest image
docker pull YOUR-DOCKERHUB-USERNAME/aptech-data-science:latest

# Run the container
docker run -p 8888:8888 -v $(pwd):/app YOUR-DOCKERHUB-USERNAME/aptech-data-science:latest

# Access Jupyter at: http://localhost:8888
```

### Option 2: Using Docker Compose (Recommended) 🐳

```bash
# Clone the repository
git clone https://github.com/YOUR-GITHUB-USERNAME/Aptech-Advanced-Data-Science.git
cd Aptech-Advanced-Data-Science

# Start the container
docker-compose up

# Access Jupyter at: http://localhost:8888
```

### Option 3: Build from Source 🔨

```bash
# Clone and build locally
git clone https://github.com/YOUR-GITHUB-USERNAME/Aptech-Advanced-Data-Science.git
cd Aptech-Advanced-Data-Science
docker-compose up --build
```

---

## 📦 What's Inside

### Libraries & Tools
- **Python 3.11** - Latest stable version
- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **seaborn & matplotlib** - Data visualization
- **scikit-learn** - Machine learning
- **Jupyter Notebook/Lab** - Interactive development

### Project Contents
- 📓 **Session 4**: Decision Trees & Gradient Boosting
  - Fruit Classification (ID3 Algorithm)
  - Car Price Prediction (Gradient Boosting)
  - Feature Importance Analysis
- 📁 Multiple sessions with various ML projects
- 📊 Datasets included

---

## 🔄 Automated CI/CD Pipeline

Every push to `main` or `master` branch automatically:

```
You Push Code → GitHub Actions Triggers → Build Docker Image → Push to Docker Hub
     ✍️               🤖                        🔨                    ☁️
```

### What Happens Automatically:
1. ✅ Detects code changes
2. ✅ Builds fresh Docker image
3. ✅ Runs in isolated environment
4. ✅ Pushes to Docker Hub
5. ✅ Available worldwide instantly

Check build status: `https://github.com/YOUR-USERNAME/YOUR-REPO/actions`

---

## 🛠️ For Developers

### Making Changes

```bash
# 1. Make your code changes
# Edit notebooks, add files, etc.

# 2. Commit and push
git add .
git commit -m "Add new feature"
git push origin main

# 3. Sit back! GitHub Actions will:
#    - Build the image
#    - Push to Docker Hub
#    - Make it available to everyone
```

### Local Development

```bash
# Run with live code sync
docker-compose up

# Your local changes appear in container instantly!
# No need to rebuild for code changes
```

### Updating Dependencies

```bash
# 1. Edit requirement.txt
# Add new library, e.g., "tensorflow"

# 2. Rebuild container
docker-compose up --build

# 3. Push to GitHub
git add requirement.txt
git commit -m "Add tensorflow"
git push origin main
# GitHub Actions will rebuild automatically
```

---

## 📚 Documentation

- **[Docker Setup Guide](DOCKER_GUIDE.md)** - Complete Docker tutorial with visualizations
- **[GitHub Actions Workflow](.github/workflows/docker-publish.yml)** - CI/CD configuration
- **[Dockerfile](Dockerfile)** - Container build instructions

---

## 🔐 Setup for Maintainers

To enable automatic Docker Hub publishing:

### 1. Create Docker Hub Account
- Go to https://hub.docker.com/
- Sign up (free)

### 2. Generate Access Token
- Login → Account Settings → Security
- Create New Access Token
- Name: `github-actions`
- Copy the token

### 3. Add GitHub Secrets
Go to: `GitHub Repo → Settings → Secrets and variables → Actions`

Add two secrets:
```
DOCKER_USERNAME: your-dockerhub-username
DOCKER_PASSWORD: your-access-token-from-step-2
```

### 4. Push and Watch Magic Happen! ✨

---

## 🎯 Use Cases

### For Students
- Run notebooks without installing Python
- Same environment as instructor
- No "it works on my machine" issues

### For Instructors
- Share consistent environment with class
- One command setup for students
- Easy to distribute assignments

### For Teams
- Reproducible research
- Version-controlled environment
- Easy collaboration

---

## 📊 Project Structure

```
Aptech-Advanced-Data-Science/
├── 📄 Dockerfile                    # Container blueprint
├── 📄 docker-compose.yml            # Easy launcher
├── 📄 requirement.txt               # Python dependencies
├── 📄 README.md                     # This file
├── 📄 DOCKER_GUIDE.md              # Detailed tutorial
├── 📁 .github/workflows/            # CI/CD automation
│   └── docker-publish.yml
├── 📁 Session 1/                    # Learning materials
├── 📁 Session 4/                    # Decision Trees
│   └── Tran_Dai_Minh_Session_4_.ipynb
├── 📁 Bai thi thu/                  # Exam practice
└── 📁 Course Files/                 # Datasets
```

---

## 🐛 Troubleshooting

### Container won't start
```bash
docker-compose down
docker-compose up --build
```

### Port 8888 already in use
```bash
# Stop existing Jupyter instances
# Or change port in docker-compose.yml: "9999:8888"
```

### Changes not appearing
```bash
# If you changed Dockerfile or requirements:
docker-compose up --build

# If you changed code:
# Just save the file, it auto-syncs!
```

---

## 📝 License

Educational project for Aptech Advanced Data Science course.

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ for Data Science Education**

*Last Updated: January 28, 2026*
