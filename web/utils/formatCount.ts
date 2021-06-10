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
    if (count > 999 && count < 10000)
        return count.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
    else if (count >= 10000 && count < 1000000)
        return toFixedAbsolute(count / 1000) + 'K';
    else if (count >= 1000000 && count < 1000000000)
        return toFixedAbsolute(count / 1000000) + 'M';
    else if (count >= 1000000000)
        return toFixedAbsolute(count / 1000000000) + 'B';
    else return count.toString();
};
