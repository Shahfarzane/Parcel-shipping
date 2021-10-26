importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-app.js");
importScripts("https://www.gstatic.com/firebasejs/8.2.1/firebase-messaging.js");

firebase.initializeApp({
  apiKey: "AIzaSyCu6QMLgaMZzTf1VlsAoWXUdBjsgy1D9FU",
  authDomain: "bizlutionp.firebaseapp.com",
  projectId: "bizlutionp",
  storageBucket: "bizlutionp.appspot.com",
  messagingSenderId: "439262773983",
  appId: "1:439262773983:web:ddc212593dff048e651f6a",
});

const messaging = firebase.messaging();
