# Mobile Testing Guide

## Quick Test Instructions

### 1. Open Developer Tools Mobile View

**Chrome/Edge:**
1. Press `F12` or `Ctrl+Shift+I`
2. Click the "Toggle device toolbar" icon (📱) or press `Ctrl+Shift+M`
3. Select different device presets from the dropdown

**Firefox:**
1. Press `F12`
2. Click "Responsive Design Mode" icon or press `Ctrl+Shift+M`

### 2. Test These Devices

#### Required Tests:
- **iPhone SE (375x667)** - Smallest modern iPhone
- **iPhone 12/13 Pro (390x844)** - Standard iPhone
- **iPhone 14 Pro Max (430x932)** - Largest iPhone
- **Samsung Galaxy S20 (360x800)** - Common Android
- **iPad Mini (768x1024)** - Tablet breakpoint

### 3. What to Check

#### ✅ Navigation Bar
```
□ Logo and text are readable
□ Hamburger menu icon is visible and large enough (44px)
□ Menu opens smoothly when tapped
□ Menu items are easy to tap (48px height minimum)
□ Login button is full-width in mobile menu
□ Profile icon shows correctly (no text overflow)
□ Menu closes when clicking a link
□ No items are cut off or hidden
```

#### ✅ Home Screen (Landing Page)
```
□ 3D CPU model is visible and centered
□ Title "ESDC" is prominent and readable
□ Subtitle text doesn't overflow
□ Description text is readable (may hide in landscape)
□ Both CTA buttons are visible and tappable
□ Buttons stack vertically in portrait
□ No horizontal scrolling
□ Content doesn't overlap with navbar
□ Stats overlay (when CPU clicked) displays properly
```

#### ✅ Touch Interactions
```
□ Buttons have visual feedback when tapped
□ Links change color/background on tap
□ Hamburger menu animates smoothly
□ No double-tap zoom on buttons
□ Scrolling is smooth
□ 3D model can be rotated with touch
```

#### ✅ Landscape Mode
```
□ Switch device to landscape orientation
□ Content fits without scrolling
□ Buttons may show horizontally
□ Description might be hidden (intended)
□ Navigation still accessible
```

### 4. Test Specific Features

#### Navigation Menu Animation
```bash
1. Tap hamburger icon → Menu slides down
2. Tap any link → Menu closes smoothly
3. Tap outside menu → Menu closes
4. Scroll within menu → Smooth scroll with momentum
```

#### 3D Canvas Performance
```bash
1. Try rotating the CPU model with touch
2. Check if animations are smooth
3. Look for any lag or stuttering
4. CPU should respond to touch/mouse movement
```

#### Responsive Text
```bash
1. Resize browser window from 320px to 768px
2. Text should scale smoothly
3. No text should overflow containers
4. Line breaks should look natural
```

### 5. Quick Device Simulation

#### Chrome DevTools Commands:
```javascript
// In Console, test different viewport sizes
window.innerWidth  // Check current width
window.innerHeight // Check current height
```

#### Simulate Slow Network (Optional):
1. In DevTools → Network tab
2. Change "No throttling" to "Slow 3G"
3. Reload page to test performance

### 6. Common Issues to Watch For

❌ **Avoid These Problems:**
- Text too small to read (< 14px body text)
- Buttons too small to tap (< 44px)
- Horizontal scroll bar appears
- Content hidden behind navbar
- Menu doesn't close properly
- 3D canvas crashes on low-end devices
- Text overflows containers
- Images not loading or too large

### 7. Browser Testing

Test in these mobile browsers (if possible):
- ✅ Chrome Mobile
- ✅ Safari iOS
- ✅ Firefox Mobile
- ✅ Samsung Internet

### 8. Accessibility Check

```
□ Can navigate using tab key
□ Focus indicators are visible
□ Color contrast is sufficient
□ Touch targets are adequately sized
□ Screen reader compatible
```

## Quick Fixes

### If something looks wrong:

**Text too small?**
→ Check CSS clamp() values in threeLanding.css

**Menu not opening?**
→ Check JavaScript console for errors
→ Verify hamburger button has onClick handler

**Horizontal scroll?**
→ Add `overflow-x: hidden` to problematic container
→ Check for elements with width > 100vw

**3D canvas not showing?**
→ Check WebGL support in browser
→ Try disabling browser extensions

## Testing URL

```
http://localhost:5173/
```

## Responsive Breakpoints Reference

```css
/* Desktop First */
Default: > 768px

/* Tablet/Large Mobile */
@media (max-width: 768px) { ... }

/* Small Mobile */
@media (max-width: 480px) { ... }

/* Landscape Mobile */
@media (max-width: 768px) and (orientation: landscape) { ... }
```

## Performance Expectations

### Good Performance Indicators:
- **FPS**: > 30fps for 3D animations
- **Load Time**: < 3 seconds on 4G
- **Touch Response**: < 100ms
- **Menu Animation**: Smooth 60fps

### If Performance is Poor:
1. Check device pixel ratio setting
2. Disable antialiasing on mobile
3. Reduce particle count
4. Lower 3D model complexity

---

**Server URL**: http://localhost:5173/  
**Test Mode**: Press `Ctrl+Shift+M` in Chrome/Firefox  
**Recommended**: Test on actual mobile devices when possible
