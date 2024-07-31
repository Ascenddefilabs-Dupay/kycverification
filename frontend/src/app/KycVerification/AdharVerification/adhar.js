'use client'

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import styles from './AadharForm.module.css';
import axios from 'axios';

const AadharForm = () => {
  const [aadharNumber, setAadharNumber] = useState('');
  const [aadharImage, setAadharImage] = useState(null);
  const [aadharImageUrl, setAadharImageUrl] = useState(null);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [imageError, setImageError] = useState('');
  const router = useRouter();

  const aadharNumberRegex = /^\d{12}$/;

  const formatAadharNumber = (value) => {
    return value.replace(/\D/g, '').replace(/(\d{4})(?=\d)/g, '$1 ').substring(0, 14);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const plainAadharNumber = aadharNumber.replace(/\s/g, ''); // Remove spaces for validation

    if (!plainAadharNumber || !aadharNumberRegex.test(plainAadharNumber)) {
      setError('Invalid Aadhar Number format.');
      return;
    }

    if (aadharImage && aadharImage.size > 2 * 1024 * 1024) { // Check for image size
      setImageError('Image size should be within 2MB.');
      return;
    }

    setError('');
    setImageError('');

    const formData = new FormData();
    formData.append('adhar_number', plainAadharNumber);

    if (aadharImage) {
      formData.append('adhar_image', aadharImage);
    }

    try {
      const response = await axios.post('http://localhost:8000/api/kyc-details/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setMessage('Aadhar submitted successfully!');
      setAadharNumber('');
      setAadharImage(null);
      setAadharImageUrl(null);

      setTimeout(() => {
        router.push('/KycVerification/KycMessage');
      }, 2000);

    } catch (error) {
      console.error('Error submitting Aadhar:', error);
      setMessage('Error submitting Aadhar.');
    }
  };

  const handleImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      if (file.size > 2 * 1024 * 1024) {
        setImageError('Image size should be within 2MB.');
        setAadharImage(null);
        setAadharImageUrl(null);
      } else {
        setImageError('');
        setAadharImage(file);
        setAadharImageUrl(URL.createObjectURL(file));
      }
    }
  };

  const handleAadharNumberChange = (event) => {
    const value = event.target.value.replace(/\s/g, ''); // Remove spaces
    if (/^\d{0,12}$/.test(value)) {
      setAadharNumber(formatAadharNumber(value));
    }
  };

  const isFormValid = () => {
    const plainAadharNumber = aadharNumber.replace(/\s/g, ''); // Remove spaces for validation
    return aadharNumberRegex.test(plainAadharNumber) && aadharImage && !imageError;
  };

  return (
    <div className={styles.formContainer}>
      <form onSubmit={handleSubmit} className={styles.form}>
        <h2 className={styles.heading}>Aadhar Verification</h2>
        <div className={styles.formGroup}>
          <label htmlFor="aadhar-number" className={styles.label}>
            Aadhar Number:
          </label>
          <input
            type="text"
            id="aadhar-number"
            name="aadhar-number"
            placeholder="Enter Aadhar Number"
            className={styles.input}
            value={aadharNumber}
            onChange={handleAadharNumberChange}
            required
          />
        </div>
        {error && <p className={styles.error}>{error}</p>}
        <div className={styles.formGroup}>
          <label htmlFor="aadhar-image" className={styles.label}>
            Upload Image:
          </label>
          <div className={styles.uploadContainer}>
            <input
              type="file"
              id="aadhar-image"
              name="aadhar-image"
              accept="image/*"
              className={styles.inputFile}
              onChange={handleImageChange}
              required
            />
            {aadharImageUrl && (
              <img src={aadharImageUrl} alt="Aadhar Preview" className={styles.uploadedImage} />
            )}
          </div>
        </div>
        {imageError && <p className={styles.error}>{imageError}</p>}
        <button type="submit" className={styles.submitButton} disabled={!isFormValid()}>
          Submit
        </button>
        {message && <p className={styles.message}>{message}</p>}
      </form>
    </div>
  );
};

export default AadharForm;
