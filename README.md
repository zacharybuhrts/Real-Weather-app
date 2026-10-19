# Real Weather

A desktop window around the Daylight weather page. Forecasts come from [Open-Meteo](https://open-meteo.com/). No API key is required.

The page in `ui/index.html` is the Daylight weather client from [zacharybuhrts/daylight-weather](https://github.com/zacharybuhrts/daylight-weather) at commit `5a88b3141a90654664e65300dd04aaa08f634fe9`, unchanged. This repository previously had no application source, only this readme.

The Mac app is a [Tauri](https://v2.tauri.app/) shell: a native window that loads that same page. Tauri fits a single HTML file better than Electron (no bundled browser) and better than a Python freezer, because the app is not a Python program.

## Download and open on a Mac

The build is for Apple Silicon (arm64), including a MacBook Neo. It is not signed with an Apple Developer ID, so macOS asks for one extra confirmation the first time you open it.

1. Merge the packaging pull request so the workflow is on `main`.
2. On GitHub, open **Actions → Build macOS app → Run workflow**, leave **Publish a GitHub Release** checked, and run it. Pushing a version tag such as `v1.0.0` builds the same disk image and publishes a release too.
3. When the run finishes, download the `.dmg` from the [Releases](https://github.com/zacharybuhrts/Real-Weather-app/releases) page, or from the workflow run’s **Real-Weather-macos-arm64** artifact.
4. Open the `.dmg` and drag **Real Weather** into **Applications**.
5. In Finder, **right-click Real Weather → Open**, then click **Open** in the dialog. A normal double-click is blocked until you do this once, because the app is unsigned.
6. If macOS says the app is damaged, or the dialog has no Open button, run this in Terminal and then right-click → Open again:

   ```bash
   xattr -cr "/Applications/Real Weather.app"
   ```

Nothing else has to be configured. The app needs a network connection for a live forecast. If the weather service cannot be reached, the page shows the same offline fallback as before (a typical Marysville, Ohio forecast).

## Build the disk image yourself

On an Apple Silicon Mac, with Node.js 22, Rust, and Xcode Command Line Tools:

```bash
npm ci
npm run build:mac
```

The disk image is written to `src-tauri/target/aarch64-apple-darwin/release/bundle/dmg/`.

`npm run desktop` opens a local dev window. The dock icon source is `assets/icon.png` (`python3 scripts/make-icon.py`, then `npx tauri icon assets/icon.png`).
