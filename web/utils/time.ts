import dayjs from 'dayjs';
import relativeTime from 'dayjs/plugin/relativeTime';

// Formats Date
export const formatDate = (date: string | Date): string => {
    return dayjs(date).format('MMMM D, YYYY');
};

// Formats Time
export const formatTime = (date: string | Date): string => {
    return dayjs(date).format('h:mm A');
};

// Formats Relative Time
export const formatRelative = (date: string | Date): string => {
    dayjs.extend(relativeTime);
    return dayjs(date).fromNow();
};

// Formats Total Days
export const formatDays = (date: string | Date) => {
    return dayjs().diff(date, 'day');
};

// Gets Difference in Time between Two Dates
export const getDiffInDays = (
    dateOne: string | Date,
    dateTwo: string | Date,
) => {
    return dayjs(dateOne).diff(dateTwo, 'day');
};

/**
 * Causes Program to Wait for a few seconds
 * @param seconds - number of seconds to wait, default is 5
 */
export const sleep = (seconds = 5) => {
    const waitTill = new Date(new Date().getTime() + seconds * 1000);
    while (waitTill > new Date()) {}
};
