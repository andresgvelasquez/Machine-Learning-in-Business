import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
    const [files, setFiles] = useState({
        region1: null,
        region2: null,
        region3: null,
    });
    const [message, setMessage] = useState('');

    const onFileChange = (event) => {
        const { name, files } = event.target;
        setFiles(prevFiles => ({
            ...prevFiles,
            [name]: files[0]
        }));
    };

    const onUpload = async () => {
        // Verifica si todos los archivos están presentes
        if (!files.region1 || !files.region2 || !files.region3) {
            setMessage('Please select all files.');
            return;
        }

        const formData = new FormData();
        formData.append('region1', files.region1);
        formData.append('region2', files.region2);
        formData.append('region3', files.region3);

        try {
            await axios.post('http://127.0.0.1:8000/portfolio/upload/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                    'Accept': 'application/json',
                },
                withCredentials: true, // Esto asegura que se envíen las cookies de sesión
            });
            setMessage('Files uploaded successfully!');
        } catch (error) {
            setMessage('Error uploading files.');
            console.error(error);
        }
    };

    return (
        <div>
            <input type="file" name="region1" onChange={onFileChange} />
            <input type="file" name="region2" onChange={onFileChange} />
            <input type="file" name="region3" onChange={onFileChange} />
            <button onClick={onUpload}>Upload</button>
            <p>{message}</p>
        </div>
    );
};

export default FileUpload;