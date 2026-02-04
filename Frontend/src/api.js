import axios from 'axios';

export const API_BASE = 'https://quess-crop.onrender.com';

const api = axios.create({
  baseURL: API_BASE,
  timeout: 10000,
});

export default api;
