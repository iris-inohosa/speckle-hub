import React, { useState, useEffect } from 'react';
import LoginButton from "./components/LoginButton.js"
// You can import your image as well
import speckle_img from "./assets/speckle_img.png"

const App = () => {
  // State to handle authentication
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Function to simulate the login action
  const handleLogin = () => {
    // Perform login logic here (for example, redirecting to authentication)
    setIsAuthenticated(true);
    // Redirect to Speckle authentication URL
    window.location = `https://app.speckle.systems/authn/verify/23663a9bda/123`;
  };

  // Function to simulate the logout action
  const handleLogout = () => {
    setIsAuthenticated(false);
  };

  return (
    <div>
      {/* App Bar */}
      <div style={styles.appBar}>
        <div style={styles.appBarContent}>
          <img
            alt="Speckle Logo"
            src={speckle_img}
            style={styles.speckle_img}
          />
          <h3>SPECKLE DEMO APP</h3>
        </div>
        
        {/* Spacer */}
        <div style={{ flexGrow: 1 }}></div>

        {/* Buttons */}
        {!isAuthenticated ? (
          <button style={styles.button} onClick={handleLogin}>
            <LoginButton/>
          </button>
        ) : (
          <button style={styles.button} onClick={handleLogout}>
            Log out
          </button>
        )}
      </div>

      {/* Main content */}
      <div style={styles.mainContent}>
        {/* You can render additional components or routes here */}
      </div>
    </div>
  );
};

// Simple inline styles for layout
const styles = {
  appBar: {
    backgroundColor: '#1976d2', // Primary color
    color: '#fff',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '10px 20px',
  },
  appBarContent: {
    display: 'flex',
    alignItems: 'center',
  },
  speckleLogo: {
    marginRight: '10px',
    width: '40px',
    height: '24px',
  },
  button: {
    border: '2px solid #1976d2',
    backgroundColor: 'transparent',
    color: '#1976d2',
    padding: '8px 16px',
    cursor: 'pointer',
    borderRadius: '4px',
    margin: '0 10px',
  },
  mainContent: {
    padding: '20px',
  }
};

export default App;
