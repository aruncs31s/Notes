# Mobile Testing Guide

## Quick Start

The website is now mobile-friendly! To test it:

### 1. Local Testing with Browser DevTools

**Chrome/Edge:**
1. Open http://localhost:5174 in your browser
2. Press `F12` to open DevTools
3. Click the device toggle icon (or press `Ctrl+Shift+M` / `Cmd+Shift+M`)
4. Select a device from the dropdown (iPhone 12 Pro, Pixel 5, etc.)
5. Test both portrait and landscape orientations
6. Try different screen sizes

**Firefox:**
1. Open http://localhost:5174
2. Press `F12` to open DevTools
3. Click the Responsive Design Mode icon (or press `Ctrl+Shift+M`)
4. Select device presets or enter custom dimensions
5. Enable touch simulation

### 2. Test on Your Phone

**Option A: Same Network**
1. Make sure your phone and computer are on the same WiFi network
2. Find your computer's IP address:
   - Windows: `ipconfig` in Command Prompt
   - Mac/Linux: `ifconfig` or `ip addr` in Terminal
3. On your phone, open browser and go to: `http://YOUR_IP:5174`
   - Example: `http://192.168.1.100:5174`

**Option B: Using Vite's Network Option**
1. Stop the current server (Ctrl+C)
2. Run: `npm run dev -- --host`
3. Use the Network URL shown in the terminal on your phone

### 3. Key Areas to Test

#### Navigation
- [ ] Tap the hamburger menu icon
- [ ] Menu slides down smoothly
- [ ] All links are easily tappable
- [ ] Menu closes when clicking a link
- [ ] Logo is visible and properly sized

#### Home Page (ThreeLanding)
- [ ] 3D model renders properly
- [ ] Text is readable
- [ ] Buttons are full-width and easy to tap
- [ ] No horizontal scrolling
- [ ] Works in both orientations

#### Forms & Inputs
- [ ] Tapping inputs doesn't zoom the page
- [ ] Keyboard appears properly
- [ ] Buttons are easy to tap
- [ ] Form validation works
- [ ] Submit buttons are accessible

#### Cards & Content
- [ ] Cards stack vertically on mobile
- [ ] Text is readable without zooming
- [ ] Images scale properly
- [ ] Spacing looks good
- [ ] Tap targets are adequate

#### Tables
- [ ] Tables scroll horizontally if needed
- [ ] Data is readable
- [ ] Action buttons are tappable
- [ ] No layout breaking

#### Footer
- [ ] Content is centered
- [ ] Links are tappable
- [ ] Social icons work
- [ ] Looks good on narrow screens

### 4. Breakpoint Testing

Test at these specific widths:
- **320px** - Small phone (iPhone SE)
- **375px** - Standard phone (iPhone 12/13)
- **414px** - Large phone (iPhone 12 Pro Max)
- **768px** - Tablet portrait (iPad)
- **1024px** - Tablet landscape (iPad)

### 5. Common Issues to Check

❌ **Problems to Look For:**
- Horizontal scrolling (should never happen)
- Text too small to read
- Buttons too small to tap comfortably
- Images overflowing
- Overlapping content
- Menu not working
- Form inputs causing page zoom

✅ **What Should Work:**
- Smooth scrolling
- Easy navigation
- Readable text
- Comfortable tap targets (44x44px minimum)
- Proper spacing
- Fast loading
- Smooth animations

### 6. Performance Testing

Use Chrome DevTools Performance Tab:
1. Open DevTools
2. Go to Performance tab
3. Start recording
4. Interact with the page (scroll, tap, navigate)
5. Stop recording
6. Check for:
   - FPS (should be 60fps)
   - Long tasks
   - Layout shifts

### 7. Lighthouse Audit

1. Open Chrome DevTools
2. Go to Lighthouse tab
3. Select "Mobile" device
4. Check "Performance" and "Accessibility"
5. Click "Generate report"
6. Aim for scores > 90

### 8. Real Device Testing

If possible, test on actual devices:

**iOS:**
- iPhone SE (small screen)
- iPhone 12/13/14 (standard)
- iPhone 14 Pro Max (large)
- iPad (tablet)

**Android:**
- Samsung Galaxy S21 (standard)
- Pixel 5 (standard)
- OnePlus 9 (large)
- Samsung Galaxy Tab (tablet)

### 9. Browser Testing

Test on multiple browsers:
- Safari (iOS) - Primary iOS browser
- Chrome (iOS & Android)
- Firefox (Android)
- Samsung Internet (Android)
- Edge (Android)

### 10. Orientation Testing

For each device, test:
- **Portrait mode** - Standard vertical orientation
- **Landscape mode** - Horizontal orientation
- **Rotation** - Switching between orientations

### 11. Touch Gestures

Test these interactions:
- [ ] Single tap on buttons
- [ ] Scroll up and down
- [ ] Pinch to zoom (should be disabled on controls)
- [ ] Swipe gestures (if any)
- [ ] Long press (if any)

### 12. Accessibility on Mobile

Check:
- [ ] Sufficient color contrast
- [ ] Touch targets at least 44x44px
- [ ] Text readable without zoom
- [ ] Focus indicators visible
- [ ] Keyboard navigation works (for tablets with keyboard)

## Quick DevTools Commands

### Chrome DevTools Device Toolbar Shortcuts:
- `Ctrl+Shift+M` (Windows/Linux) or `Cmd+Shift+M` (Mac) - Toggle device mode
- `Ctrl+Shift+R` - Rotate device
- `Ctrl+Shift+P` - Open command palette
  - Type "Capture screenshot" for full page screenshot
  - Type "Show device frame" to see device bezel

## Network Simulation

Test on slower connections:
1. Open DevTools Network tab
2. Change throttling to:
   - Fast 3G
   - Slow 3G
   - Offline (to test error handling)

## Debugging Tips

### If something looks wrong:

1. **Check Console Errors:**
   ```
   Open DevTools → Console tab
   Look for red error messages
   ```

2. **Inspect Element:**
   ```
   Right-click element → Inspect
   Check applied styles
   Look for overridden CSS
   ```

3. **Test in Isolation:**
   ```
   Navigate to specific page
   Test one component at a time
   ```

4. **Clear Cache:**
   ```
   Ctrl+Shift+Delete (Chrome)
   Clear browsing data
   Reload with Ctrl+Shift+R
   ```

## Success Criteria

Your mobile implementation is successful if:

✅ All content is accessible without horizontal scrolling
✅ Text is readable without zooming (minimum 16px)
✅ All interactive elements are easy to tap (44x44px minimum)
✅ Navigation menu works smoothly
✅ Forms work without page zoom
✅ Images scale properly
✅ Layout adapts to all screen sizes
✅ Performance is good (60fps scrolling)
✅ No layout shifts or jumps
✅ Works in both orientations

## Need Help?

If you encounter issues:
1. Check the console for errors
2. Verify CSS is loading correctly
3. Test on different browsers
4. Check network requests
5. Review the mobile-optimizations.css file

## Additional Tools

- **BrowserStack** - Test on real devices remotely
- **LambdaTest** - Cross-browser testing
- **Google PageSpeed Insights** - Mobile performance
- **GTmetrix** - Performance analysis
- **WebPageTest** - Detailed performance metrics

## Current Status

🎉 **Mobile Implementation: COMPLETE**

All CSS files have been updated with comprehensive mobile optimizations. The website should now work beautifully on all mobile devices!

### Test URL:
- Local: http://localhost:5174
- Network: (Run `npm run dev -- --host` and use the displayed network URL)

Happy testing! 📱✨
