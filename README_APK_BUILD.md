# PNAI Cloud Database Engineer — Android APK project

This is a native Android WebView wrapper around the mobile-first PNAI database-engineering app. It targets Android 6+ (minSdk 23) and should be suitable for the Honor 9 Lite / Android 9.

## Important
This ZIP contains Android project source and a GitHub Actions workflow, **not a precompiled APK**. This environment does not have the Android SDK/Gradle toolchain installed, so the APK must be compiled by GitHub Actions or Android Studio.

## Build using GitHub on your phone
1. Extract this ZIP.
2. Create/open a GitHub repository, for example `pnai-honor9lite`.
3. Upload the *contents* of this folder into the repository root (not the outer folder).
4. Ensure the default branch is `main` or `master`.
5. Open the repository's **Actions** tab.
6. Choose **Build PNAI Android APK** and tap **Run workflow** if it has not run automatically.
7. Open the completed workflow run, scroll to **Artifacts**, and download `PNAI-Honor9Lite-debug-apk`.
8. Extract the downloaded artifact ZIP to obtain `app-debug.apk`.
9. Open the APK on the Honor 9 Lite and follow Android's prompt to allow installation from that source, if asked.

If GitHub mobile hides file upload or Actions controls, use the browser's **Desktop site** option.

## AI response mode
Without an API endpoint, the app provides built-in starter diagnostics and task templates. To enable real AI responses, deploy the optional FastAPI backend from the companion source package, set `OPENAI_API_KEY` as a server environment secret, then set `API_BASE` in `app/src/main/assets/app.js` to the backend's HTTPS URL before building. Do not embed API keys in the APK or commit them to GitHub.

## Safety
No database connections or production changes are performed by this app. It generates draft scripts and advice. Review all scripts and test in non-production before applying them.
