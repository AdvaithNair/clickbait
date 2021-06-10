export interface LightVideo {
    channel: string;
    date: string;
    id: string;
    thumbnail: string;
    title: string;
    views: number;
}

export interface Video extends LightVideo {
    description: string;
    tags: Array<string>;
}
