# CHANGELOG

All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/) and [Keep a Changelog](http://keepachangelog.com/).



## Unreleased
---

### New

### Changes

### Fixes

### Breaks


## 1.1.1 (2025-07-31)
---

### Changes
- Update project documentation (README)
- Update Python version 3.13 and Node version 20
- Exclude IDE config files.


## 1.1.0 (2025-07-26)
---

### New
- Add poetry configuration to make the project ready to be used as a package [GS-204].
- Add unit tests [GS-204].
- Add 'effective_date_ymd' to the API response with the spanish date format converted to YYYY-MM-DD [GS-204].
- Add timeout and SSL verification settings for BCV API requests [GS-204].

### Changes
- Rename "src" folder to "bcv_exchange_rates" to match the project name [GS-204].
- Return values as float instead of string [GS-204].
- Refactor error handling in currency scraping [GS-204].

### Fixes
- Update dependencies to latest versions to fix Snyk alerts [GS-219].


## 1.0.0 (2023-01-18)
---

### New
- README with better SEO & spanish version

### Changes
- Move vercel.json to parent folder

### Fixes
- CLI python run doesn't find a src.index module error.


## 0.1.0 (2023-01-06)
---

### New
- Initial README instructions
- Ideation and initial development
