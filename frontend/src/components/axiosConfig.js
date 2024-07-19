// src/axiosConfig.js
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:8000/portfolio/', // Base URL de tu backend
  withCredentials: true, // Asegúrate de enviar cookies de sesión
});

export default axiosInstance;