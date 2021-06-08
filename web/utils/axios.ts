import axiosController from 'axios';

const PORT: number = 5002;
const baseURL = `http://localhost:${PORT}`;

const axios = axiosController.create({
    baseURL,
    withCredentials: false,
});

export default axios;
