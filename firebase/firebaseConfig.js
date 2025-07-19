// Import the functions you need from the SDKs you need
// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAtl0sxUXjbeODeTUXLDMqj49dhoXTsNBc",
  authDomain: "codeforces-rating-update.firebaseapp.com",
  projectId: "codeforces-rating-update",
  storageBucket: "codeforces-rating-update.firebasestorage.app",
  messagingSenderId: "1076825158600",
  appId: "1:1076825158600:web:021c1ef02c83c6992186fd",
  measurementId: "G-3RS0XN8R7W"
};

// Initialize Firebase (using compat SDK loaded via <script>)
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();


// // Initialize Firebase
// const app = initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);