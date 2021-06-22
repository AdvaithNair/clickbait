import { formatRelative } from './time';
import { LightVideo, Video } from './types';

const toFixedAbsolute = (value: number) => {
    const n = 1;
    const reg = new RegExp('^-?\\d+(?:\\.\\d{0,' + n + '})?', 'g');
    const a = (value.toString() as any).match(reg)[0];
    const dot = a.indexOf('.');
    if (dot === -1) return a + '.' + '0'.repeat(n);
    const b = n - (a.length - dot) + 1;
    return b > 0 ? a + '0'.repeat(b) : a;
};

export const formatCount = (count: number) => {
    if (count > 999 && count < 1000000)
        return toFixedAbsolute(count / 1000) + 'K';
    else if (count >= 1000000 && count < 1000000000)
        return toFixedAbsolute(count / 1000000) + 'M';
    else if (count >= 1000000000)
        return toFixedAbsolute(count / 1000000000) + 'B';
    else return count.toString();
};

export const formatFullVideo = (item: Video) => {
    item.thumbnail = `https://i.ytimg.com/vi/${item.id}/hqdefault.jpg`;
    item.views = formatCount(item.views ?? 0) as any;
    item.date = formatRelative(item.date);
    item.description.replace(/(?:\r\n|\r|\n)/g, '<br />');
    // TODO: Format Tags
};

export const formatVideo = (item: LightVideo) => {
    item.thumbnail = `https://i.ytimg.com/vi/${item.id}/hqdefault.jpg`;
    item.views = formatCount(item.views ?? 0) as any;
    item.date = formatRelative(item.date);
};

export const formatVideoArray = (array: Array<LightVideo>) => {
    for (const item of array) {
        if (item.id) formatVideo(item);
        else console.log(item);
    }
};
