document.getElementById("signup-form").addEventListener("submit", function(e) {
    e.preventDefault();
  
    const formData = {
      name: document.getElementById("name").value,
      email: document.getElementById("email").value,
      password: document.getElementById("password").value
    };
  
    fetch("http://127.0.0.1:8080"/signup, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(formData)
    })
      .then(res => res.json())
      .then(data => {
        console.log("Response from backend:", data);
        alert("Signed up successfully!");
      })
      .catch(err => {
        console.error("Error:", err);
      });
  });
  