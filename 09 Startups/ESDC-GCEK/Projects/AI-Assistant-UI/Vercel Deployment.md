# 🚀 Vercel Deployment Guide

## Prerequisites

1. **Node.js and npm** installed
2. **Vercel CLI** installed globally
## Quick Deploy

### Option 1: Using the Deploy Script
```bash
# Run the deployment script
./deploy.bat
```

---
id: callout
aliases: []
tags:
  - files
  - templates
  - templater
dg-publish: true
---
> [!abstract]- `deploy.bat`
> ```bat
> @echo off
> echo 🚀 Deploying AI Voice Assistant to Vercel...
> 
> REM Navigate to project directory (if not already there)
> cd /d e:\Git\ES-GCEK\AI-Voice-Assistant-UI\ai_voice_assistant
> 
> REM Check if Flutter is available
> flutter --version >nul 2>&1
> if %errorlevel% neq 0 (
>     echo ❌ Flutter not found! Please install Flutter and add it to PATH.
>     pause
>     exit /b 1
> )
> 
> REM Check if Vercel CLI is installed
> vercel --version >nul 2>&1
> if %errorlevel% neq 0 (
>     echo Installing Vercel CLI...
>     npm install -g vercel
> )
> 
> REM Clean previous builds
> echo 🧹 Cleaning previous builds...
> flutter clean
> 
> REM Build for web with correct base href
> echo 🔨 Building Flutter web app...
> flutter build web --release --base-href /
> 
> REM Check if build was successful
> if not exist "build\web\index.html" (
>     echo ❌ Build failed! Check Flutter configuration.
>     pause
>     exit /b 1
> )
> 
> REM Deploy to Vercel
> echo 📤 Deploying to Vercel...
> vercel --prod build/web
> 
> echo ✅ Deployment complete!
> echo 🌐 Your app should be live at the URL shown above.
> echo 📝 Don't forget to add environment variables in Vercel dashboard if needed.
> ```



### Option 2: Manual Deployment

1. **Install Vercel CLI** (if not already installed):
```bash
npm install -g vercel
```

2. **Login to Vercel**:
```bash
vercel login
```

3. **Deploy to Vercel**:
```bash
vercel --prod
```

## Build Process

The app has already been built for web. If you need to rebuild:

```bash
# Enable web support
flutter config --enable-web

# Build for web
flutter build web --release
```

## Configuration Files

- `vercel.json` - Vercel deployment configuration
- `build/web/` - Web build output directory

> old but once worked.
```json
{
  "version": 2,
  "builds": [
    {
      "src": "build/web",
      "use": "@vercel/static"
    },
    {
      "src": "build/web/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/build/web/$1"
    }
  ]
}
```


## Features Available on Web

✅ **JARVIS Interface** - Interactive robot assistant
✅ **Navigation** - Bottom navigation between screens
✅ **AI Chat** - Chat interface (may have limitations)
✅ **Conversations** - View conversation history
❌ **Map** - Google Maps may not work on web
❌ **Users** - User management features

## Troubleshooting

### Build Issues
If you encounter build issues:
```bash
flutter clean
flutter pub get
flutter build web --release
```

### Deployment Issues
If deployment fails:
```bash
vercel --debug
```

### Web-Specific Issues
- Some native plugins may not work on web
- Geolocation features may be limited
- File system access is restricted

## Environment Variables

If your app uses environment variables, add them in Vercel dashboard:
1. Go to your project in Vercel dashboard
2. Settings → Environment Variables
3. Add your Supabase keys and other configs

## Live URL

After deployment, Vercel will provide a live URL like:
`https://your-project-name.vercel.app`

## Support

For issues with:
- Flutter web: Check Flutter documentation
- Vercel deployment: Check Vercel documentation
- App functionality: Check the main README
