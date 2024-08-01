'use client'
import { useState, useEffect } from 'react';
import axios from 'axios';
import { useRouter } from 'next/navigation';
import styles from './DocumentForm.module.css';
import ProgressBar from './ProgressBar';

const countries = [
    'United States', 'Canada', 'United Kingdom', 'Australia', 'Germany', 'France', 'India', 'Japan', 'China', 'Brazil',
];

const documentOptions = {
    India: ['PanCard'],
    Default: ['Passport']
};

const DocumentForm = () => {
    const [country, setCountry] = useState(countries[0]);
    const [documentType, setDocumentType] = useState('');
    const router = useRouter();

    useEffect(() => {
        if (documentType) {
            const handleSaveAndRedirect = async () => {
                const data = { country, document_type: documentType };
                try {
                    await axios.post('http://localhost:8000/api/documents/', data);
                    alert('Document saved successfully!');
                    // Define redirection URLs based on document type
                    let redirectUrl = '';
                    if (documentType === 'PanCard') {
                        redirectUrl = 'http://localhost:3000/kycverification/PanVerification';
                    } else if (documentType === 'AdharCard') {
                        redirectUrl = 'http://localhost:3000/kycverification/AdharVerification';
                    } else {
                        redirectUrl = 'http://localhost:3000/kycverification/kyc3'; // Default redirection
                    }
                    router.push(redirectUrl);
                } catch (error) {
                    console.error('There was an error saving the document!', error);
                }
            };

            handleSaveAndRedirect();
        }
    }, [documentType, country, router]);

    const availableDocuments = country === 'India' ? documentOptions.India : documentOptions.Default;

    return (
        <div className={styles.container}>
            <div className={styles.card}>
                <form>
                    <h1 className={styles.h1}>ID Proof</h1><br/>
                    <ProgressBar step={2} totalSteps={3} />
                    <label className={styles.label}><br/>
                        Issuing country:</label>
                        <select 
                            value={country} 
                            onChange={(e) => setCountry(e.target.value)} 
                            className={styles.select}
                        >
                            {countries.map((country) => (
                                <option key={country} value={country}>{country}</option>
                            ))}
                        </select>                    
                    <br />
                    <div className={styles.documentButtons}>
                        <label className={styles.label}>Document Type:</label>
                        {availableDocuments.map((doc) => (
                            <button 
                                type="button" 
                                key={doc} 
                                className={`${styles.button} ${documentType === doc ? styles.activeButton : ''}`}
                                onClick={() => setDocumentType(doc)}
                            >
                                {doc}
                            </button>
                        ))}
                    </div>
                </form>
            </div>
        </div>
    );
};

export default DocumentForm;
