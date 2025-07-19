// Anonymous sign-in first
firebase.auth().signInAnonymously()
  .then((userCredential) => {
    const user = userCredential.user;
    console.log("Signed in anonymously as", user.uid);

    // Attach submit listener only after auth is ready
    document.getElementById('registerForm').addEventListener('submit', function (e) {
      e.preventDefault();

      const email = document.getElementById('email').value.trim();
      const handle = document.getElementById('handle').value.trim();
      const name = document.getElementById('name').value.trim();

      if (!email || !handle || !name) {
        document.getElementById("message").innerText = "All fields are required.";
        return;
      }

      firebase.firestore().collection("users").doc(user.uid).set({
        name: name,
        email: email,
        handle: handle,
        last_rating: 0
      }).then(() => {
        document.getElementById("message").innerText = "User registered successfully!";
      }).catch((error) => {
        document.getElementById("message").innerText = "Error saving user: " + error.message;
      });
    });

  })
  .catch((error) => {
    console.error("Error during anonymous sign-in:", error);
    document.getElementById("message").innerText = "Auth error: " + error.message;
  });
