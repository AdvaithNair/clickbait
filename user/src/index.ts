import express from 'express';

const app = express();

app.get('/', (req, res) => {
    res.json({ hello: 'world3' });
});

app.get('/api/user/', (req, res) => {
    res.json({ username: 'gottem' });
});

app.listen(4003, () => {
    console.log('Running on 4003...');
});
