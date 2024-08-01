'use client'

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import axios from 'axios';
import styles from './PanForm.module.css';

const PanForm = () => {
  const [panNumber, setPanNumber] = useState('');
  const [panImage, setPanImage] = useState(null);
  const [panImageUrl, setPanImageUrl] = useState(null);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [imageError, setImageError] = useState('');
  const router = useRouter();

  const panNumberRegex = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!panNumber || !panNumberRegex.test(panNumber)) {
      setError('Invalid PAN Number format.');
      return;
    }

    if (panImage && panImage.size > 2 * 1024 * 1024) { // Check for image size
      setImageError('Image size should be within 2MB.');
      return;
    }

    setError('');
    setImageError('');

    const formData = new FormData();
    formData.append('pan_number', panNumber);

    if (panImage) {
      formData.append('pan_image', panImage);
    }

    try {
      const response = await axios.post('http://localhost:8000/api/kyc-details/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setMessage('PAN submitted successfully!');
      setPanNumber('');
      setPanImage(null);
      setPanImageUrl(null);

      setTimeout(() => {
        router.push('/KycVerification/AdharVerification');
      }, 2000);

    } catch (error) {
      console.error('Error submitting PAN:', error);
      setMessage('Error submitting PAN. Please try again.');
    }
  };

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      if (file.size > 2 * 1024 * 1024) {
        setImageError('Image size should be within 2MB.');
        setPanImage(null);
        setPanImageUrl(null);
      } else {
        setImageError('');
        setPanImage(file);
        setPanImageUrl(URL.createObjectURL(file));
      }

      
    }
  };

  const handlePanNumberChange = (e) => {
    const value = e.target.value.toUpperCase();
    if (value.length <= 10) {
      setPanNumber(value);
    }
  };

  return (
    <div className={styles.formContainer}>
      <form onSubmit={handleSubmit} className={styles.form}>
        <h2 className={styles.heading}>PAN Verification</h2>
        <div className={styles.formGroup}>
          <label htmlFor="pan-number" className={styles.label}>
            PAN Number:
          </label>
          <input
            type="text"
            id="pan-number"
            name="pan-number"
            placeholder="Enter PAN Number"
            className={styles.input}
            value={panNumber}
            onChange={handlePanNumberChange}
            required
          />
        </div>
        {error && <p className={styles.error}>{error}</p>}
        <div className={styles.formGroup}>
          <label htmlFor="pan-image" className={styles.label}>
            Upload PAN Image (Optional):
          </label>
          <div className={styles.uploadContainer}>
            <input
              type="file"
              id="pan-image"
              name="pan-image"
              accept="image/*"
              className={styles.inputFile}
              onChange={handleImageChange}
            />
            {panImageUrl && (
              <img src={panImageUrl} alt="PAN Preview" className={styles.uploadedImage} />
            )}
          </div>
        </div>
        {imageError && <p className={styles.error}>{imageError}</p>}
        <button type="submit" className={styles.submitButton} disabled={imageError !== ''}>
          Submit
        </button>
        {message && <p className={styles.message}>{message}</p>}
      </form>
    </div>
  );
};

export default PanForm;
