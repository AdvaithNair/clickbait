import express from 'express';

const app = express();

app.get('/', (req, res) => {
    res.json({ hello: 'world3' });
});

app.listen(4003, () => {
    console.log('Running on 4003...');
});
