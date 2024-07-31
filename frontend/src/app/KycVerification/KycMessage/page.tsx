'use client';
import React, { useEffect } from 'react';
import ProgressBar from '../kycform1/ProgressBar';

const IDProofAndSelfie = () => {
  useEffect(() => {
    const timer = setTimeout(() => {
      window.location.href = 'https://www.google.com/search?q=react+js+documentation&oq=&gs_lcrp=EgZjaHJvbWUqCQgBECMYJxjqAjIJCAAQIxgnGOoCMgkIARAjGCcY6gIyCQgCECMYJxjqAjIJCAMQIxgnGOoCMgkIBBAjGCcY6gIyCQgFECMYJxjqAjIJCAYQIxgnGOoCMgkIBxAjGCcY6gLSAQkxOTg4MmowajeoAgiwAgE&sourceid=chrome&ie=UTF-8';
    }, 2000); // 5000 milliseconds = 5 seconds
    return () => clearTimeout(timer);
  }, []);

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h2 style={styles.title}>ID Proof</h2><br/><br/>
        <ProgressBar step={3} totalSteps={3} />
        <div style={styles.checkmarkContainer}>
          <div style={styles.checkmark}>✓</div>
        </div>
        <p style={styles.thankYou}>Thank you</p>
        <p style={styles.message}>That's all we need to start verifying your identity</p>
      </div>
    </div>
  );
};

const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: 'whitesmoke',
    padding: '20px',
  },
  card: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    textAlign: 'center',
    backgroundColor: 'white',
    borderRadius: '8px',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.1)',
    padding: '20px',
    maxWidth: '400px',
    width: '100%',
    boxSizing: 'border-box',
  },
  title: {
    margin: 0,
    fontSize: '25px',
    fontWeight: 'bold',
    color: 'black',
  },
  menuButton: {
    backgroundColor: 'transparent',
    border: 'none',
    fontSize: '24px',
    cursor: 'pointer',
  },
  checkmarkContainer: {
    width: '80px',
    height: '80px',
    borderRadius: '50%',
    backgroundColor: '#e0f7fa',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: '20px',
  },
  checkmark: {
    color: '#00bcd4',
    fontSize: '40px',
    animation: 'checkmark-animation 2s ease-in-out',
  },
  thankYou: {
    fontSize: '24px',
    fontWeight: 'bold',
    margin: '0 0 10px 0',
    color: 'black',
  },
  message: {
    fontSize: '16px',
    color: '#777',
  },
}

export default IDProofAndSelfie;
