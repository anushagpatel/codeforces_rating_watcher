# Codeforces Rating Watcher

A background job and email notifier built using **Firebase**, **Azure Functions**, and **Python** that alerts registered users when their Codeforces rating changes.


## Features

- Collects Codeforces handles, names, and emails via a web form.
- Stores data in **Firebase Firestore**.
- Periodically checks for rating changes using **Azure Timer Triggers**.
- Sends notification emails to users whose ratings have changed.
- GitHub Push Protection enabled to avoid secrets in repo.

---

## Tech Stack

- **Frontend**: HTML5 form, CSS, Javascript
- **Backend**: Azure Functions (Python)
- **Database**: Firestore (Firebase)
- **Email Service**: SMTP (via Python `smtplib`)
- **Cloud Infra**: Azure Functions (Timer Trigger), Firebase Admin SDK

---

## ⚙️ Setup

1. **Clone the repo**  
```bash
git clone https://github.com/anushagpatel/codeforces_rating_watcher.git
cd codeforces_rating_watcher
