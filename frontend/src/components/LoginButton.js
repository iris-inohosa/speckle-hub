import React, { useState } from 'react';

const LoginButton = () => {
  // Local state to manage authentication status
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Handle login redirection
  const handleLogin = () => {
    // Here, you would perform the login logic
    // For example, redirect to the login page, or authenticate the user
    setIsAuthenticated(true); // Set the user as authenticated (mock for now)
    window.location = `${process.env.REACT_APP_SERVER_URL}/authn/verify/${process.env.REACT_APP_SPECKLE_ID}/${"challenge-value"}`; // Redirect to the URL
  };

  // Handle logout
  const handleLogout = () => {
    setIsAuthenticated(false); // Set the user as logged out
  };

  return (
    <div>
      {!isAuthenticated ? (
        <button
          className="outlined-button"
          onClick={handleLogin}
        >
          <span>Login with Speckle</span>
        </button>
      ) : (
        <button
          className="outlined-button"
          onClick={handleLogout}
        >
          Log out
        </button>
      )}
    </div>
  );
};

export default LoginButton;
