import axios from 'axios';

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/', // URL base de tu API
    withCredentials: true, // Asegura que se envíen las cookies de sesión
});

export default instance;