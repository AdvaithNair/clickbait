import axiosController from 'axios';

const PORT: number = 8080;
const baseURL = `http://localhost:${PORT}`;

const axios = axiosController.create({
    baseURL,
    withCredentials: false,
});

export default axios;
