# Aaron Tarlue Chea — Profile (Black & Gold)

This is a minimal single-page static profile site built with a black & gold theme.

Files:
- index.html
- styles.css
- script.js

Quick preview (from the project folder):

```bash
# using Python 3
python -m http.server 8000
# then open http://localhost:8000

# or with Node (install `serve`):
npx serve .
```

Next steps you might want:
- Replace the placeholder email with your real contact address in `index.html`.
- Add a resume link, profile photo, or portfolio projects section.
- Deploy to GitHub Pages, Netlify, or Vercel.

Add your attached photo
- Save the photo you attached to this conversation as `assets/photo.jpg` (overwrite if needed). The page will load that image automatically into the header.
- If you prefer a different filename or location, update the `src` on the `img` with id `profile-photo` in `index.html`.

Automated optimization (recommended)
- Place the original photo in `assets/photo-original.jpg` (or `photo-original.png`).
- Install the dependency and run the script to generate an optimized `assets/photo.jpg`:

```bash
python -m pip install -r requirements.txt
python scripts/optimize_photo.py
```

This resizes the image to a maximum of 800x800 and writes a compressed JPEG suitable for the web.

## Deploy to GitHub Pages

This site is ready to deploy to GitHub Pages for free hosting.

### Steps:
1. Push this folder to a GitHub repository (create a new repo first).
2. Go to **Settings > Pages** in your repo.
3. Under **Build and deployment**, select:
   - **Source**: `GitHub Actions`
4. The CI/CD workflow (`.github/workflows/deploy.yml`) will automatically deploy on every push to `main` or `master`.
5. Your site will be live at: `https://yourusername.github.io/your-repo-name/`

### Quick GitHub setup:
```bash
cd "c:\Users\Aaron chea\Desktop\My Profile"
git add .
git commit -m "Initial profile commit"
git remote add origin https://github.com/yourusername/your-repo-name.git
git branch -M main
git push -u origin main
```

Then wait ~2 minutes for GitHub Actions to deploy. Check the **Actions** tab in your repo to monitor the deployment.


