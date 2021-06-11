import { Video } from './types';

export const defaultLightVideo = {
    id: '',
    views: 0,
    thumbnail:
        'https://www.mandlpaints.com/wp-content/uploads/2018/09/Lead-Gray-600x600.jpg',
    date: new Date().toString(),
    title: 'Loading...',
    channel: 'Loading...',
};

export const defaultVideo: Video = {
    ...defaultLightVideo,
    description: 'Loading...',
    tags: [],
    src: '',
};
