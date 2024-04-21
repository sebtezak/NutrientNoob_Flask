// Validating Password, Longer than 8 characters and needs at least 1 number and 1 capital letter
function isValidPassword(password) {
    if (password.length < 8) {
      return false;
    }
    if (!/[A-Z]/.test(password)) {
      return false;
    } 
    if (!/\d/.test(password)) {
      return false;
    }
    return true;
  }
  
  // Saves user information to local storage
  function saveUserToLocalStorage(username, email, password) {
    const user = { username, email, password };
    localStorage.setItem(username, JSON.stringify(user));
  }
  
  // Retrieves user information from local storage
  function getUserFromLocalStorage(username) {
    const userString = localStorage.getItem(username);
    return userString ? JSON.parse(userString) : null;
  }
  
  // Checks if username already exists in local storage
  function isExistingUsername(username) {
    return localStorage.getItem(username) !== null;
  }
  
  // Checks if any field is empty (made for the text boxes)
  function isEmptyField(field) {
    return field.value.trim() === '';
  }
  
  // This deals with the Sign Up form
  document.addEventListener('DOMContentLoaded', function() {
    const signupForm = document.querySelector('.signup form');
    if (signupForm) {
      signupForm.addEventListener('submit', function(event) {
        event.preventDefault();
  
        const usernameInput = this.querySelector('input[placeholder="Username"]');
        const emailInput = this.querySelector('input[placeholder="Email"]');
        const passwordInput = this.querySelector('input[placeholder="Password"]');
        const confirmPasswordInput = this.querySelector('input[placeholder="Confirm Password"]');
  
        if (isEmptyField(usernameInput) || isEmptyField(emailInput) || isEmptyField(passwordInput) || isEmptyField(confirmPasswordInput)) {
          alert('Please fill in all the text boxes.');
          return;
        }
  
        const username = usernameInput.value;
        const email = emailInput.value;
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;
  
        if (isExistingUsername(username)) {
          alert('Username already exists. Please choose a different username.');
          return;
        }
  
        if (password !== confirmPassword) {
          alert('Passwords do not match. Please try again.');
          return;
        }
  
        if (!isValidPassword(password)) {
          alert('Password must be at least 8 characters long, contain at least 1 capital letter and 1 number.');
          return;
        }
  
        // Saves the users information to local storage (successful Sign Up)
        saveUserToLocalStorage(username, email, password);
        alert('Sign up successful! You can now log in.');
        window.location.href = 'login.html';
      });
    } 
  
    // This deals with the Login form
    const loginForm = document.querySelector('.login form');
    if (loginForm) {
      loginForm.addEventListener('submit', function(event) {
        event.preventDefault();
  
        const usernameInput = this.querySelector('input[placeholder="Username"]');
        const passwordInput = this.querySelector('input[placeholder="Password"]');
  
        if (isEmptyField(usernameInput) || isEmptyField(passwordInput)) {
          alert('Please fill in all the text boxes.');
          return;
        }
  
        const username = usernameInput.value;
        const password = passwordInput.value;
  
        const user = getUserFromLocalStorage(username);
  
        if (!user || user.password !== password) {
          alert('Invalid username or password. Please try again.');
          return;
        }
  
        // Change this part to link straight to their account page
        alert('Log in successful!');
      });
    }
  });
