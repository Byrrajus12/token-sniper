import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:5000/api', // Ensure this matches your Flask backend URL
});

export default api;
