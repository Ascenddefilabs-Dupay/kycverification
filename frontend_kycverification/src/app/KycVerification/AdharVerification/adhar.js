'use client'

import React, { useState } from 'react';
import { useRouter } from 'next/navigation';
import axios from 'axios';
import styles from './AadharForm.module.css';
import ProgressBar from '../kycform1/ProgressBar';

const AadharForm = () => {
  const [aadharNumber, setAadharNumber] = useState('');
  const [aadharFrontImage, setAadharFrontImage] = useState(null);
  const [aadharFrontImageUrl, setAadharFrontImageUrl] = useState(null);
  const [aadharBackImage, setAadharBackImage] = useState(null);
  const [aadharBackImageUrl, setAadharBackImageUrl] = useState(null);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [imageError, setImageError] = useState('');
  const router = useRouter();

  const aadharNumberRegex = /^[0-9 ]{14}$/;

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!aadharNumber || !aadharNumberRegex.test(aadharNumber)) {
      setError('Invalid Aadhar Number format.');
      return;
    }

    if (
      (aadharFrontImage && aadharFrontImage.size > 2 * 1024 * 1024) ||
      (aadharBackImage && aadharBackImage.size > 2 * 1024 * 1024)
    ) {
      setImageError('Image size should be within 2MB.');
      return;
    }

    setError('');
    setImageError('');

    const formData = new FormData();
    formData.append('adhar_number', aadharNumber.replace(/ /g, ''));

    if (aadharFrontImage) {
      formData.append('adhar_front_image', aadharFrontImage);
    }

    if (aadharBackImage) {
      formData.append('adhar_back_image', aadharBackImage);
    }

    try {
      const response = await axios.post('http://localhost:8000/api/kyc-details/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setMessage('Aadhar submitted successfully!');
      setAadharNumber('');
      setAadharFrontImage(null);
      setAadharFrontImageUrl(null);
      setAadharBackImage(null);
      setAadharBackImageUrl(null);

      setTimeout(() => {
        router.push('/KycVerification/PanVerification');
      });

    } catch (error) {
      console.error('Error submitting Aadhar:', error);
      setMessage('Error submitting Aadhar. Please try again.');
    }
  };

  const handleImageChange = (e, setImage, setImageUrl) => {
    const file = e.target.files[0];
    if (file) {
      if (file.size > 2 * 1024 * 1024) {
        setImageError('Image size should be within 2MB.');
        setImage(null);
        setImageUrl(null);
      } else {
        setImageError('');
        setImage(file);
        setImageUrl(URL.createObjectURL(file));
      }
    }
  };

  const handleAadharNumberChange = (e) => {
    const value = e.target.value.replace(/\s/g, '');
    if (value.length <= 12) {
      const formattedValue = value.replace(/(\d{4})(?=\d)/g, '$1 ');
      setAadharNumber(formattedValue);
    }
  };

  return (
    <div className={styles.formContainer}>
      <div className={styles.card}>
        <form onSubmit={handleSubmit} className={styles.form}>
          <h2 className={styles.heading}>Aadhar Verification</h2>
          <ProgressBar step={2} totalSteps={3} />
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
            <label htmlFor="aadhar-front-image" className={styles.label}>
              Upload Aadhar Front Image:
            </label>
            <div className={styles.uploadContainer}>
              <input
                type="file"
                id="aadhar-front-image"
                name="aadhar-front-image"
                accept="image/*"
                className={styles.inputFile}
                onChange={(e) => handleImageChange(e, setAadharFrontImage, setAadharFrontImageUrl)}
                required
              />
              {aadharFrontImageUrl && (
                <img src={aadharFrontImageUrl} alt="Aadhar Front Preview" className={styles.uploadedImage} />
              )}
            </div>
          </div>
          <div className={styles.formGroup}>
            <label htmlFor="aadhar-back-image" className={styles.label}>
              Upload Aadhar Back Image:
            </label>
            <div className={styles.uploadContainer}>
              <input
                type="file"
                id="aadhar-back-image"
                name="aadhar-back-image"
                accept="image/*"
                className={styles.inputFile}
                onChange={(e) => handleImageChange(e, setAadharBackImage, setAadharBackImageUrl)}
                required
              />
              {aadharBackImageUrl && (
                <img src={aadharBackImageUrl} alt="Aadhar Back Preview" className={styles.uploadedImage} />
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
    </div>
  );
};

export default AadharForm;
