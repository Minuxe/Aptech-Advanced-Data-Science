# ✅ GitHub Actions + Docker Hub Setup Checklist

## Quick Setup Guide - Follow in Order

### 📋 Pre-requisites
- [ ] Git installed on your computer
- [ ] Docker installed on your computer
- [ ] GitHub account created
- [ ] Project pushed to GitHub

---

## 🎯 Step 1: Docker Hub Account (5 minutes)

- [ ] Go to https://hub.docker.com/
- [ ] Click "Sign Up"
- [ ] Fill in:
  - Username: `________________`
  - Email: `________________`
  - Password: `________________`
- [ ] Verify email
- [ ] Login successful ✅

---

## 🎯 Step 2: Generate Access Token (2 minutes)

- [ ] Login to Docker Hub
- [ ] Click profile icon → **Account Settings**
- [ ] Left menu → **Security**
- [ ] Click **New Access Token**
- [ ] Description: `github-actions`
- [ ] Permissions: **Read, Write, Delete**
- [ ] Click **Generate**
- [ ] **COPY THE TOKEN NOW** (you'll only see it once!)
- [ ] Token saved: `dckr_pat_________________`

---

## 🎯 Step 3: Add Secrets to GitHub (3 minutes)

- [ ] Go to your GitHub repository
- [ ] Click **Settings** tab
- [ ] Left menu → **Secrets and variables** → **Actions**
- [ ] Click **New repository secret**

### First Secret:
- [ ] Name: `DOCKER_USERNAME`
- [ ] Value: `your-dockerhub-username`
- [ ] Click **Add secret**

### Second Secret:
- [ ] Click **New repository secret** again
- [ ] Name: `DOCKER_PASSWORD`
- [ ] Value: `paste-your-token-from-step-2`
- [ ] Click **Add secret**

### Verify:
- [ ] Both secrets visible in list
- [ ] Names match exactly (case-sensitive!)

---

## 🎯 Step 4: Verify Files Exist (1 minute)

Check these files are in your project:

```bash
# Run these commands in your terminal
ls -la .github/workflows/docker-publish.yml
ls -la Dockerfile
ls -la docker-compose.yml
ls -la requirement.txt
ls -la README.md
```

- [ ] `.github/workflows/docker-publish.yml` exists
- [ ] `Dockerfile` exists
- [ ] `docker-compose.yml` exists
- [ ] `requirement.txt` exists
- [ ] `README.md` exists

---

## 🎯 Step 5: Push to GitHub (2 minutes)

```bash
# In your project directory:
git add .
git commit -m "Add CI/CD workflow for Docker Hub"
git push origin main
```

- [ ] Files added
- [ ] Committed
- [ ] Pushed to GitHub ✅

---

## 🎯 Step 6: Watch Build (5 minutes)

- [ ] Go to GitHub repository
- [ ] Click **Actions** tab
- [ ] See workflow: "Build and Push Docker Image"
- [ ] Status: 🟡 Running...
- [ ] Wait for completion...
- [ ] Status: ✅ Success!
- [ ] Click on workflow to see details
- [ ] All steps green ✅

**If failed:** Check the logs for error messages

---

## 🎯 Step 7: Verify on Docker Hub (1 minute)

- [ ] Go to https://hub.docker.com/
- [ ] Login
- [ ] Click **Repositories**
- [ ] Find: `your-username/aptech-data-science`
- [ ] See tag: **latest** ✅
- [ ] See last updated: just now ✅
- [ ] Copy pull command

---

## 🎯 Step 8: Test the Image (2 minutes)

```bash
# On any computer (even your friend's):
docker pull YOUR-USERNAME/aptech-data-science:latest
docker run -p 8888:8888 YOUR-USERNAME/aptech-data-science:latest
```

- [ ] Image pulled successfully
- [ ] Container started
- [ ] Open browser: http://localhost:8888
- [ ] Jupyter Notebook loads ✅
- [ ] Can open notebooks ✅

---

## 🎉 Success Checklist

- [ ] ✅ Docker Hub account created
- [ ] ✅ Access token generated
- [ ] ✅ GitHub secrets configured
- [ ] ✅ Workflow file pushed
- [ ] ✅ Build completed successfully
- [ ] ✅ Image visible on Docker Hub
- [ ] ✅ Image can be pulled and run
- [ ] ✅ Jupyter works in container

---

## 🔄 From Now On...

Every time you push code to GitHub:

```bash
git add .
git commit -m "Your changes"
git push origin main
```

**Automatically happens:**
1. GitHub Actions detects push
2. Builds new Docker image
3. Pushes to Docker Hub
4. Available worldwide!

**You just need to:**
- Write code
- Push to GitHub
- Done! ✨

---

## 🐛 Troubleshooting

### Build fails with "Login failed"
- Check `DOCKER_USERNAME` secret is correct
- Check `DOCKER_PASSWORD` secret is your token (not password)
- Regenerate token if needed

### Build fails at "Build and push"
- Check Dockerfile syntax
- Check requirement.txt has valid packages
- Check GitHub Actions logs for details

### Image not appearing on Docker Hub
- Check build completed successfully (green checkmark)
- Check Docker Hub username in secrets is correct
- Refresh Docker Hub page

### Can't pull image
- Check image name matches exactly
- Check image is public on Docker Hub
- Try: `docker login` first

---

## 📚 Next Steps

1. Share your Docker Hub link with others
2. Update README.md with your actual username
3. Update docker-compose.yml with your username (for Option 1)
4. Tell your team/professor: "Just run `docker pull your-username/aptech-data-science`"

---

## 📞 Need Help?

- GitHub Actions logs: `https://github.com/YOUR-USERNAME/YOUR-REPO/actions`
- Docker Hub: `https://hub.docker.com/r/YOUR-USERNAME/aptech-data-science`
- Check [DOCKER_GUIDE.md](DOCKER_GUIDE.md) for detailed explanations

---

**Total Setup Time: ~20 minutes**

**Time Saved Forever: Hours per week!** 🎉

*Last Updated: January 28, 2026*
